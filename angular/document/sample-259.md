# #259 「Component の責任分離」

## 概要
Componentの責任分離は、各コンポーネントが単一の明確な責任のみを持つように設計する原則です。データ取得、ビジネスロジック、表示、ユーザー操作などを適切に分離することで、保守性、テスタビリティ、再利用性が向上します。

## 学習目標
- 責任分離の原則と重要性を理解する
- 適切な責任の分割方法を習得する
- 実践的な分離パターンを学ぶ

## 技術ポイント
- **単一責任**: 一つのコンポーネントは一つの責任
- **疎結合**: コンポーネント間の依存を最小化
- **高凝集**: 関連する機能をまとめる

## 📺 画面表示用コード

### 責任の分離前（悪い例）
```typescript
// ❌ すべてが一つのコンポーネントに
@Component({
  selector: 'app-user-management',
  template: `
    <!-- データ取得、表示、編集、削除が混在 -->
    <div>
      <input [(ngModel)]="searchQuery">
      @for (user of filteredUsers(); track user.id) {
        <div>
          {{ user.name }}
          <button (click)="edit(user)">編集</button>
          <button (click)="delete(user.id)">削除</button>
        </div>
      }
      <!-- 編集フォームも同じコンポーネント内 -->
      @if (editingUser()) {
        <form (submit)="save()">
          <input [(ngModel)]="editingUser().name">
          <button type="submit">保存</button>
        </form>
      }
    </div>
  `
})
export class UserManagementComponent {
  // すべての責任が混在
  private service = inject(UserService);
  users = signal<User[]>([]);
  searchQuery = signal('');
  editingUser = signal<User | null>(null);

  filteredUsers = computed(/* ... */);
  async ngOnInit() { /* データ取得 */ }
  edit(user: User) { /* 編集処理 */ }
  async delete(id: string) { /* 削除処理 */ }
  async save() { /* 保存処理 */ }
}
```

### 責任の分離後（良い例）
```typescript
// ✅ Container: データ管理
@Component({
  selector: 'app-user-list-container',
  template: `
    <app-user-search
      [query]="searchQuery()"
      (queryChange)="handleSearchChange($event)"
    />
    <app-user-list
      [users]="filteredUsers()"
      (edit)="handleEdit($event)"
      (delete)="handleDelete($event)"
    />
    <app-user-edit-modal
      [user]="editingUser()"
      [isOpen]="isEditModalOpen()"
      (save)="handleSave($event)"
      (close)="closeEditModal()"
    />
  `
})
export class UserListContainerComponent {
  private userService = inject(UserService);

  users = signal<User[]>([]);
  searchQuery = signal('');
  editingUser = signal<User | null>(null);
  isEditModalOpen = signal(false);

  filteredUsers = computed(/* ... */);

  async ngOnInit() { /* データ取得のみ */ }
  handleSearchChange(query: string) { /* 検索処理 */ }
  handleEdit(user: User) { /* 編集開始 */ }
  async handleDelete(id: string) { /* 削除処理 */ }
  async handleSave(user: User) { /* 保存処理 */ }
  closeEditModal() { /* モーダル閉じる */ }
}

// ✅ Presentation: 検索UI
@Component({
  selector: 'app-user-search',
  template: `
    <input
      [value]="query()"
      (input)="queryChange.emit($any($event.target).value)"
      placeholder="検索...">
  `
})
export class UserSearchComponent {
  query = input('');
  queryChange = output<string>();
}

// ✅ Presentation: リスト表示
@Component({
  selector: 'app-user-list',
  template: `
    @for (user of users(); track user.id) {
      <app-user-item
        [user]="user"
        (edit)="edit.emit(user)"
        (delete)="delete.emit(user.id)"
      />
    }
  `
})
export class UserListComponent {
  users = input<User[]>([]);
  edit = output<User>();
  delete = output<string>();
}

// ✅ Presentation: アイテム表示
@Component({
  selector: 'app-user-item',
  template: `
    <div class="user-item">
      {{ user().name }}
      <button (click)="edit.emit()">編集</button>
      <button (click)="delete.emit()">削除</button>
    </div>
  `
})
export class UserItemComponent {
  user = input.required<User>();
  edit = output<void>();
  delete = output<void>();
}

// ✅ Feature: 編集モーダル
@Component({
  selector: 'app-user-edit-modal',
  template: `
    <app-modal [isOpen]="isOpen()" (close)="close.emit()">
      <app-user-form
        [user]="user()"
        (submit)="save.emit($event)"
      />
    </app-modal>
  `
})
export class UserEditModalComponent {
  user = input<User | null>(null);
  isOpen = input(false);
  save = output<User>();
  close = output<void>();
}
```

