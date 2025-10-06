# #261 「Component の粒度設計」

## 概要
Componentの粒度設計は、コンポーネントを適切なサイズに分割する技術です。小さすぎると管理コストが増大し、大きすぎると保守性が低下します。再利用性、テスト容易性、変更の影響範囲を考慮して、最適な粒度を見極めることが重要です。

## 学習目標
- 適切なコンポーネント粒度の判断基準を理解する
- 過度な分割と肥大化を避ける方法を習得する
- 実践的な粒度設計パターンを学ぶ

## 技術ポイント
- **バランス**: 小さすぎず大きすぎない設計
- **凝集度**: 関連機能をまとめる
- **結合度**: 依存を最小化

## 📺 画面表示用コード

### 粒度が細かすぎる例
```typescript
// ❌ 過度に細分化（管理コスト大）
@Component({
  selector: 'app-user-first-name',
  template: `<span>{{ firstName() }}</span>`
})
export class UserFirstNameComponent {
  firstName = input.required<string>();
}

@Component({
  selector: 'app-user-last-name',
  template: `<span>{{ lastName() }}</span>`
})
export class UserLastNameComponent {
  lastName = input.required<string>();
}

@Component({
  selector: 'app-user-email',
  template: `<span>{{ email() }}</span>`
})
export class UserEmailComponent {
  email = input.required<string>();
}

// 使用側: コンポーネントが多すぎる
@Component({
  template: `
    <app-user-first-name [firstName]="user.firstName" />
    <app-user-last-name [lastName]="user.lastName" />
    <app-user-email [email]="user.email" />
  `,
  imports: [UserFirstNameComponent, UserLastNameComponent, UserEmailComponent]
})
export class UserDisplayComponent {}
```

### 粒度が粗すぎる例
```typescript
// ❌ 肥大化しすぎ（保守性低下）
@Component({
  selector: 'app-user-management',
  template: `
    <!-- リスト表示 -->
    <div class="list">
      @for (user of users(); track user.id) {
        <div>{{ user.name }}</div>
      }
    </div>

    <!-- 詳細表示 -->
    <div class="detail">
      <h2>{{ selectedUser()?.name }}</h2>
      <p>{{ selectedUser()?.email }}</p>
    </div>

    <!-- 編集フォーム -->
    <form (submit)="save()">
      <input [(ngModel)]="editData.name">
      <input [(ngModel)]="editData.email">
      <button>保存</button>
    </form>

    <!-- 削除確認ダイアログ -->
    <div class="modal">
      <p>削除しますか?</p>
      <button (click)="confirmDelete()">はい</button>
    </div>
  `,
  imports: [FormsModule]
})
export class UserManagementComponent {
  // すべての機能が混在
  users = signal<User[]>([]);
  selectedUser = signal<User | null>(null);
  editData = { name: '', email: '' };

  async loadUsers() { /* ... */ }
  selectUser(user: User) { /* ... */ }
  async save() { /* ... */ }
  async confirmDelete() { /* ... */ }
}
```

### 適切な粒度の例
```typescript
// ✅ バランスの取れた粒度

// Atomic: 最小単位（再利用可能な部品）
@Component({
  selector: 'app-avatar',
  template: `
    <img
      [src]="imageUrl()"
      [alt]="name()"
      [style.width.px]="size()"
      [style.height.px]="size()"
      class="avatar">
  `,
  styles: [`
    .avatar {
      border-radius: 50%;
      object-fit: cover;
    }
  `],
  standalone: true
})
export class AvatarComponent {
  imageUrl = input.required<string>();
  name = input.required<string>();
  size = input(40);
}

// Molecular: 複数のAtomicを組み合わせ
@Component({
  selector: 'app-user-card',
  template: `
    <div class="user-card">
      <app-avatar
        [imageUrl]="user().avatar"
        [name]="user().name"
        [size]="48"
      />
      <div class="info">
        <h3>{{ user().name }}</h3>
        <p>{{ user().email }}</p>
      </div>
    </div>
  `,
  standalone: true,
  imports: [AvatarComponent]
})
export class UserCardComponent {
  user = input.required<User>();
}

// Organism: 複数のMolecularを組み合わせた機能単位
@Component({
  selector: 'app-user-list',
  template: `
    <div class="user-list">
      @for (user of users(); track user.id) {
        <app-user-card
          [user]="user"
          (click)="userClick.emit(user)"
        />
      }
    </div>
  `,
  standalone: true,
  imports: [UserCardComponent]
})
export class UserListComponent {
  users = input<User[]>([]);
  userClick = output<User>();
}

// Template: ページレベルの構成
@Component({
  selector: 'app-users-page',
  template: `
    <app-user-list
      [users]="users()"
      (userClick)="handleUserClick($event)"
    />
  `,
  imports: [UserListComponent]
})
export class UsersPageComponent {
  private userService = inject(UserService);
  users = signal<User[]>([]);

  async ngOnInit() {
    this.users.set(await this.userService.getAll());
  }

  handleUserClick(user: User) {
    console.log('Clicked:', user);
  }
}
```

