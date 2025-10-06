# #260 「Single Responsibility Principle」

## 概要
Single Responsibility Principle (SRP) は、一つのコンポーネントは一つの責任だけを持つべきという設計原則です。「変更理由は一つだけ」という考え方に基づき、各コンポーネントが明確で限定的な役割を持つことで、保守性と再利用性が向上します。

## 学習目標
- SRPの原則と重要性を理解する
- 責任の範囲を適切に判断する方法を習得する
- SRPを適用した設計パターンを学ぶ

## 技術ポイント
- **単一責任**: 一つの変更理由のみ
- **凝集度**: 関連機能を一箇所に
- **疎結合**: 他への依存を最小化

## 📺 画面表示用コード

### SRP違反の例
```typescript
// ❌ 複数の責任を持つコンポーネント
@Component({
  selector: 'app-user-profile',
  template: `
    <!-- データ取得、表示、編集、検証が全て混在 -->
    <div>
      <img [src]="user()?.avatar">
      <input [(ngModel)]="editName">
      <button (click)="save()">保存</button>
    </div>
  `
})
export class UserProfileComponent {
  private userService = inject(UserService);  // データ取得
  private validator = inject(ValidatorService); // 検証

  user = signal<User | null>(null);
  editName = signal('');

  // 責任1: データ取得
  async ngOnInit() {
    this.user.set(await this.userService.getUser());
  }

  // 責任2: バリデーション
  validate(): boolean {
    return this.validator.validateName(this.editName());
  }

  // 責任3: 保存処理
  async save() {
    if (!this.validate()) return;
    await this.userService.update({ name: this.editName() });
  }

  // 責任4: 表示フォーマット
  formatDate(date: Date): string {
    return date.toLocaleDateString();
  }
}
// 変更理由が複数: データ構造変更、表示変更、検証ルール変更、保存ロジック変更
```

### SRPを適用した例
```typescript
// ✅ Container: データ管理のみ
@Component({
  selector: 'app-user-profile-container',
  template: `
    <app-user-display [user]="user()" />
    <app-user-edit-form
      [user]="user()"
      (save)="handleSave($event)"
    />
  `
})
export class UserProfileContainerComponent {
  private userService = inject(UserService);
  user = signal<User | null>(null);

  async ngOnInit() {
    this.user.set(await this.userService.getUser());
  }

  async handleSave(data: UserUpdateData) {
    await this.userService.update(data);
    this.user.set(await this.userService.getUser());
  }
}
// 変更理由: データ取得・更新ロジックの変更のみ

// ✅ Presentation: 表示のみ
@Component({
  selector: 'app-user-display',
  template: `
    <div class="profile">
      <app-avatar [imageUrl]="user().avatar" />
      <h2>{{ user().name }}</h2>
      <p>{{ formatDate(user().joinedAt) }}</p>
    </div>
  `,
  imports: [AvatarComponent]
})
export class UserDisplayComponent {
  user = input.required<User>();

  formatDate(date: Date): string {
    return new Date(date).toLocaleDateString();
  }
}
// 変更理由: 表示レイアウトの変更のみ

// ✅ Feature: フォーム編集のみ
@Component({
  selector: 'app-user-edit-form',
  template: `
    <form (ngSubmit)="handleSubmit()">
      <app-validated-input
        [(value)]="formData.name"
        [validator]="nameValidator"
      />
      <button type="submit">保存</button>
    </form>
  `,
  imports: [ValidatedInputComponent]
})
export class UserEditFormComponent {
  user = input.required<User>();
  save = output<UserUpdateData>();

  formData = { name: '' };

  ngOnInit() {
    this.formData.name = this.user().name;
  }

  handleSubmit() {
    this.save.emit(this.formData);
  }

  nameValidator = (value: string) => value.length > 0;
}
// 変更理由: フォームのUI・検証ルールの変更のみ
```

### 責任判断の基準
```typescript
// 質問: このコンポーネントを変更する理由は何か？

// ❌ 複数の理由がある場合は分割
@Component({
  selector: 'app-dashboard'
})
export class DashboardComponent {
  // 理由1: 統計データの計算ロジック変更
  // 理由2: グラフの表示方法変更
  // 理由3: データ取得API変更
  // → 3つの責任があるため分割すべき
}

// ✅ 単一の理由のみ
@Component({
  selector: 'app-stats-calculator'
})
export class StatsCalculatorComponent {
  // 理由: 統計データの計算ロジック変更のみ
}

@Component({
  selector: 'app-chart-display'
})
export class ChartDisplayComponent {
  // 理由: グラフの表示方法変更のみ
}

@Component({
  selector: 'app-dashboard-container'
})
export class DashboardContainerComponent {
  // 理由: データ取得ロジック変更のみ
}
```

