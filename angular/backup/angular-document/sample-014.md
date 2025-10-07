# #014 「Standalone vs Module-based 比較」

## 概要
Angular v20ではStandalone Componentが推奨されます。従来のModule-based アプローチとの違いを理解し、適切な選択をしましょう。

## 学習目標
- StandaloneとModule-basedの違いを理解する
- それぞれのメリット・デメリットを把握する
- マイグレーション方法を学ぶ

## 技術ポイント
- **Standalone**: NgModule不要、依存関係が明確
- **Module-based**: 従来の方式、NgModuleで管理
- **v20推奨**: Standalone Component

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
// Standalone Component（v20推奨）
@Component({
  selector: 'app-user',
  standalone: true,
  imports: [CommonModule],  // 直接import
  template: '<p>{{name}}</p>'
})
export class UserComponent {
  name = 'John';
}
```

```typescript
// Module-based Component（従来）
@Component({
  selector: 'app-user',
  template: '<p>{{name}}</p>'
})
export class UserComponent {
  name = 'John';
}

@NgModule({
  declarations: [UserComponent],
  imports: [CommonModule],
  exports: [UserComponent]
})
export class UserModule {}
```

```typescript
// 使用方法の違い
// Standalone: 直接import
imports: [UserComponent]

// Module-based: モジュールをimport
imports: [UserModule]
```

## 💻 詳細実装例（学習用）

### 基本的な比較

#### Standalone Component
```typescript
// user.component.ts（Standalone）
import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-user',
  standalone: true,
  imports: [CommonModule],  // 必要なものを直接宣言
  template: `
    <div *ngIf="user">
      <h2>{{user.name}}</h2>
      <p>{{user.email}}</p>
    </div>
  `
})
export class UserComponent {
  user = {
    name: 'John Doe',
    email: 'john@example.com'
  };
}

// 使用側
import { UserComponent } from './user.component';

@Component({
  imports: [UserComponent]  // 直接import
})
export class AppComponent {}
```

#### Module-based Component
```typescript
// user.component.ts（Module-based）
import { Component } from '@angular/core';

@Component({
  selector: 'app-user',
  template: `
    <div *ngIf="user">
      <h2>{{user.name}}</h2>
      <p>{{user.email}}</p>
    </div>
  `
})
export class UserComponent {
  user = {
    name: 'John Doe',
    email: 'john@example.com'
  };
}

// user.module.ts
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { UserComponent } from './user.component';

@NgModule({
  declarations: [UserComponent],  // Componentを宣言
  imports: [CommonModule],         // 依存モジュール
  exports: [UserComponent]         // 外部に公開
})
export class UserModule {}

// 使用側
import { UserModule } from './user/user.module';

@NgModule({
  imports: [UserModule]  // モジュールをimport
})
export class AppModule {}
```

### アプリケーション起動の違い

#### Standalone
```typescript
// main.ts（Standalone）
import { bootstrapApplication } from '@angular/platform-browser';
import { AppComponent } from './app/app.component';
import { provideRouter } from '@angular/router';
import { provideHttpClient } from '@angular/common/http';
import { routes } from './app/app.routes';

bootstrapApplication(AppComponent, {
  providers: [
    provideRouter(routes),
    provideHttpClient()
  ]
}).catch(err => console.error(err));
```

#### Module-based
```typescript
// main.ts（Module-based）
import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';
import { AppModule } from './app/app.module';

platformBrowserDynamic()
  .bootstrapModule(AppModule)
  .catch(err => console.error(err));

// app.module.ts
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { RouterModule } from '@angular/router';
import { AppComponent } from './app.component';
import { routes } from './app.routes';

@NgModule({
  declarations: [AppComponent],
  imports: [
    BrowserModule,
    HttpClientModule,
    RouterModule.forRoot(routes)
  ],
  bootstrap: [AppComponent]
})
export class AppModule {}
```

### ルーティングの違い

#### Standalone
```typescript
// app.routes.ts（Standalone）
import { Routes } from '@angular/router';

export const routes: Routes = [
  {
    path: 'home',
    loadComponent: () =>
      import('./home/home.component').then(m => m.HomeComponent)
  },
  {
    path: 'users',
    loadComponent: () =>
      import('./users/user-list.component').then(m => m.UserListComponent)
  }
];

// app.component.ts
@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, RouterLink],
  template: `
    <nav>
      <a routerLink="/home">Home</a>
      <a routerLink="/users">Users</a>
    </nav>
    <router-outlet></router-outlet>
  `
})
export class AppComponent {}
```

#### Module-based
```typescript
// app-routing.module.ts（Module-based）
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path: 'home',
    loadChildren: () =>
      import('./home/home.module').then(m => m.HomeModule)
  },
  {
    path: 'users',
    loadChildren: () =>
      import('./users/users.module').then(m => m.UsersModule)
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}