## 実践的な活用例

### Eコマース: 商品一覧の責任分離
```typescript
// Container: ビジネスロジック層
@Component({
  selector: 'app-product-page-container',
  template: `
    <app-product-filters
      [filters]="filters()"
      [categories]="categories()"
      (filterChange)="handleFilterChange($event)"
    />

    <app-product-grid
      [products]="filteredProducts()"
      [loading]="loading()"
      (addToCart)="handleAddToCart($event)"
      (viewDetails)="handleViewDetails($event)"
    />

    <app-pagination
      [currentPage]="currentPage()"
      [totalPages]="totalPages()"
      (pageChange)="handlePageChange($event)"
    />
  `
})
export class ProductPageContainerComponent {
  private productService = inject(ProductService);
  private cartService = inject(CartService);
  private router = inject(Router);

  // 状態管理のみ
  products = signal<Product[]>([]);
  filters = signal<ProductFilters>({});
  categories = signal<Category[]>([]);
  currentPage = signal(1);
  loading = signal(false);

  filteredProducts = computed(() => {
    return this.applyFilters(this.products(), this.filters());
  });

  totalPages = computed(() =>
    Math.ceil(this.filteredProducts().length / 12)
  );

  async ngOnInit() {
    await this.loadData();
  }

  private async loadData() {
    this.loading.set(true);
    const [products, categories] = await Promise.all([
      this.productService.getAll(),
      this.productService.getCategories()
    ]);
    this.products.set(products);
    this.categories.set(categories);
    this.loading.set(false);
  }

  handleFilterChange(filters: ProductFilters) {
    this.filters.set(filters);
    this.currentPage.set(1);
  }

  async handleAddToCart(product: Product) {
    await this.cartService.add(product);
  }

  handleViewDetails(product: Product) {
    this.router.navigate(['/products', product.id]);
  }

  handlePageChange(page: number) {
    this.currentPage.set(page);
  }

  private applyFilters(
    products: Product[],
    filters: ProductFilters
  ): Product[] {
    // フィルタリングロジック
    return products;
  }
}

// Presentation: フィルタUI
@Component({
  selector: 'app-product-filters',
  template: `
    <div class="filters">
      <select
        [value]="filters().category"
        (change)="updateCategory($any($event.target).value)">
        <option value="">すべてのカテゴリ</option>
        @for (cat of categories(); track cat.id) {
          <option [value]="cat.id">{{ cat.name }}</option>
        }
      </select>

      <input
        type="range"
        [min]="0"
        [max]="100000"
        [value]="filters().maxPrice"
        (input)="updatePrice($any($event.target).value)">
    </div>
  `,
  standalone: true
})
export class ProductFiltersComponent {
  filters = input.required<ProductFilters>();
  categories = input<Category[]>([]);
  filterChange = output<ProductFilters>();

  updateCategory(category: string) {
    this.filterChange.emit({ ...this.filters(), category });
  }

  updatePrice(price: string) {
    this.filterChange.emit({
      ...this.filters(),
      maxPrice: parseInt(price)
    });
  }
}

// Presentation: 商品グリッド
@Component({
  selector: 'app-product-grid',
  template: `
    @if (loading()) {
      <div class="loading">読み込み中...</div>
    } @else {
      <div class="grid">
        @for (product of products(); track product.id) {
          <app-product-card
            [product]="product"
            (addToCart)="addToCart.emit($event)"
            (viewDetails)="viewDetails.emit($event)"
          />
        }
      </div>
    }
  `,
  standalone: true,
  imports: [ProductCardComponent]
})
export class ProductGridComponent {
  products = input<Product[]>([]);
  loading = input(false);
  addToCart = output<Product>();
  viewDetails = output<Product>();
}

// Presentation: 商品カード
@Component({
  selector: 'app-product-card',
  template: `
    <div class="card" (click)="viewDetails.emit(product())">
      <img [src]="product().image" [alt]="product().name">
      <h3>{{ product().name }}</h3>
      <p class="price">¥{{ product().price.toLocaleString() }}</p>
      <button
        (click)="addToCart.emit(product()); $event.stopPropagation()">
        カートに追加
      </button>
    </div>
  `,
  standalone: true
})
export class ProductCardComponent {
  product = input.required<Product>();
  addToCart = output<Product>();
  viewDetails = output<Product>();
}
```

