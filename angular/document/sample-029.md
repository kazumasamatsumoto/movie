# #029 「Component のフォルダ構成戦略」台本

四国めたん「Component のフォルダ構成戦略について解説します！」
ずんだもん「フォルダ構成戦略って何？」
四国めたん「プロジェクトの規模と要件に応じて、Componentを効率的に整理する方法です」
ずんだもん「どんな戦略があるの？」
四国めたん「機能別、レイヤー別、共有別、マイクロフロントエンド別などがあります」
ずんだもん「どうやって選ぶの？」
四国めたん「プロジェクトの規模、チーム構成、開発期間、保守性を考慮して選択します」

---

## 📺 画面表示用コード

// 戦略1: 機能別構成（Feature-based）
```
src/app/
├── features/                    # 機能別モジュール
│   ├── user-management/         # ユーザー管理機能
│   │   ├── components/
│   │   │   ├── user-list/
│   │   │   ├── user-detail/
│   │   │   └── user-form/
│   │   ├── services/
│   │   │   └── user.service.ts
│   │   ├── models/
│   │   │   └── user.model.ts
│   │   └── user-management.module.ts
│   ├── product-catalog/         # 商品カタログ機能
│   │   ├── components/
│   │   │   ├── product-list/
│   │   │   ├── product-detail/
│   │   │   └── product-search/
│   │   ├── services/
│   │   │   └── product.service.ts
│   │   └── product-catalog.module.ts
│   └── order-management/        # 注文管理機能
│       ├── components/
│       │   ├── order-list/
│       │   ├── order-detail/
│       │   └── order-form/
│       └── order-management.module.ts
├── shared/                      # 共有リソース
│   ├── components/
│   │   ├── button/
│   │   ├── modal/
│   │   └── table/
│   ├── services/
│   │   ├── api.service.ts
│   │   └── auth.service.ts
│   └── shared.module.ts
└── core/                        # コア機能
    ├── services/
    ├── guards/
    └── interceptors/
```

// 機能別構成の例
```typescript
// features/user-management/components/user-list/user-list.component.ts
@Component({
  selector: 'app-user-list',
  standalone: true,
  template: `
    <div class="user-list">
      <h2>ユーザー一覧</h2>
      <div *ngFor="let user of users" class="user-item">
        <span>{{user.name}} - {{user.email}}</span>
        <button (click)="editUser(user)">編集</button>
      </div>
    </div>
  `,
  styles: [`
    .user-list {
      padding: 20px;
    }
    .user-item {
      display: flex;
      justify-content: space-between;
      padding: 10px;
      border: 1px solid #ddd;
      margin-bottom: 5px;
    }
  `]
})
export class UserListComponent {
  @Input() users: User[] = [];
  @Output() edit = new EventEmitter<User>();
  
  editUser(user: User) {
    this.edit.emit(user);
  }
}
```

// 戦略2: レイヤー別構成（Layer-based）
```
src/app/
├── presentation/                # プレゼンテーション層
│   ├── components/
│   │   ├── user/
│   │   │   ├── user-list/
│   │   │   ├── user-detail/
│   │   │   └── user-form/
│   │   ├── product/
│   │   │   ├── product-list/
│   │   │   └── product-detail/
│   │   └── shared/
│   │       ├── button/
│   │       └── modal/
│   └── pages/
│       ├── user-management/
│       ├── product-catalog/
│       └── dashboard/
├── business/                    # ビジネス層
│   ├── services/
│   │   ├── user.service.ts
│   │   ├── product.service.ts
│   │   └── order.service.ts
│   ├── models/
│   │   ├── user.model.ts
│   │   ├── product.model.ts
│   │   └── order.model.ts
│   └── validators/
│       ├── user.validator.ts
│       └── product.validator.ts
├── data/                        # データ層
│   ├── repositories/
│   │   ├── user.repository.ts
│   │   └── product.repository.ts
│   ├── api/
│   │   ├── user.api.ts
│   │   └── product.api.ts
│   └── mocks/
│       ├── user.mock.ts
│       └── product.mock.ts
└── core/                        # コア層
    ├── services/
    ├── guards/
    └── interceptors/
```