## 実践的な活用例

### ログイン機能のSRP適用
```typescript
// ❌ SRP違反: すべてが一つに
@Component({
  selector: 'app-login',
  template: `
    <form (ngSubmit)="login()">
      <input [(ngModel)]="email" type="email">
      <input [(ngModel)]="password" type="password">
      <button>ログイン</button>
    </form>
  `
})
export class LoginComponent {
  private authService = inject(AuthService);
  email = signal('');
  password = signal('');

  // UI表示、検証、認証、ナビゲーションが混在
  async login() {
    // 検証
    if (!this.validateEmail(this.email())) return;
    if (!this.validatePassword(this.password())) return;

    // 認証
    try {
      await this.authService.login(this.email(), this.password());
      // ナビゲーション
      this.router.navigate(['/dashboard']);
    } catch (err) {
      // エラー処理
      this.showError(err);
    }
  }

  validateEmail(email: string): boolean { /* ... */ }
  validatePassword(password: string): boolean { /* ... */ }
  showError(err: any): void { /* ... */ }
}

// ✅ SRP適用: 責任を分離
// Container: 認証フロー制御
@Component({
  selector: 'app-login-container',
  template: `
    <app-login-form
      [errors]="errors()"
      [loading]="loading()"
      (submit)="handleLogin($event)"
    />
  `
})
export class LoginContainerComponent {
  private authService = inject(AuthService);
  private router = inject(Router);

  errors = signal<LoginErrors>({});
  loading = signal(false);

  async handleLogin(credentials: LoginCredentials) {
    this.loading.set(true);
    this.errors.set({});

    try {
      await this.authService.login(credentials);
      this.router.navigate(['/dashboard']);
    } catch (err) {
      this.errors.set({ server: 'ログインに失敗しました' });
    } finally {
      this.loading.set(false);
    }
  }
}
// 変更理由: 認証フローの変更のみ

// Presentation: フォームUI
@Component({
  selector: 'app-login-form',
  template: `
    <form (ngSubmit)="handleSubmit()">
      <app-email-input
        [(value)]="formData.email"
        [error]="errors().email"
      />
      <app-password-input
        [(value)]="formData.password"
        [error]="errors().password"
      />
      <button type="submit" [disabled]="loading()">
        {{ loading() ? 'ログイン中...' : 'ログイン' }}
      </button>
    </form>
  `,
  imports: [EmailInputComponent, PasswordInputComponent]
})
export class LoginFormComponent {
  errors = input<LoginErrors>({});
  loading = input(false);
  submit = output<LoginCredentials>();

  formData = { email: '', password: '' };

  handleSubmit() {
    this.submit.emit(this.formData);
  }
}
// 変更理由: フォームのレイアウト変更のみ

// Component: メール入力（検証付き）
@Component({
  selector: 'app-email-input',
  template: `
    <div class="field">
      <input
        type="email"
        [value]="value()"
        (input)="handleInput($any($event.target).value)">
      @if (validationError()) {
        <span class="error">{{ validationError() }}</span>
      }
      @if (error()) {
        <span class="error">{{ error() }}</span>
      }
    </div>
  `
})
export class EmailInputComponent {
  value = model('');
  error = input<string>();

  validationError = computed(() => {
    const val = this.value();
    if (!val) return '必須項目です';
    if (!this.isValidEmail(val)) return '有効なメールアドレスを入力してください';
    return null;
  });

  handleInput(val: string) {
    this.value.set(val);
  }

  private isValidEmail(email: string): boolean {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  }
}
// 変更理由: メール検証ルールの変更のみ
```

