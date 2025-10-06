# #255 「Container Component - ロジック層」

## 概要
Container Componentは、ビジネスロジック、データ取得、状態管理を担当するロジック層のコンポーネントです。Presentation Componentにデータを供給し、ユーザーアクションを処理することで、関心の分離を実現します。Smart Componentと同じ概念です。

## 学習目標
- Container Componentの責任範囲を理解する
- データフローの設計方法を習得する
- ロジック層の効果的な実装を学ぶ

## 技術ポイント
- **データ取得**: サービスからのデータ取得
- **状態管理**: Signal、RxJSによる状態制御
- **ロジック処理**: ビジネスルールの実装

## 📺 画面表示用コード

### 基本パターン
```typescript
@Component({
  selector: 'app-products-container',
  template: `
    <app-product-grid
      [products]="products()"
      [loading]="loading()"
      (productClick)="handleProductClick($event)"
    />
  `,
  standalone: true,
  imports: [ProductGridComponent]
})
export class ProductsContainerComponent {
  private productService = inject(ProductService);
  private router = inject(Router);

  products = signal<Product[]>([]);
  loading = signal(false);

  ngOnInit() {
    this.loadProducts();
  }

  async loadProducts() {
    this.loading.set(true);
    const data = await this.productService.getAll();
    this.products.set(data);
    this.loading.set(false);
  }

  handleProductClick(product: Product) {
    this.router.navigate(['/products', product.id]);
  }
}
```

### 複数サービス統合
```typescript
@Component({
  selector: 'app-user-dashboard-container',
  template: `
    <app-user-dashboard
      [user]="user()"
      [orders]="orders()"
      [stats]="stats()"
      [loading]="loading()"
      (refresh)="refresh()"
    />
  `
})
export class UserDashboardContainerComponent {
  private userService = inject(UserService);
  private orderService = inject(OrderService);
  private analyticsService = inject(AnalyticsService);

  user = signal<User | null>(null);
  orders = signal<Order[]>([]);
  stats = signal<UserStats | null>(null);
  loading = signal(false);

  async ngOnInit() {
    await this.loadData();
  }

  async loadData() {
    this.loading.set(true);

    const [user, orders, stats] = await Promise.all([
      this.userService.getCurrentUser(),
      this.orderService.getUserOrders(),
      this.analyticsService.getUserStats()
    ]);

    this.user.set(user);
    this.orders.set(orders);
    this.stats.set(stats);
    this.loading.set(false);
  }

  async refresh() {
    await this.loadData();
  }
}
```

### フィルタリングと検索
```typescript
@Component({
  selector: 'app-search-container',
  template: `
    <app-search-view
      [results]="filteredResults()"
      [query]="query()"
      [filters]="filters()"
      [loading]="loading()"
      (search)="handleSearch($event)"
      (filterChange)="handleFilterChange($event)"
    />
  `
})
export class SearchContainerComponent {
  private searchService = inject(SearchService);

  allResults = signal<SearchResult[]>([]);
  query = signal('');
  filters = signal<SearchFilters>({});
  loading = signal(false);

  filteredResults = computed(() => {
    return this.applyFilters(
      this.allResults(),
      this.filters()
    );
  });

  async handleSearch(query: string) {
    this.query.set(query);
    this.loading.set(true);

    const results = await this.searchService.search(query);
    this.allResults.set(results);
    this.loading.set(false);
  }

  handleFilterChange(filters: SearchFilters) {
    this.filters.set(filters);
  }

  private applyFilters(
    results: SearchResult[],
    filters: SearchFilters
  ): SearchResult[] {
    return results.filter(result => {
      if (filters.category && result.category !== filters.category) {
        return false;
      }
      if (filters.minPrice && result.price < filters.minPrice) {
        return false;
      }
      return true;
    });
  }
}
```

## 実践的な活用例

