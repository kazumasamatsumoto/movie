# #013 「Standalone Component - standalone: true」

## 概要
Standalone ComponentはNgModuleなしで動作するComponentです。Angular v14で導入され、v20では標準的な方法となりました。

## 学習目標
- Standalone Componentの概念を理解する
- standalone: trueの使い方を習得する
- Standaloneのメリットを理解する

## 技術ポイント
- **standalone: true**: NgModule不要の設定
- **imports配列**: 直接依存関係を宣言
- **シンプルな構造**: モジュールレスアーキテクチャ

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
// Standalone Componentの基本
@Component({
  selector: 'app-user',
  standalone: true,  // これだけ！
  template: '<p>{{name}}</p>'
})
export class UserComponent {
  name = 'John';
}
```

```typescript
// 依存関係の直接宣言
@Component({
  selector: 'app-user-list',
  standalone: true,
  imports: [CommonModule],  // 必要なものを直接import
  template: '<div *ngFor="let user of users">{{user}}</div>'
})
export class UserListComponent {
  users = ['John', 'Jane'];
}
```

```typescript
// CLIでStandalone生成
// ng g c user --standalone
@Component({
  selector: 'app-user',
  standalone: true,
  imports: [],
  templateUrl: './user.component.html'
})
export class UserComponent {}
```

## 💻 詳細実装例（学習用）

### 基本的なStandalone Component
```typescript
import { Component } from '@angular/core';

// 最小限のStandalone Component
@Component({
  selector: 'app-hello',
  standalone: true,
  template: '<h1>Hello, Standalone!</h1>'
})
export class HelloComponent {}

// 使用方法
import { bootstrapApplication } from '@angular/platform-browser';
import { HelloComponent } from './app/hello.component';

// 直接ブートストラップ可能
bootstrapApplication(HelloComponent);
```

### CommonModuleのimport
```typescript
import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-user-list',
  standalone: true,
  imports: [CommonModule],  // *ngIf, *ngFor等を使用
  template: `
    <div>
      <h2>Users</h2>
      @if (users.length > 0) {
        <ul>
          @for (user of users; track user.id) {
            <li>{{user.name}}</li>
          }
        </ul>
      } @else {
        <p>No users found</p>
      }
    </div>
  `
})
export class UserListComponent {
  users = [
    { id: 1, name: 'John' },
    { id: 2, name: 'Jane' }
  ];
}
```

### FormsModuleの使用
```typescript
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-login-form',
  standalone: true,
  imports: [FormsModule],  // ngModelを使用
  template: `
    <form>
      <input
        type="text"
        [(ngModel)]="username"
        placeholder="Username"
      >
      <button (click)="login()">Login</button>
      <p>Username: {{username}}</p>
    </form>
  `
})
export class LoginFormComponent {
  username = '';

  login() {
    console.log('Logging in:', this.username);
  }
}
```

### 他のStandalone Componentをimport
```typescript
import { Component } from '@angular/core';

// 子Component
@Component({
  selector: 'app-button',
  standalone: true,
  template: `
    <button>
      <ng-content></ng-content>
    </button>
  `,
  styles: [`
    button {
      padding: 10px 20px;
      background: #007bff;
      color: white;
      border: none;
      border-radius: 4px;
    }
  `]
})
export class ButtonComponent {}

// 親Component
@Component({
  selector: 'app-user-profile',
  standalone: true,
  imports: [ButtonComponent],  // Standalone Componentを直接import
  template: `
    <div>
      <h2>User Profile</h2>
      <app-button>Edit Profile</app-button>
      <app-button>Delete Account</app-button>
    </div>
  `
})
export class UserProfileComponent {}
```

### RouterModuleとの組み合わせ
```typescript
import { Component } from '@angular/core';
import { RouterOutlet, RouterLink } from '@angular/router';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, RouterLink],  // ルーティング機能
  template: `
    <nav>
      <a routerLink="/home">Home</a>
      <a routerLink="/about">About</a>
    </nav>
    <router-outlet></router-outlet>
  `
})
export class AppComponent {}

// ルート設定
import { Routes } from '@angular/router';
import { HomeComponent } from './home.component';
import { AboutComponent } from './about.component';

export const routes: Routes = [
  { path: 'home', component: HomeComponent },
  { path: 'about', component: AboutComponent },
  { path: '', redirectTo: '/home', pathMatch: 'full' }
];

// main.ts
import { bootstrapApplication } from '@angular/platform-browser';
import { provideRouter } from '@angular/router';
import { AppComponent } from './app/app.component';
import { routes } from './app/app.routes';

bootstrapApplication(AppComponent, {
  providers: [
    provideRouter(routes)
  ]
});
```

### HttpClientの使用
```typescript
import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { CommonModule } from '@angular/common';

interface User {
  id: number;
  name: string;
  email: string;
}