// home.module.ts
@NgModule({
  declarations: [HomeComponent],
  imports: [
    CommonModule,
    RouterModule.forChild([
      { path: '', component: HomeComponent }
    ])
  ]
})
export class HomeModule {}
```

### 依存関係の管理

#### Standalone
```typescript
// 明示的で分かりやすい
@Component({
  selector: 'app-product-list',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    ProductCardComponent,  // 他のStandalone Component
    SearchPipe             // Standalone Pipe
  ],
  template: `...`
})
export class ProductListComponent {}
```

#### Module-based
```typescript
// モジュールにまとめて管理
@NgModule({
  declarations: [
    ProductListComponent,
    ProductCardComponent,
    SearchPipe
  ],
  imports: [
    CommonModule,
    FormsModule
  ],
  exports: [ProductListComponent]
})
export class ProductModule {}
```

### サービス提供の違い

#### Standalone
```typescript
// グローバルサービス
@Injectable({
  providedIn: 'root'
})
export class UserService {}

// Component専用サービス
@Component({
  selector: 'app-user-detail',
  standalone: true,
  providers: [UserDetailService],  // Component レベル
  template: `...`
})
export class UserDetailComponent {}

// アプリケーションレベル（main.ts）
bootstrapApplication(AppComponent, {
  providers: [
    provideHttpClient(),
    { provide: API_URL, useValue: 'https://api.example.com' }
  ]
});
```

#### Module-based
```typescript
// モジュールで提供
@NgModule({
  providers: [UserService]  // モジュールレベル
})
export class UserModule {}

// アプリケーションレベル
@NgModule({
  providers: [
    { provide: API_URL, useValue: 'https://api.example.com' }
  ]
})
export class AppModule {}

// Component専用
@Component({
  providers: [UserDetailService]
})
export class UserDetailComponent {}
```

### Lazy Loadingの違い

#### Standalone
```typescript
// シンプルなLazy Loading
export const routes: Routes = [
  {
    path: 'admin',
    loadComponent: () =>
      import('./admin/admin.component').then(m => m.AdminComponent)
  },
  {
    path: 'users',
    loadChildren: () =>
      import('./users/user.routes').then(m => m.USER_ROUTES)
  }
];
```

#### Module-based
```typescript
// モジュールベースのLazy Loading
const routes: Routes = [
  {
    path: 'admin',
    loadChildren: () =>
      import('./admin/admin.module').then(m => m.AdminModule)
  }
];

// admin.module.ts
@NgModule({
  declarations: [AdminComponent],
  imports: [
    CommonModule,
    RouterModule.forChild([
      { path: '', component: AdminComponent }
    ])
  ]
})
export class AdminModule {}
```

### テストの違い

#### Standalone
```typescript
// シンプルなテスト設定
describe('UserComponent', () => {
  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [UserComponent]  // importsで直接指定
    }).compileComponents();
  });

  it('should create', () => {
    const fixture = TestBed.createComponent(UserComponent);
    expect(fixture.componentInstance).toBeTruthy();
  });
});
```

#### Module-based
```typescript
// モジュールのインポートが必要
describe('UserComponent', () => {
  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [UserComponent],  // declarations
      imports: [CommonModule, FormsModule]
    }).compileComponents();
  });

  it('should create', () => {
    const fixture = TestBed.createComponent(UserComponent);
    expect(fixture.componentInstance).toBeTruthy();
  });
});
```

### 比較表

| 特徴 | Standalone | Module-based |
|------|-----------|--------------|
| **設定** | `standalone: true` | `@NgModule` |
| **依存関係** | `imports配列` | `declarations/imports/exports` |
| **ブートストラップ** | `bootstrapApplication()` | `bootstrapModule()` |
| **Lazy Loading** | `loadComponent()` | `loadChildren()` |
| **テスト** | `imports: [Component]` | `declarations: [Component]` |
| **複雑さ** | シンプル | やや複雑 |
| **学習曲線** | 緩やか | 急 |
| **推奨度（v20）** | ✅ 推奨 | ⚠️ レガシー |

### マイグレーション手順

#### Step 1: Componentをstandaloneに変換
```typescript
// Before
@Component({
  selector: 'app-user',
  templateUrl: './user.component.html'
})
export class UserComponent {}

// After
@Component({
  selector: 'app-user',
  standalone: true,
  imports: [CommonModule],  // 必要な依存を追加
  templateUrl: './user.component.html'
})
export class UserComponent {}
```

#### Step 2: NgModuleを削除
```typescript
// user.module.ts を削除
// または段階的に空にする

@NgModule({
  // declarations: [UserComponent],  // 削除
  imports: [CommonModule],
  // exports: [UserComponent]  // 削除
})
export class UserModule {}
```

#### Step 3: インポート方法を変更
```typescript
// Before
imports: [UserModule]

// After
imports: [UserComponent]
```

## ベストプラクティス

1. **新規プロジェクト**: Standaloneを使用
2. **既存プロジェクト**: 段階的にStandaloneへ移行
3. **依存関係の明示**: importsで明確に宣言
4. **CLIの活用**: `--standalone`フラグを使用

## 注意点

- Standaloneはv14以降で利用可能
- v20では Standaloneが推奨
- Module-basedも引き続きサポート
- 混在も可能だが統一を推奨

## 関連技術
- NgModule
- Standalone APIs
- Dependency Injection
- Angular Migration