### CRUD操作の管理
```typescript
@Component({
  selector: 'app-task-list-container',
  template: `
    <app-task-list
      [tasks]="tasks()"
      [loading]="loading()"
      [error]="error()"
      (add)="handleAdd($event)"
      (update)="handleUpdate($event)"
      (delete)="handleDelete($event)"
      (toggleComplete)="handleToggle($event)"
    />
  `
})
export class TaskListContainerComponent {
  private taskService = inject(TaskService);
  private notification = inject(NotificationService);

  tasks = signal<Task[]>([]);
  loading = signal(false);
  error = signal<string | null>(null);

  ngOnInit() {
    this.loadTasks();
  }

  async loadTasks() {
    this.loading.set(true);
    this.error.set(null);

    try {
      const tasks = await this.taskService.getAll();
      this.tasks.set(tasks);
    } catch (err) {
      this.error.set('タスクの読み込みに失敗しました');
    } finally {
      this.loading.set(false);
    }
  }

  async handleAdd(taskData: CreateTaskDto) {
    try {
      const newTask = await this.taskService.create(taskData);
      this.tasks.update(tasks => [...tasks, newTask]);
      this.notification.success('タスクを追加しました');
    } catch (err) {
      this.notification.error('タスクの追加に失敗しました');
    }
  }

  async handleUpdate(task: Task) {
    try {
      await this.taskService.update(task.id, task);
      this.tasks.update(tasks =>
        tasks.map(t => t.id === task.id ? task : t)
      );
      this.notification.success('タスクを更新しました');
    } catch (err) {
      this.notification.error('タスクの更新に失敗しました');
    }
  }

  async handleDelete(taskId: string) {
    try {
      await this.taskService.delete(taskId);
      this.tasks.update(tasks =>
        tasks.filter(t => t.id !== taskId)
      );
      this.notification.success('タスクを削除しました');
    } catch (err) {
      this.notification.error('タスクの削除に失敗しました');
    }
  }

  async handleToggle(taskId: string) {
    const task = this.tasks().find(t => t.id === taskId);
    if (!task) return;

    const updated = { ...task, completed: !task.completed };
    await this.handleUpdate(updated);
  }
}
```

### ページネーション管理
```typescript
@Component({
  selector: 'app-paginated-list-container',
  template: `
    <app-paginated-list
      [items]="currentPageItems()"
      [currentPage]="currentPage()"
      [totalPages]="totalPages()"
      [pageSize]="pageSize()"
      [totalItems]="totalItems()"
      (pageChange)="handlePageChange($event)"
      (pageSizeChange)="handlePageSizeChange($event)"
    />
  `
})
export class PaginatedListContainerComponent {
  private dataService = inject(DataService);

  allItems = signal<Item[]>([]);
  currentPage = signal(1);
  pageSize = signal(10);
  loading = signal(false);

  totalItems = computed(() => this.allItems().length);

  totalPages = computed(() =>
    Math.ceil(this.totalItems() / this.pageSize())
  );

  currentPageItems = computed(() => {
    const start = (this.currentPage() - 1) * this.pageSize();
    const end = start + this.pageSize();
    return this.allItems().slice(start, end);
  });

  async ngOnInit() {
    await this.loadData();
  }

  async loadData() {
    this.loading.set(true);
    const items = await this.dataService.getAll();
    this.allItems.set(items);
    this.loading.set(false);
  }

  handlePageChange(page: number) {
    this.currentPage.set(page);
  }

  handlePageSizeChange(size: number) {
    this.pageSize.set(size);
    this.currentPage.set(1); // リセット
  }
}
```