### ショッピングカートのSRP適用
```typescript
// Container: カート管理ロジック
@Component({
  selector: 'app-cart-container',
  template: `
    <app-cart-summary
      [itemCount]="itemCount()"
      [subtotal]="subtotal()"
      [tax]="tax()"
      [total]="total()"
    />
    <app-cart-items
      [items]="items()"
      (updateQuantity)="handleUpdateQuantity($event)"
      (remove)="handleRemove($event)"
    />
    <app-cart-actions
      [canCheckout]="canCheckout()"
      (checkout)="handleCheckout()"
    />
  `
})
export class CartContainerComponent {
  private cartService = inject(CartService);

  items = signal<CartItem[]>([]);

  itemCount = computed(() =>
    this.items().reduce((sum, item) => sum + item.quantity, 0)
  );

  subtotal = computed(() =>
    this.items().reduce((sum, item) => sum + item.price * item.quantity, 0)
  );

  tax = computed(() => Math.floor(this.subtotal() * 0.1));

  total = computed(() => this.subtotal() + this.tax());

  canCheckout = computed(() => this.items().length > 0);

  async handleUpdateQuantity(data: { id: string; quantity: number }) {
    await this.cartService.updateQuantity(data.id, data.quantity);
    await this.reload();
  }

  async handleRemove(id: string) {
    await this.cartService.remove(id);
    await this.reload();
  }

  async handleCheckout() {
    await this.cartService.checkout();
  }

  private async reload() {
    this.items.set(await this.cartService.getItems());
  }
}
// 変更理由: カート操作ロジックの変更のみ

// Presentation: サマリー表示
@Component({
  selector: 'app-cart-summary',
  template: `
    <div class="summary">
      <p>商品数: {{ itemCount() }}点</p>
      <p>小計: {{ formatPrice(subtotal()) }}</p>
      <p>消費税: {{ formatPrice(tax()) }}</p>
      <p class="total">合計: {{ formatPrice(total()) }}</p>
    </div>
  `
})
export class CartSummaryComponent {
  itemCount = input.required<number>();
  subtotal = input.required<number>();
  tax = input.required<number>();
  total = input.required<number>();

  formatPrice(price: number): string {
    return `¥${price.toLocaleString()}`;
  }
}
// 変更理由: サマリーの表示形式変更のみ

// Presentation: アイテム一覧
@Component({
  selector: 'app-cart-items',
  template: `
    @for (item of items(); track item.id) {
      <app-cart-item
        [item]="item"
        (updateQuantity)="updateQuantity.emit($event)"
        (remove)="remove.emit(item.id)"
      />
    }
  `,
  imports: [CartItemComponent]
})
export class CartItemsComponent {
  items = input<CartItem[]>([]);
  updateQuantity = output<{ id: string; quantity: number }>();
  remove = output<string>();
}
// 変更理由: アイテム一覧のレイアウト変更のみ

// Component: 個別アイテム表示
@Component({
  selector: 'app-cart-item',
  template: `
    <div class="item">
      <img [src]="item().image" [alt]="item().name">
      <div class="details">
        <h3>{{ item().name }}</h3>
        <p>{{ formatPrice(item().price) }}</p>
      </div>
      <app-quantity-selector
        [quantity]="item().quantity"
        (quantityChange)="handleQuantityChange($event)"
      />
      <button (click)="remove.emit()">削除</button>
    </div>
  `,
  imports: [QuantitySelectorComponent]
})
export class CartItemComponent {
  item = input.required<CartItem>();
  updateQuantity = output<{ id: string; quantity: number }>();
  remove = output<void>();

  formatPrice(price: number): string {
    return `¥${price.toLocaleString()}`;
  }

  handleQuantityChange(quantity: number) {
    this.updateQuantity.emit({ id: this.item().id, quantity });
  }
}
// 変更理由: アイテムカードの表示変更のみ

// Component: 数量セレクター
@Component({
  selector: 'app-quantity-selector',
  template: `
    <div class="quantity">
      <button (click)="decrement()">-</button>
      <span>{{ quantity() }}</span>
      <button (click)="increment()">+</button>
    </div>
  `
})
export class QuantitySelectorComponent {
  quantity = input.required<number>();
  quantityChange = output<number>();

  increment() {
    this.quantityChange.emit(this.quantity() + 1);
  }

  decrement() {
    if (this.quantity() > 1) {
      this.quantityChange.emit(this.quantity() - 1);
    }
  }
}
// 変更理由: 数量選択UIの変更のみ
```