### ダッシュボード: 複数機能の責任分離
```typescript
// Container: 統合レイヤー
@Component({
  selector: 'app-dashboard-container',
  template: `
    <div class="dashboard">
      <app-stats-section-container />
      <app-activity-feed-container />
      <app-chart-section-container />
      <app-quick-actions-container />
    </div>
  `
})
export class DashboardContainerComponent {}

// Container: 統計セクション
@Component({
  selector: 'app-stats-section-container',
  template: `
    <app-stats-section
      [stats]="stats()"
      [loading]="loading()"
      (refresh)="loadStats()"
    />
  `
})
export class StatsSectionContainerComponent {
  private statsService = inject(StatsService);

  stats = signal<DashboardStats | null>(null);
  loading = signal(false);

  ngOnInit() {
    this.loadStats();
  }

  async loadStats() {
    this.loading.set(true);
    this.stats.set(await this.statsService.getStats());
    this.loading.set(false);
  }
}

// Presentation: 統計表示
@Component({
  selector: 'app-stats-section',
  template: `
    <div class="stats">
      @if (loading()) {
        <div>読み込み中...</div>
      } @else if (stats()) {
        <app-stat-card
          [label]="'総売上'"
          [value]="stats()!.totalSales"
          [trend]="stats()!.salesTrend"
        />
        <app-stat-card
          [label]="'新規顧客'"
          [value]="stats()!.newCustomers"
          [trend]="stats()!.customerTrend"
        />
      }
      <button (click)="refresh.emit()">更新</button>
    </div>
  `,
  imports: [StatCardComponent]
})
export class StatsSectionComponent {
  stats = input<DashboardStats | null>(null);
  loading = input(false);
  refresh = output<void>();
}

// Presentation: 統計カード
@Component({
  selector: 'app-stat-card',
  template: `
    <div class="stat-card">
      <p class="label">{{ label() }}</p>
      <p class="value">{{ formatValue(value()) }}</p>
      <p [class]="getTrendClass(trend())">
        {{ formatTrend(trend()) }}
      </p>
    </div>
  `
})
export class StatCardComponent {
  label = input.required<string>();
  value = input.required<number>();
  trend = input<number>(0);

  formatValue(value: number): string {
    return value.toLocaleString();
  }

  formatTrend(trend: number): string {
    return `${trend > 0 ? '+' : ''}${trend}%`;
  }

  getTrendClass(trend: number): string {
    return trend > 0 ? 'positive' : trend < 0 ? 'negative' : 'neutral';
  }
}
```