@Component({
  selector: 'app-user-data',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div>
      <h2>User Data</h2>
      @if (loading) {
        <p>Loading...</p>
      } @else {
        <ul>
          @for (user of users; track user.id) {
            <li>{{user.name}} - {{user.email}}</li>
          }
        </ul>
      }
    </div>
  `
})
export class UserDataComponent implements OnInit {
  users: User[] = [];
  loading = true;

  constructor(private http: HttpClient) {}

  ngOnInit() {
    this.http.get<User[]>('https://api.example.com/users')
      .subscribe(data => {
        this.users = data;
        this.loading = false;
      });
  }
}

// main.ts で HttpClient を提供
import { provideHttpClient } from '@angular/common/http';

bootstrapApplication(AppComponent, {
  providers: [
    provideHttpClient()
  ]
});
```

### サービスの使用
```typescript
import { Injectable } from '@angular/core';

// Standalone Service
@Injectable({
  providedIn: 'root'  // アプリ全体で共有
})
export class UserService {
  private users = [
    { id: 1, name: 'John' },
    { id: 2, name: 'Jane' }
  ];

  getUsers() {
    return this.users;
  }

  addUser(name: string) {
    const newUser = {
      id: this.users.length + 1,
      name
    };
    this.users.push(newUser);
  }
}

// Component
import { Component } from '@angular/core';
import { UserService } from './user.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-user-manager',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div>
      <ul>
        @for (user of users; track user.id) {
          <li>{{user.name}}</li>
        }
      </ul>
      <button (click)="addUser()">Add User</button>
    </div>
  `
})
export class UserManagerComponent {
  users = this.userService.getUsers();

  constructor(private userService: UserService) {}

  addUser() {
    this.userService.addUser('New User');
    this.users = this.userService.getUsers();
  }
}
```

### Lazy Loadingとの組み合わせ
```typescript
// app.routes.ts
import { Routes } from '@angular/router';

export const routes: Routes = [
  {
    path: 'admin',
    loadComponent: () =>
      import('./admin/admin.component').then(m => m.AdminComponent)
  },
  {
    path: 'user',
    loadChildren: () =>
      import('./user/user.routes').then(m => m.USER_ROUTES)
  }
];

// admin.component.ts
@Component({
  selector: 'app-admin',
  standalone: true,
  template: '<h1>Admin Panel</h1>'
})
export class AdminComponent {}

// user/user.routes.ts
import { Routes } from '@angular/router';
import { UserListComponent } from './user-list.component';
import { UserDetailComponent } from './user-detail.component';

export const USER_ROUTES: Routes = [
  { path: 'list', component: UserListComponent },
  { path: 'detail/:id', component: UserDetailComponent }
];
```

### 環境変数の設定
```typescript
// main.ts
import { bootstrapApplication } from '@angular/platform-browser';
import { AppComponent } from './app/app.component';
import { provideRouter } from '@angular/router';
import { provideHttpClient } from '@angular/common/http';
import { routes } from './app/app.routes';

bootstrapApplication(AppComponent, {
  providers: [
    provideRouter(routes),
    provideHttpClient(),
    // その他のプロバイダー
    { provide: 'API_URL', useValue: 'https://api.example.com' }
  ]
}).catch(err => console.error(err));
```

### app.config.ts パターン
```typescript
// app.config.ts
import { ApplicationConfig } from '@angular/core';
import { provideRouter } from '@angular/router';
import { provideHttpClient } from '@angular/common/http';
import { provideAnimations } from '@angular/platform-browser/animations';
import { routes } from './app.routes';

export const appConfig: ApplicationConfig = {
  providers: [
    provideRouter(routes),
    provideHttpClient(),
    provideAnimations()
  ]
};

// main.ts
import { bootstrapApplication } from '@angular/platform-browser';
import { AppComponent } from './app/app.component';
import { appConfig } from './app/app.config';

bootstrapApplication(AppComponent, appConfig)
  .catch(err => console.error(err));
```

### テストの書き方
```typescript
// user.component.spec.ts
import { ComponentFixture, TestBed } from '@angular/core/testing';
import { UserComponent } from './user.component';

describe('UserComponent (Standalone)', () => {
  let component: UserComponent;
  let fixture: ComponentFixture<UserComponent>;

  beforeEach(async () => {
    // Standalone Componentはimportsで直接指定
    await TestBed.configureTestingModule({
      imports: [UserComponent]  // declarationsではなくimports
    }).compileComponents();

    fixture = TestBed.createComponent(UserComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should display user name', () => {
    component.name = 'Test User';
    fixture.detectChanges();
    const compiled = fixture.nativeElement;
    expect(compiled.textContent).toContain('Test User');
  });
});
```

### マイグレーション例
```typescript
// Before: Module-based
@NgModule({
  declarations: [UserComponent],
  imports: [CommonModule, FormsModule],
  exports: [UserComponent]
})
export class UserModule {}

@Component({
  selector: 'app-user',
  templateUrl: './user.component.html'
})
export class UserComponent {}

// After: Standalone
@Component({
  selector: 'app-user',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './user.component.html'
})
export class UserComponent {}
```

## ベストプラクティス

1. **v20ではStandaloneを使用**: 新しいプロジェクトは全てStandalone
2. **必要な依存関係のみimport**: 無駄な依存を避ける
3. **app.config.tsで設定管理**: プロバイダーを一元管理
4. **Lazy Loadingの活用**: パフォーマンス向上

## 注意点

- standalone: true を必ず指定
- 使用するモジュール/Componentをimportsに追加
- NgModuleのdeclarationsは使用しない
- テストでもimportsで指定

## 関連技術
- Standalone APIs
- Dependency Injection
- Module-less Architecture
- Tree Shaking