### フォーム送信処理
```typescript
interface FormData {
  title: string;
  description: string;
  category: string;
  tags: string[];
}

@Component({
  selector: 'app-form-container',
  template: `
    <app-form-view
      [initialData]="formData()"
      [submitting]="submitting()"
      [errors]="errors()"
      [categories]="categories()"
      (submit)="handleSubmit($event)"
      (cancel)="handleCancel()"
    />
  `
})
export class FormContainerComponent {
  private formService = inject(FormService);
  private categoryService = inject(CategoryService);
  private router = inject(Router);
  private route = inject(ActivatedRoute);

  formData = signal<FormData | null>(null);
  categories = signal<Category[]>([]);
  submitting = signal(false);
  errors = signal<Record<string, string>>({});

  async ngOnInit() {
    // カテゴリ読み込み
    const categories = await this.categoryService.getAll();
    this.categories.set(categories);

    // 編集モードの場合、既存データを読み込み
    const id = this.route.snapshot.params['id'];
    if (id) {
      const data = await this.formService.getById(id);
      this.formData.set(data);
    }
  }

  async handleSubmit(data: FormData) {
    // バリデーション
    const validationErrors = this.validate(data);
    if (Object.keys(validationErrors).length > 0) {
      this.errors.set(validationErrors);
      return;
    }

    // 送信処理
    this.submitting.set(true);
    this.errors.set({});

    try {
      const id = this.route.snapshot.params['id'];
      if (id) {
        await this.formService.update(id, data);
      } else {
        await this.formService.create(data);
      }
      this.router.navigate(['/success']);
    } catch (err) {
      this.errors.set({ server: 'サーバーエラーが発生しました' });
    } finally {
      this.submitting.set(false);
    }
  }

  handleCancel() {
    this.router.navigate(['/list']);
  }

  private validate(data: FormData): Record<string, string> {
    const errors: Record<string, string> = {};

    if (!data.title || data.title.trim().length === 0) {
      errors['title'] = 'タイトルは必須です';
    }

    if (data.title && data.title.length > 100) {
      errors['title'] = 'タイトルは100文字以内です';
    }

    if (!data.category) {
      errors['category'] = 'カテゴリを選択してください';
    }

    return errors;
  }
}
```

### リアルタイムデータ同期
```typescript
@Component({
  selector: 'app-live-feed-container',
  template: `
    <app-live-feed
      [items]="items()"
      [connected]="connected()"
      [unreadCount]="unreadCount()"
      (markRead)="handleMarkRead($event)"
      (refresh)="handleRefresh()"
    />
  `
})
export class LiveFeedContainerComponent implements OnDestroy {
  private feedService = inject(FeedService);
  private destroyRef = inject(DestroyRef);

  items = signal<FeedItem[]>([]);
  connected = signal(false);
  unreadCount = signal(0);

  ngOnInit() {
    // WebSocket接続
    this.feedService.connect();

    // 接続状態監視
    this.feedService.connectionStatus$
      .pipe(takeUntilDestroyed(this.destroyRef))
      .subscribe(status => {
        this.connected.set(status === 'connected');
      });

    // リアルタイム更新
    this.feedService.items$
      .pipe(takeUntilDestroyed(this.destroyRef))
      .subscribe(items => {
        this.items.set(items);
        this.updateUnreadCount(items);
      });
  }

  handleMarkRead(itemId: string) {
    this.feedService.markAsRead(itemId);
    this.items.update(items =>
      items.map(item =>
        item.id === itemId ? { ...item, read: true } : item
      )
    );
    this.updateUnreadCount(this.items());
  }

  handleRefresh() {
    this.feedService.refresh();
  }

  private updateUnreadCount(items: FeedItem[]) {
    const count = items.filter(item => !item.read).length;
    this.unreadCount.set(count);
  }

  ngOnDestroy() {
    this.feedService.disconnect();
  }
}
```