### フォーム: 入力検証の責任分離
```typescript
// Container: フォームロジック
@Component({
  selector: 'app-registration-form-container',
  template: `
    <app-registration-form
      [formData]="formData()"
      [errors]="errors()"
      [submitting]="submitting()"
      (submit)="handleSubmit($event)"
      (fieldChange)="handleFieldChange($event)"
    />
  `
})
export class RegistrationFormContainerComponent {
  private authService = inject(AuthService);
  private validator = inject(ValidationService);

  formData = signal<RegistrationData>({
    email: '',
    password: '',
    confirmPassword: ''
  });

  errors = signal<ValidationErrors>({});
  submitting = signal(false);

  handleFieldChange(change: { field: string; value: string }) {
    this.formData.update(data => ({
      ...data,
      [change.field]: change.value
    }));

    // リアルタイムバリデーション
    const fieldErrors = this.validator.validateField(
      change.field,
      change.value,
      this.formData()
    );

    this.errors.update(errors => ({
      ...errors,
      [change.field]: fieldErrors
    }));
  }

  async handleSubmit(data: RegistrationData) {
    // 全体バリデーション
    const validationErrors = this.validator.validate(data);
    if (Object.keys(validationErrors).length > 0) {
      this.errors.set(validationErrors);
      return;
    }

    // 送信処理
    this.submitting.set(true);
    try {
      await this.authService.register(data);
    } catch (err) {
      this.errors.set({ server: 'エラーが発生しました' });
    } finally {
      this.submitting.set(false);
    }
  }
}

// Presentation: フォームUI
@Component({
  selector: 'app-registration-form',
  template: `
    <form (ngSubmit)="submit.emit(formData())">
      <app-form-field
        [label]="'メールアドレス'"
        [value]="formData().email"
        [error]="errors().email"
        [type]="'email'"
        (valueChange)="emitChange('email', $event)"
      />

      <app-form-field
        [label]="'パスワード'"
        [value]="formData().password"
        [error]="errors().password"
        [type]="'password'"
        (valueChange)="emitChange('password', $event)"
      />

      <app-form-field
        [label]="'パスワード確認'"
        [value]="formData().confirmPassword"
        [error]="errors().confirmPassword"
        [type]="'password'"
        (valueChange)="emitChange('confirmPassword', $event)"
      />

      <button type="submit" [disabled]="submitting()">
        {{ submitting() ? '登録中...' : '登録' }}
      </button>
    </form>
  `,
  imports: [FormFieldComponent]
})
export class RegistrationFormComponent {
  formData = input.required<RegistrationData>();
  errors = input<ValidationErrors>({});
  submitting = input(false);

  submit = output<RegistrationData>();
  fieldChange = output<{ field: string; value: string }>();

  emitChange(field: string, value: string) {
    this.fieldChange.emit({ field, value });
  }
}

// Presentation: フォームフィールド
@Component({
  selector: 'app-form-field',
  template: `
    <div class="field">
      <label>{{ label() }}</label>
      <input
        [type]="type()"
        [value]="value()"
        (input)="valueChange.emit($any($event.target).value)">
      @if (error()) {
        <span class="error">{{ error() }}</span>
      }
    </div>
  `
})
export class FormFieldComponent {
  label = input.required<string>();
  value = input('');
  error = input<string>();
  type = input<'text' | 'email' | 'password'>('text');

  valueChange = output<string>();
}
```

## ベストプラクティス

### 単一責任の原則
```typescript
// ✅ 一つの責任に集中
@Component({
  selector: 'app-user-avatar',
  template: `<img [src]="imageUrl()" [alt]="name()">`
})
export class UserAvatarComponent {
  imageUrl = input.required<string>();
  name = input.required<string>();
}

// ❌ 複数の責任が混在
@Component({
  selector: 'app-user-profile',
  template: `
    <!-- アバター表示、編集、データ取得が混在 -->
  `
})
export class UserProfileComponent {
  // データ取得、表示、編集が全部入っている
}
```

### レイヤーの分離
```
Container Layer: データ取得、状態管理
  ↓
Presentation Layer: UI表示
  ↓
Component Layer: 再利用可能なパーツ
```

### 適切な粒度
```typescript
// ✅ 適切な粒度
app-product-list-container/      (Container)
  app-product-list/              (Presentation)
    app-product-card/            (Component)

// ❌ 過度な分割
app-product-name/                (小さすぎる)
app-product-price/               (小さすぎる)
```

## 注意点

### 過度な分離
すべてを細かく分ける必要はありません。機能の複雑さに応じて調整してください。

### パフォーマンス
コンポーネント数が増えると初期化コストがかかるため、バランスを考慮してください。

### コミュニケーション
親子間のデータ受け渡しが複雑になりすぎる場合は、状態管理サービスの利用を検討してください。

### ファイル構成
```
features/products/
  containers/
    product-list.container.ts
  components/
    product-list.component.ts
    product-card.component.ts
  services/
    product.service.ts
```

## 関連技術
- **Single Responsibility Principle**: 単一責任の原則
- **Smart/Dumb Pattern**: コンポーネント設計
- **Dependency Injection**: サービス注入
- **Component Architecture**: アーキテクチャ設計
- **Separation of Concerns**: 関心の分離