## 実践的な活用例

### Atomic Design による粒度設計
```typescript
// Atoms: 最小の構成要素
@Component({
  selector: 'app-button',
  template: `
    <button
      [type]="type()"
      [disabled]="disabled()"
      [class]="'btn btn-' + variant()">
      <ng-content></ng-content>
    </button>
  `,
  styles: [`
    .btn { padding: 8px 16px; border-radius: 4px; }
    .btn-primary { background: #007bff; color: white; }
    .btn-secondary { background: #6c757d; color: white; }
  `],
  standalone: true
})
export class ButtonComponent {
  type = input<'button' | 'submit'>('button');
  disabled = input(false);
  variant = input<'primary' | 'secondary'>('primary');
}

@Component({
  selector: 'app-input',
  template: `
    <input
      [type]="type()"
      [placeholder]="placeholder()"
      [value]="value()"
      [disabled]="disabled()"
      (input)="valueChange.emit($any($event.target).value)">
  `,
  standalone: true
})
export class InputComponent {
  type = input<'text' | 'email' | 'password'>('text');
  placeholder = input('');
  value = input('');
  disabled = input(false);
  valueChange = output<string>();
}

// Molecules: Atomsの組み合わせ
@Component({
  selector: 'app-form-field',
  template: `
    <div class="form-field">
      <label>{{ label() }}</label>
      <app-input
        [type]="type()"
        [value]="value()"
        [placeholder]="placeholder()"
        (valueChange)="valueChange.emit($event)"
      />
      @if (error()) {
        <span class="error">{{ error() }}</span>
      }
    </div>
  `,
  standalone: true,
  imports: [InputComponent]
})
export class FormFieldComponent {
  label = input.required<string>();
  type = input<'text' | 'email' | 'password'>('text');
  value = input('');
  placeholder = input('');
  error = input<string>();
  valueChange = output<string>();
}

@Component({
  selector: 'app-search-box',
  template: `
    <div class="search-box">
      <app-input
        [value]="query()"
        [placeholder]="placeholder()"
        (valueChange)="queryChange.emit($event)"
      />
      <app-button (click)="search.emit()">
        検索
      </app-button>
    </div>
  `,
  standalone: true,
  imports: [InputComponent, ButtonComponent]
})
export class SearchBoxComponent {
  query = input('');
  placeholder = input('検索...');
  queryChange = output<string>();
  search = output<void>();
}

// Organisms: Moleculesの組み合わせ
@Component({
  selector: 'app-login-form',
  template: `
    <form (ngSubmit)="submit.emit(formData)" class="login-form">
      <h2>ログイン</h2>

      <app-form-field
        [label]="'メールアドレス'"
        [type]="'email'"
        [value]="formData.email"
        [error]="errors().email"
        (valueChange)="updateEmail($event)"
      />

      <app-form-field
        [label]="'パスワード'"
        [type]="'password'"
        [value]="formData.password"
        [error]="errors().password"
        (valueChange)="updatePassword($event)"
      />

      <app-button
        [type]="'submit'"
        [disabled]="submitting()">
        {{ submitting() ? 'ログイン中...' : 'ログイン' }}
      </app-button>
    </form>
  `,
  standalone: true,
  imports: [FormFieldComponent, ButtonComponent]
})
export class LoginFormComponent {
  errors = input<LoginErrors>({});
  submitting = input(false);
  submit = output<LoginData>();

  formData = { email: '', password: '' };

  updateEmail(email: string) {
    this.formData.email = email;
  }

  updatePassword(password: string) {
    this.formData.password = password;
  }
}

// Templates: ページ全体の構成
@Component({
  selector: 'app-login-page',
  template: `
    <div class="login-page">
      <app-login-form
        [errors]="errors()"
        [submitting]="submitting()"
        (submit)="handleLogin($event)"
      />
    </div>
  `,
  standalone: true,
  imports: [LoginFormComponent]
})
export class LoginPageComponent {
  private authService = inject(AuthService);
  private router = inject(Router);

  errors = signal<LoginErrors>({});
  submitting = signal(false);

  async handleLogin(data: LoginData) {
    this.submitting.set(true);
    this.errors.set({});

    try {
      await this.authService.login(data);
      this.router.navigate(['/dashboard']);
    } catch (err) {
      this.errors.set({ server: 'ログインに失敗しました' });
    } finally {
      this.submitting.set(false);
    }
  }
}
```

### 機能ベースの粒度設計
```typescript
// Feature: 商品カード（適切な粒度）
@Component({
  selector: 'app-product-card',
  template: `
    <article class="product-card">
      <img [src]="product().image" [alt]="product().name">
      <div class="content">
        <h3>{{ product().name }}</h3>
        <p class="price">¥{{ product().price.toLocaleString() }}</p>
        <p class="description">{{ product().description }}</p>

        @if (product().inStock) {
          <span class="badge in-stock">在庫あり</span>
        } @else {
          <span class="badge out-of-stock">在庫なし</span>
        }

        <button
          (click)="addToCart.emit(product())"
          [disabled]="!product().inStock">
          カートに追加
        </button>
      </div>
    </article>
  `,
  standalone: true
})
export class ProductCardComponent {
  product = input.required<Product>();
  addToCart = output<Product>();
}
// 粒度判断: 商品カードとして完結した機能単位
// - 再利用可能: ◯ (様々な場所で使える)
// - テスト容易: ◯ (単体でテスト可能)
// - 適切なサイズ: ◯ (小さすぎず大きすぎない)

// Feature: 商品グリッド
@Component({
  selector: 'app-product-grid',
  template: `
    <div class="product-grid">
      @if (loading()) {
        <div class="loading">読み込み中...</div>
      } @else if (products().length === 0) {
        <div class="empty">商品がありません</div>
      } @else {
        @for (product of products(); track product.id) {
          <app-product-card
            [product]="product"
            (addToCart)="addToCart.emit($event)"
          />
        }
      }
    </div>
  `,
  standalone: true,
  imports: [ProductCardComponent]
})
export class ProductGridComponent {
  products = input<Product[]>([]);
  loading = input(false);
  addToCart = output<Product>();
}
// 粒度判断: 商品一覧表示の責任を持つ
// - ProductCardより一段階上のレベル
// - グリッドレイアウトとローディング状態を管理

// Page: 商品ページ
@Component({
  selector: 'app-products-page',
  template: `
    <div class="products-page">
      <h1>商品一覧</h1>

      <app-search-box
        [query]="searchQuery()"
        (queryChange)="handleSearchChange($event)"
        (search)="performSearch()"
      />

      <app-product-grid
        [products]="filteredProducts()"
        [loading]="loading()"
        (addToCart)="handleAddToCart($event)"
      />

      <app-pagination
        [currentPage]="currentPage()"
        [totalPages]="totalPages()"
        (pageChange)="handlePageChange($event)"
      />
    </div>
  `,
  standalone: true,
  imports: [SearchBoxComponent, ProductGridComponent, PaginationComponent]
})
export class ProductsPageComponent {
  private productService = inject(ProductService);
  private cartService = inject(CartService);

  products = signal<Product[]>([]);
  searchQuery = signal('');
  currentPage = signal(1);
  loading = signal(false);

  filteredProducts = computed(() => {
    // フィルタリングロジック
    return this.products();
  });

  totalPages = computed(() => Math.ceil(this.products().length / 12));

  async ngOnInit() {
    await this.loadProducts();
  }

  async loadProducts() {
    this.loading.set(true);
    this.products.set(await this.productService.getAll());
    this.loading.set(false);
  }

  handleSearchChange(query: string) {
    this.searchQuery.set(query);
  }

  async performSearch() {
    await this.loadProducts();
  }

  async handleAddToCart(product: Product) {
    await this.cartService.add(product);
  }

  handlePageChange(page: number) {
    this.currentPage.set(page);
  }
}
// 粒度判断: ページ全体の統合
// - 複数のOrganismを組み合わせる
// - ビジネスロジックと状態管理を担当
```

### 粒度判断のチェックリスト
```typescript
// 粒度が適切かチェックする質問

// 1. 再利用性
// Q: このコンポーネントは他の場所で使えるか?
// ✅ Yes → 適切な粒度の可能性が高い
// ❌ No → 特定の場所に依存しすぎている可能性

@Component({
  selector: 'app-status-badge',  // ✅ 汎用的
  template: `<span [class]="status()">{{ label() }}</span>`
})
export class StatusBadgeComponent {
  status = input.required<string>();
  label = input.required<string>();
}

// 2. テスト容易性
// Q: このコンポーネント単体でテストできるか?
// ✅ Yes → 適切な粒度
// ❌ No → 依存が多すぎる可能性

// 3. 変更頻度
// Q: このコンポーネントは頻繁に変更されるか?
// ✅ 適度 → 適切な粒度
// ❌ 高頻度 → 責任が多すぎる可能性
// ❌ ほぼない → 細かすぎる可能性

// 4. サイズ
// Q: コンポーネントのコード量は適切か?
// ✅ 50-200行程度 → 適切な粒度
// ❌ 10行未満 → 細かすぎる可能性
// ❌ 500行以上 → 大きすぎる可能性

// 5. 責任の数
// Q: このコンポーネントの責任はいくつか?
// ✅ 1つ → 適切な粒度
// ❌ 2つ以上 → 分割を検討

// 6. インポート数
// Q: 依存するコンポーネント/モジュールの数は?
// ✅ 3-7個程度 → 適切な粒度
// ❌ 1-2個 → 細かすぎる可能性
// ❌ 10個以上 → 大きすぎる可能性
```

## ベストプラクティス

### 段階的な粒度設計
```typescript
// Step 1: まず大きく作る
@Component({
  selector: 'app-user-profile',
  template: `
    <!-- すべてを一つに -->
    <div>
      <img [src]="user.avatar">
      <h2>{{ user.name }}</h2>
      <p>{{ user.email }}</p>
      <button (click)="edit()">編集</button>
    </div>
  `
})
export class UserProfileComponent {}

// Step 2: 再利用可能な部分を抽出
@Component({
  selector: 'app-avatar',
  template: `<img [src]="imageUrl()" [alt]="name()">`
})
export class AvatarComponent {
  imageUrl = input.required<string>();
  name = input.required<string>();
}

// Step 3: 機能単位で分割
@Component({
  selector: 'app-user-info',
  template: `
    <app-avatar [imageUrl]="user().avatar" [name]="user().name" />
    <h2>{{ user().name }}</h2>
    <p>{{ user().email }}</p>
  `,
  imports: [AvatarComponent]
})
export class UserInfoComponent {
  user = input.required<User>();
}
```

### 粒度の調整
```typescript
// 細かすぎる場合 → 統合
// Before
@Component({ selector: 'app-first-name' })
export class FirstNameComponent {}

@Component({ selector: 'app-last-name' })
export class LastNameComponent {}

// After
@Component({ selector: 'app-full-name' })
export class FullNameComponent {}

// 大きすぎる場合 → 分割
// Before
@Component({ selector: 'app-user-management' })
export class UserManagementComponent {
  // リスト、詳細、編集、削除が混在
}

// After
@Component({ selector: 'app-user-list' })
export class UserListComponent {}

@Component({ selector: 'app-user-detail' })
export class UserDetailComponent {}

@Component({ selector: 'app-user-edit' })
export class UserEditComponent {}
```

## 注意点

### コンテキストによる違い
プロジェクトの規模、チームの規模、要件の複雑さによって適切な粒度は異なります。

### パフォーマンスへの影響
細かく分割しすぎると初期化コストが増加します。バランスを考慮してください。

### 保守性とのトレードオフ
細かい粒度は再利用性が高いですが、管理するコンポーネント数が増えます。

### 段階的なリファクタリング
最初から完璧な粒度を目指す必要はありません。必要に応じて調整してください。

## 関連技術
- **Atomic Design**: コンポーネント設計手法
- **Single Responsibility Principle**: 単一責任の原則
- **Component Architecture**: アーキテクチャ設計
- **Modular Design**: モジュラー設計
- **Composition Pattern**: 合成パターン