### 複雑な状態管理
```typescript
@Component({
  selector: 'app-shopping-cart-container',
  template: `
    <app-shopping-cart
      [items]="cartItems()"
      [subtotal]="subtotal()"
      [tax]="tax()"
      [total]="total()"
      [discount]="discount()"
      [canCheckout]="canCheckout()"
      (updateQuantity)="handleUpdateQuantity($event)"
      (removeItem)="handleRemoveItem($event)"
      (applyCoupon)="handleApplyCoupon($event)"
      (checkout)="handleCheckout()"
    />
  `
})
export class ShoppingCartContainerComponent {
  private cartService = inject(CartService);
  private couponService = inject(CouponService);
  private checkoutService = inject(CheckoutService);
  private router = inject(Router);

  cartItems = signal<CartItem[]>([]);
  couponCode = signal<string | null>(null);
  discount = signal(0);

  subtotal = computed(() =>
    this.cartItems().reduce((sum, item) =>
      sum + item.price * item.quantity, 0
    )
  );

  tax = computed(() =>
    Math.floor(this.subtotal() * 0.1)
  );

  total = computed(() =>
    this.subtotal() + this.tax() - this.discount()
  );

  canCheckout = computed(() =>
    this.cartItems().length > 0 && this.total() > 0
  );

  async ngOnInit() {
    const items = await this.cartService.getItems();
    this.cartItems.set(items);
  }

  async handleUpdateQuantity(data: { id: string; quantity: number }) {
    await this.cartService.updateQuantity(data.id, data.quantity);
    this.cartItems.update(items =>
      items.map(item =>
        item.id === data.id
          ? { ...item, quantity: data.quantity }
          : item
      )
    );
  }

  async handleRemoveItem(itemId: string) {
    await this.cartService.removeItem(itemId);
    this.cartItems.update(items =>
      items.filter(item => item.id !== itemId)
    );
  }

  async handleApplyCoupon(code: string) {
    try {
      const discount = await this.couponService.apply(code);
      this.couponCode.set(code);
      this.discount.set(discount);
    } catch (err) {
      alert('クーポンコードが無効です');
    }
  }

  async handleCheckout() {
    if (!this.canCheckout()) return;

    const order = await this.checkoutService.createOrder({
      items: this.cartItems(),
      couponCode: this.couponCode(),
      total: this.total()
    });

    this.router.navigate(['/orders', order.id]);
  }
}
```

## ベストプラクティス

### ロジックの集中管理
```typescript
// ✅ Container でロジックを管理
export class ContainerComponent {
  private service = inject(MyService);

  data = signal([]);

  async loadData() {
    const result = await this.service.fetch();
    this.data.set(this.transform(result));
  }

  private transform(data: RawData[]): DisplayData[] {
    // データ変換ロジック
    return data.map(/* ... */);
  }
}

// ❌ Presentation にロジックを置かない
export class PresentationComponent {
  private service = inject(MyService); // 避ける
}
```

### エラーハンドリング
```typescript
// ✅ 適切なエラー処理
async loadData() {
  this.loading.set(true);
  this.error.set(null);

  try {
    const data = await this.service.fetch();
    this.data.set(data);
  } catch (err) {
    this.error.set(this.formatError(err));
  } finally {
    this.loading.set(false);
  }
}
```

### 状態の最適化
```typescript
// ✅ computed で派生状態
filteredItems = computed(() =>
  this.items().filter(item =>
    item.name.includes(this.searchQuery())
  )
);

// ❌ 毎回計算
get filteredItems() {
  return this.items.filter(/* ... */); // 非効率
}
```

## 注意点

### 責任の範囲
Container Componentは複雑になりがちです。肥大化した場合は複数のContainerに分割してください。

### テスト
サービス依存が多いため、適切なモックを用意してテストを行ってください。

### パフォーマンス
大量のデータ処理は`computed()`で最適化し、不要な再計算を避けてください。

### メモリリーク
Subscriptionは必ず`takeUntilDestroyed()`で解除してください。

## 関連技術
- **Smart Component**: 同様の概念
- **Dependency Injection**: サービス注入
- **Signal**: 状態管理
- **RxJS**: リアクティブプログラミング
- **Service Layer**: ビジネスロジック層