// レイヤー別構成の例
```typescript
// presentation/components/user/user-list/user-list.component.ts
@Component({
  selector: 'app-user-list',
  standalone: true,
  template: `
    <div class="user-list">
      <h2>ユーザー一覧</h2>
      <div *ngFor="let user of users" class="user-item">
        <span>{{user.name}} - {{user.email}}</span>
        <button (click)="editUser(user)">編集</button>
      </div>
    </div>
  `
})
export class UserListComponent {
  @Input() users: User[] = [];
  @Output() edit = new EventEmitter<User>();
  
  editUser(user: User) {
    this.edit.emit(user);
  }
}

// business/services/user.service.ts
@Injectable({
  providedIn: 'root'
})
export class UserService {
  constructor(private userRepository: UserRepository) {}
  
  getUsers(): Observable<User[]> {
    return this.userRepository.getAll();
  }
  
  createUser(user: User): Observable<User> {
    return this.userRepository.create(user);
  }
}

// data/repositories/user.repository.ts
@Injectable({
  providedIn: 'root'
})
export class UserRepository {
  constructor(private userApi: UserApi) {}
  
  getAll(): Observable<User[]> {
    return this.userApi.getUsers();
  }
  
  create(user: User): Observable<User> {
    return this.userApi.createUser(user);
  }
}
```

// 戦略3: 共有別構成（Shared-based）
```
src/app/
├── shared/                      # 共有リソース
│   ├── ui/                      # UI Component
│   │   ├── button/
│   │   ├── input/
│   │   ├── modal/
│   │   ├── table/
│   │   └── card/
│   ├── layout/                  # レイアウトComponent
│   │   ├── header/
│   │   ├── footer/
│   │   ├── sidebar/
│   │   └── navigation/
│   ├── forms/                   # フォームComponent
│   │   ├── user-form/
│   │   ├── product-form/
│   │   └── order-form/
│   ├── services/                # 共有サービス
│   │   ├── api.service.ts
│   │   ├── auth.service.ts
│   │   └── notification.service.ts
│   └── utils/                   # ユーティリティ
│       ├── validators/
│       ├── formatters/
│       └── helpers/
├── features/                    # 機能別Component
│   ├── user-management/
│   ├── product-catalog/
│   └── order-management/
└── pages/                       # ページComponent
    ├── dashboard/
    ├── user-management/
    └── product-catalog/
```

// 共有別構成の例
```typescript
// shared/ui/button/button.component.ts
@Component({
  selector: 'app-button',
  standalone: true,
  template: `
    <button 
      [class]="buttonClass"
      [disabled]="disabled"
      (click)="onClick.emit()">
      <ng-content></ng-content>
    </button>
  `,
  styles: [`
    button {
      padding: 8px 16px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    .btn-primary {
      background-color: #007bff;
      color: white;
    }
    .btn-secondary {
      background-color: #6c757d;
      color: white;
    }
  `]
})
export class ButtonComponent {
  @Input() buttonClass = 'btn-primary';
  @Input() disabled = false;
  @Output() onClick = new EventEmitter<void>();
}

// shared/layout/header/header.component.ts
@Component({
  selector: 'app-header',
  standalone: true,
  template: `
    <header class="header">
      <div class="logo">
        <h1>{{title}}</h1>
      </div>
      <nav class="navigation">
        <a routerLink="/dashboard">ダッシュボード</a>
        <a routerLink="/users">ユーザー管理</a>
        <a routerLink="/products">商品管理</a>
      </nav>
    </header>
  `,
  styles: [`
    .header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 1rem 2rem;
      background-color: #f8f9fa;
      border-bottom: 1px solid #dee2e6;
    }
    .logo h1 {
      margin: 0;
      color: #007bff;
    }
    .navigation a {
      margin-right: 1rem;
      text-decoration: none;
      color: #333;
    }
  `]
})
export class HeaderComponent {
  @Input() title = 'アプリケーション';
}
```

