# #251 「Smart Component - 賢いコンポーネント」

## 概要
Smart Component（賢いコンポーネント）は、ビジネスロジック、データ取得、状態管理を担当するコンポーネントです。サービスを注入し、アプリケーションの頭脳として機能します。表示ロジックは持たず、Dumb Componentに委譲することで、関心の分離を実現します。

## 学習目標
- Smart Componentの役割と責任を理解する
- ビジネスロジックの適切な配置方法を習得する
- データフローの制御方法を学ぶ

## 技術ポイント
- **ビジネスロジック**: データ処理、バリデーション
- **サービス注入**: 依存性注入の活用
- **状態管理**: Signal、RxJSでの状態制御

## 📺 画面表示用コード

### 基本的なSmart Component
```typescript
@Component({
  selector: 'app-user-list-container',
  template: `
    <app-user-list
      [users]="users()"
      [loading]="loading()"
      (userSelected)="onUserSelected($event)"
    />
  `
})
export class UserListContainerComponent {
  private userService = inject(UserService);

  users = signal<User[]>([]);
  loading = signal(true);

  ngOnInit() {
    this.loadUsers();
  }

  async loadUsers() {
    this.loading.set(true);
    const data = await this.userService.getUsers();
    this.users.set(data);
    this.loading.set(false);
  }

  onUserSelected(user: User) {
    this.router.navigate(['/users', user.id]);
  }
}
```

### サービス連携
```typescript
@Component({
  selector: 'app-product-container',
  template: `
    <app-product-display
      [product]="product()"
      (addToCart)="handleAddToCart($event)"
    />
  `
})
export class ProductContainerComponent {
  private productService = inject(ProductService);
  private cartService = inject(CartService);

  product = signal<Product | null>(null);

  async handleAddToCart(product: Product) {
    await this.cartService.add(product);
    this.showNotification('カートに追加しました');
  }
}
```

### 状態管理
```typescript
@Component({
  selector: 'app-todo-container'
})
export class TodoContainerComponent {
  private todoStore = inject(TodoStore);

  todos = this.todoStore.todos;
  filter = this.todoStore.filter;

  addTodo(text: string) {
    this.todoStore.add({ text, completed: false });
  }

  toggleTodo(id: string) {
    this.todoStore.toggle(id);
  }

  setFilter(filter: 'all' | 'active' | 'completed') {
    this.todoStore.setFilter(filter);
  }
}
```

## 実践的な活用例

### データ取得と変換
```typescript
@Component({
  selector: 'app-dashboard-container',
  template: `
    <app-dashboard
      [stats]="stats()"
      [chartData]="chartData()"
      [loading]="loading()"
      (refresh)="refresh()"
    />
  `
})
export class DashboardContainerComponent implements OnInit {
  private analyticsService = inject(AnalyticsService);

  rawData = signal<RawAnalytics | null>(null);
  loading = signal(false);

  // 計算されたデータ
  stats = computed(() => {
    const data = this.rawData();
    if (!data) return null;

    return {
      totalUsers: data.users.length,
      activeUsers: data.users.filter(u => u.active).length,
      revenue: data.transactions.reduce((sum, t) => sum + t.amount, 0)
    };
  });

  chartData = computed(() => {
    const data = this.rawData();
    if (!data) return [];

    return data.transactions.map(t => ({
      date: t.date,
      amount: t.amount
    }));
  });

  async ngOnInit() {
    await this.loadData();
  }

  async loadData() {
    this.loading.set(true);
    try {
      const data = await this.analyticsService.getData();
      this.rawData.set(data);
    } catch (error) {
      console.error('データ取得エラー:', error);
    } finally {
      this.loading.set(false);
    }
  }

  async refresh() {
    await this.loadData();
  }
}
```

### フォーム処理
```typescript
@Component({
  selector: 'app-user-form-container',
  template: `
    <app-user-form
      [initialValue]="user()"
      [saving]="saving()"
      [errors]="errors()"
      (submit)="handleSubmit($event)"
      (cancel)="handleCancel()"
    />
  `
})
export class UserFormContainerComponent {
  private userService = inject(UserService);
  private router = inject(Router);
  private route = inject(ActivatedRoute);

  user = signal<User | null>(null);
  saving = signal(false);
  errors = signal<ValidationErrors>({});

  async ngOnInit() {
    const userId = this.route.snapshot.params['id'];
    if (userId) {
      const user = await this.userService.getUser(userId);
      this.user.set(user);
    }
  }

  async handleSubmit(formValue: UserFormData) {
    // バリデーション
    const validationErrors = this.validate(formValue);
    if (Object.keys(validationErrors).length > 0) {
      this.errors.set(validationErrors);
      return;
    }

    // 保存処理
    this.saving.set(true);
    this.errors.set({});

    try {
      if (this.user()?.id) {
        await this.userService.update(this.user()!.id, formValue);
      } else {
        await this.userService.create(formValue);
      }
      this.router.navigate(['/users']);
    } catch (error) {
      this.errors.set({ server: 'サーバーエラーが発生しました' });
    } finally {
      this.saving.set(false);
    }
  }

  handleCancel() {
    this.router.navigate(['/users']);
  }

  private validate(data: UserFormData): ValidationErrors {
    const errors: ValidationErrors = {};

    if (!data.name || data.name.trim().length === 0) {
      errors['name'] = '名前は必須です';
    }

    if (!data.email || !this.isValidEmail(data.email)) {
      errors['email'] = '有効なメールアドレスを入力してください';
    }

    return errors;
  }

  private isValidEmail(email: string): boolean {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  }
}
```