### 検索機能のSRP適用
```typescript
// Container: 検索ロジック
@Component({
  selector: 'app-search-container',
  template: `
    <app-search-input
      [query]="query()"
      (queryChange)="handleQueryChange($event)"
    />
    <app-search-filters
      [filters]="filters()"
      (filterChange)="handleFilterChange($event)"
    />
    <app-search-results
      [results]="results()"
      [loading]="loading()"
      (itemClick)="handleItemClick($event)"
    />
  `
})
export class SearchContainerComponent {
  private searchService = inject(SearchService);
  private router = inject(Router);

  query = signal('');
  filters = signal<SearchFilters>({});
  results = signal<SearchResult[]>([]);
  loading = signal(false);

  async handleQueryChange(query: string) {
    this.query.set(query);
    await this.performSearch();
  }

  async handleFilterChange(filters: SearchFilters) {
    this.filters.set(filters);
    await this.performSearch();
  }

  private async performSearch() {
    if (this.query().length < 2) {
      this.results.set([]);
      return;
    }

    this.loading.set(true);
    const results = await this.searchService.search(
      this.query(),
      this.filters()
    );
    this.results.set(results);
    this.loading.set(false);
  }

  handleItemClick(item: SearchResult) {
    this.router.navigate(['/items', item.id]);
  }
}
// 変更理由: 検索ロジックの変更のみ

// Presentation: 検索入力
@Component({
  selector: 'app-search-input',
  template: `
    <input
      type="search"
      [value]="query()"
      (input)="queryChange.emit($any($event.target).value)"
      placeholder="検索...">
  `
})
export class SearchInputComponent {
  query = input('');
  queryChange = output<string>();
}
// 変更理由: 検索入力UIの変更のみ

// Presentation: フィルター
@Component({
  selector: 'app-search-filters',
  template: `
    <div class="filters">
      <select
        [value]="filters().category"
        (change)="updateCategory($any($event.target).value)">
        <option value="">すべて</option>
        <option value="books">書籍</option>
        <option value="electronics">電子機器</option>
      </select>
    </div>
  `
})
export class SearchFiltersComponent {
  filters = input.required<SearchFilters>();
  filterChange = output<SearchFilters>();

  updateCategory(category: string) {
    this.filterChange.emit({ ...this.filters(), category });
  }
}
// 変更理由: フィルターUIの変更のみ

// Presentation: 結果表示
@Component({
  selector: 'app-search-results',
  template: `
    @if (loading()) {
      <div>検索中...</div>
    } @else {
      @for (result of results(); track result.id) {
        <app-search-result-item
          [result]="result"
          (click)="itemClick.emit(result)"
        />
      }
    }
  `,
  imports: [SearchResultItemComponent]
})
export class SearchResultsComponent {
  results = input<SearchResult[]>([]);
  loading = input(false);
  itemClick = output<SearchResult>();
}
// 変更理由: 結果表示のレイアウト変更のみ
```

## ベストプラクティス

### 変更理由のチェック
```typescript
// 質問: このコンポーネントはなぜ変更されるか？
// - 答えが1つ → SRP準拠
// - 答えが複数 → 分割を検討

// ✅ 変更理由が1つ
@Component({ /* ... */ })
export class UserAvatarComponent {
  // 変更理由: アバター表示方法の変更
}

// ❌ 変更理由が複数
@Component({ /* ... */ })
export class UserComponent {
  // 変更理由1: データ取得方法の変更
  // 変更理由2: 表示レイアウトの変更
  // 変更理由3: バリデーションルールの変更
}
```

### 適切な抽象化レベル
```typescript
// ✅ 同じ抽象化レベル
@Component({ /* ... */ })
export class ProductListComponent {
  // すべて「商品リスト表示」に関する責任
  renderProducts() { }
  formatPrice() { }
  highlightDiscount() { }
}

// ❌ 異なる抽象化レベル
@Component({ /* ... */ })
export class ProductComponent {
  fetchFromAPI() { }      // 低レベル: データ取得
  displayProduct() { }    // 高レベル: 表示
  validateInput() { }     // 中レベル: 検証
}
```

## 注意点

### 過度な分割
SRPを厳密に適用しすぎると、コンポーネント数が爆発的に増えます。実用的なバランスを保ってください。

### コンテキストの理解
「責任」の定義はプロジェクトやチームによって異なります。チーム内で合意を形成してください。

### パフォーマンス
コンポーネントの分割はパフォーマンスに影響する場合があります。適切な粒度を見極めてください。

## 関連技術
- **SOLID Principles**: オブジェクト指向設計原則
- **Separation of Concerns**: 関心の分離
- **Component Architecture**: コンポーネント設計
- **Smart/Dumb Pattern**: 責任分離パターン
- **Modular Design**: モジュラー設計