// 戦略4: マイクロフロントエンド別構成
```
src/
├── shell/                       # シェルアプリケーション
│   ├── app/
│   │   ├── components/
│   │   │   ├── header/
│   │   │   ├── footer/
│   │   │   └── navigation/
│   │   └── app.component.ts
│   └── shell.module.ts
├── user-management/             # ユーザー管理マイクロフロントエンド
│   ├── app/
│   │   ├── components/
│   │   │   ├── user-list/
│   │   │   ├── user-detail/
│   │   │   └── user-form/
│   │   └── user-management.module.ts
│   └── user-management.module.ts
├── product-catalog/             # 商品カタログマイクロフロントエンド
│   ├── app/
│   │   ├── components/
│   │   │   ├── product-list/
│   │   │   ├── product-detail/
│   │   │   └── product-search/
│   │   └── product-catalog.module.ts
│   └── product-catalog.module.ts
└── shared/                      # 共有ライブラリ
    ├── components/
    ├── services/
    └── models/
```

// マイクロフロントエンド別構成の例
```typescript
// user-management/app/components/user-list/user-list.component.ts
@Component({
  selector: 'app-user-list',
  standalone: true,
  template: `
    <div class="user-list">
      <h2>ユーザー一覧</h2>
      <div *ngFor="let user of users" class="user-item">
        <span>{{user.name}} - {{user.email}}</span>
        <button (click)="editUser(user)">編集</button>
      </div>
    </div>
  `
})
export class UserListComponent {
  @Input() users: User[] = [];
  @Output() edit = new EventEmitter<User>();
  
  editUser(user: User) {
    this.edit.emit(user);
  }
}

// shell/app/components/navigation/navigation.component.ts
@Component({
  selector: 'app-navigation',
  standalone: true,
  template: `
    <nav class="navigation">
      <a routerLink="/dashboard">ダッシュボード</a>
      <a routerLink="/user-management">ユーザー管理</a>
      <a routerLink="/product-catalog">商品カタログ</a>
    </nav>
  `
})
export class NavigationComponent {
  // シェルアプリケーションのナビゲーション
}
```

// フォルダ構成戦略の選択指針
```typescript
@Component({
  selector: 'app-folder-strategy-guide',
  standalone: true,
  template: `
    <div class="strategy-guide">
      <h2>フォルダ構成戦略の選択指針</h2>
      <div class="strategy-item">
        <h3>機能別構成</h3>
        <p><strong>適用場面:</strong> 中規模〜大規模プロジェクト</p>
        <p><strong>メリット:</strong> 機能の独立性、チーム開発に適している</p>
        <p><strong>デメリット:</strong> 共有リソースの管理が複雑</p>
      </div>
      <div class="strategy-item">
        <h3>レイヤー別構成</h3>
        <p><strong>適用場面:</strong> 大規模エンタープライズアプリケーション</p>
        <p><strong>メリット:</strong> 責任の分離、テスタビリティ</p>
        <p><strong>デメリット:</strong> 学習コストが高い</p>
      </div>
      <div class="strategy-item">
        <h3>共有別構成</h3>
        <p><strong>適用場面:</strong> 小規模〜中規模プロジェクト</p>
        <p><strong>メリット:</strong> 再利用性、保守性</p>
        <p><strong>デメリット:</strong> 機能の境界が曖昧</p>
      </div>
      <div class="strategy-item">
        <h3>マイクロフロントエンド別構成</h3>
        <p><strong>適用場面:</strong> 大規模分散開発</p>
        <p><strong>メリット:</strong> 独立性、スケーラビリティ</p>
        <p><strong>デメリット:</strong> 複雑性、運用コスト</p>
      </div>
    </div>
  `,
  styles: [`
    .strategy-guide {
      padding: 20px;
      max-width: 800px;
      margin: 0 auto;
    }
    .strategy-item {
      margin-bottom: 20px;
      padding: 15px;
      border: 1px solid #ddd;
      border-radius: 8px;
      background-color: #f8f9fa;
    }
    .strategy-item h3 {
      color: #007bff;
      margin-top: 0;
    }
  `]
})
export class FolderStrategyGuideComponent {
  // フォルダ構成戦略の選択指針を説明
}
```