### 複数サービスの統合
```typescript
@Component({
  selector: 'app-order-container',
  template: `
    <app-order-view
      [order]="order()"
      [customer]="customer()"
      [products]="products()"
      [loading]="loading()"
      (updateStatus)="handleStatusUpdate($event)"
    />
  `
})
export class OrderContainerComponent {
  private orderService = inject(OrderService);
  private customerService = inject(CustomerService);
  private productService = inject(ProductService);
  private notificationService = inject(NotificationService);

  order = signal<Order | null>(null);
  customer = signal<Customer | null>(null);
  products = signal<Product[]>([]);
  loading = signal(false);

  async ngOnInit() {
    await this.loadOrderData();
  }

  private async loadOrderData() {
    this.loading.set(true);

    try {
      const orderId = this.route.snapshot.params['id'];

      // 並行データ取得
      const [order, customer, products] = await Promise.all([
        this.orderService.getOrder(orderId),
        this.customerService.getCustomer(orderId),
        this.productService.getProductsByOrder(orderId)
      ]);

      this.order.set(order);
      this.customer.set(customer);
      this.products.set(products);
    } catch (error) {
      this.notificationService.error('データの読み込みに失敗しました');
    } finally {
      this.loading.set(false);
    }
  }

  async handleStatusUpdate(newStatus: OrderStatus) {
    const currentOrder = this.order();
    if (!currentOrder) return;

    try {
      await this.orderService.updateStatus(currentOrder.id, newStatus);
      this.order.update(order => ({ ...order!, status: newStatus }));
      this.notificationService.success('ステータスを更新しました');
    } catch (error) {
      this.notificationService.error('更新に失敗しました');
    }
  }
}
```

### リアルタイム更新
```typescript
@Component({
  selector: 'app-chat-container'
})
export class ChatContainerComponent implements OnInit, OnDestroy {
  private chatService = inject(ChatService);
  private destroyRef = inject(DestroyRef);

  messages = signal<Message[]>([]);
  onlineUsers = signal<User[]>([]);

  ngOnInit() {
    // リアルタイムメッセージ購読
    this.chatService.messages$
      .pipe(takeUntilDestroyed(this.destroyRef))
      .subscribe(message => {
        this.messages.update(msgs => [...msgs, message]);
      });

    // オンラインユーザー監視
    this.chatService.onlineUsers$
      .pipe(takeUntilDestroyed(this.destroyRef))
      .subscribe(users => {
        this.onlineUsers.set(users);
      });
  }

  sendMessage(text: string) {
    const message: Message = {
      id: crypto.randomUUID(),
      text,
      timestamp: new Date(),
      userId: this.currentUserId
    };

    this.chatService.send(message);
  }

  deleteMessage(messageId: string) {
    this.chatService.delete(messageId);
    this.messages.update(msgs => msgs.filter(m => m.id !== messageId));
  }
}
```

### エラーハンドリング
```typescript
@Component({
  selector: 'app-data-container'
})
export class DataContainerComponent {
  private dataService = inject(DataService);
  private errorHandler = inject(ErrorHandlingService);

  data = signal<Data | null>(null);
  error = signal<string | null>(null);
  loading = signal(false);

  async loadData() {
    this.loading.set(true);
    this.error.set(null);

    try {
      const result = await this.dataService.fetch();
      this.data.set(result);
    } catch (err) {
      const errorMessage = this.errorHandler.handle(err);
      this.error.set(errorMessage);
      this.logError(err);
    } finally {
      this.loading.set(false);
    }
  }

  retry() {
    this.loadData();
  }

  private logError(error: unknown) {
    console.error('Data loading error:', error);
    // アナリティクスに送信
    this.analytics.trackError('data_load_error', error);
  }
}
```

## ベストプラクティス

### 責任の明確化
```typescript
// ✅ Smart: ロジックのみ担当
@Component({
  selector: 'app-user-container',
  template: `<app-user-list [users]="users()" />`
})
export class UserContainerComponent {
  private service = inject(UserService);
  users = signal<User[]>([]);
}

// ❌ Smart と Dumb の混在
@Component({
  template: `
    <div class="user-list">  <!-- 表示ロジックが混在 -->
      @for (user of users(); track user.id) {
        <div>{{ user.name }}</div>
      }
    </div>
  `
})
```

### サービスの注入
```typescript
// ✅ コンストラクタまたは inject()
export class SmartComponent {
  private service = inject(MyService);
  // または
  constructor(private service: MyService) {}
}

// ❌ Dumb Component でのサービス注入
export class DumbComponent {
  private service = inject(MyService); // 避けるべき
}
```

### 状態の管理
```typescript
// ✅ Signal による状態管理
users = signal<User[]>([]);
loading = signal(false);

// ✅ computed での派生状態
activeUsers = computed(() =>
  this.users().filter(u => u.active)
);
```

## 注意点

### 過度な肥大化
Smart Componentが大きくなりすぎた場合、複数のSmartコンポーネントに分割するか、サービスにロジックを移動してください。

### テストの複雑さ
サービス依存が多いため、テスト時にはモックの準備が必要です。依存性注入を活用してテスタビリティを確保してください。

### パフォーマンス
複雑な計算は`computed()`を使って最適化し、不要な再計算を避けてください。

### エラー処理
すべての非同期処理に適切なエラーハンドリングを実装してください。

## 関連技術
- **Dependency Injection**: 依存性注入
- **Signal**: 状態管理
- **Service**: ビジネスロジック層
- **RxJS**: リアクティブプログラミング
- **Container/Presentational Pattern**: アーキテクチャパターン
