# #015 「imports 配列 - 依存関係の宣言」

## 概要
Standalone Componentのimports配列には、Componentが使用するすべての依存関係を宣言します。明示的な依存管理により、コードの可読性と保守性が向上します。

## 学習目標
- imports配列の役割を理解する
- 必要な依存関係の宣言方法を習得する
- よく使うモジュールとComponentを理解する

## 技術ポイント
- **imports配列**: 依存関係の明示的な宣言
- **モジュール**: CommonModule、FormsModuleなど
- **Component**: 他のStandalone Component

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
// 基本的なimports
@Component({
  selector: 'app-user',
  standalone: true,
  imports: [
    CommonModule,    // *ngIf, *ngFor等
    FormsModule      // ngModel
  ],
  template: '<input [(ngModel)]="name">'
})
export class UserComponent {
  name = '';
}
```

```typescript
// 他のComponentをimport
@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [
    HeaderComponent,  // Standalone Component
    FooterComponent   // Standalone Component
  ],
  template: '<app-header /><app-footer />'
})
export class DashboardComponent {}
```

```typescript
// 複数の依存関係
@Component({
  selector: 'app-product-list',
  standalone: true,
  imports: [
    CommonModule,
    ReactiveFormsModule,
    ProductCardComponent,
    SearchPipe
  ],
  template: '...'
})
export class ProductListComponent {}
```

## 💻 詳細実装例（学習用）

### 基本的なモジュールのimport

#### CommonModule
```typescript
import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-user-list',
  standalone: true,
  imports: [CommonModule],  // *ngIf, *ngFor, pipes等
  template: `
    <div>
      @if (users.length > 0) {
        <ul>
          @for (user of users; track user.id) {
            <li>{{user.name | uppercase}}</li>
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

#### FormsModule
```typescript
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [FormsModule],  // ngModel, ngForm等
  template: `
    <form #loginForm="ngForm" (ngSubmit)="onSubmit()">
      <input
        type="text"
        name="username"
        [(ngModel)]="credentials.username"
        required
      >
      <input
        type="password"
        name="password"
        [(ngModel)]="credentials.password"
        required
      >
      <button [disabled]="loginForm.invalid">Login</button>
    </form>
  `
})
export class LoginComponent {
  credentials = {
    username: '',
    password: ''
  };

  onSubmit() {
    console.log('Login:', this.credentials);
  }
}
```

#### ReactiveFormsModule
```typescript
import { Component } from '@angular/core';
import { ReactiveFormsModule, FormBuilder, Validators } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-signup',
  standalone: true,
  imports: [
    CommonModule,
    ReactiveFormsModule  // FormGroup, FormControl等
  ],
  template: `
    <form [formGroup]="signupForm" (ngSubmit)="onSubmit()">
      <input formControlName="email" type="email">
      <div *ngIf="signupForm.get('email')?.invalid && signupForm.get('email')?.touched">
        <span>Invalid email</span>
      </div>

      <input formControlName="password" type="password">
      <button [disabled]="signupForm.invalid">Sign Up</button>
    </form>
  `
})
export class SignupComponent {
  signupForm = this.fb.group({
    email: ['', [Validators.required, Validators.email]],
    password: ['', [Validators.required, Validators.minLength(8)]]
  });

  constructor(private fb: FormBuilder) {}

  onSubmit() {
    console.log('Signup:', this.signupForm.value);
  }
}
```

### Componentのimport

```typescript
// button.component.ts
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-button',
  standalone: true,
  template: `
    <button [class]="variant">
      <ng-content></ng-content>
    </button>
  `,
  styles: [`
    .primary { background: #007bff; color: white; }
    .secondary { background: #6c757d; color: white; }
  `]
})
export class ButtonComponent {
  @Input() variant = 'primary';
}

// card.component.ts
@Component({
  selector: 'app-card',
  standalone: true,
  template: `
    <div class="card">
      <ng-content></ng-content>
    </div>
  `
})
export class CardComponent {}

// user-profile.component.ts
import { Component } from '@angular/core';
import { ButtonComponent } from './button.component';
import { CardComponent } from './card.component';

@Component({
  selector: 'app-user-profile',
  standalone: true,
  imports: [
    ButtonComponent,  // 他のStandalone Component
    CardComponent
  ],
  template: `
    <app-card>
      <h2>User Profile</h2>
      <app-button variant="primary">Edit</app-button>
      <app-button variant="secondary">Delete</app-button>
    </app-card>
  `
})
export class UserProfileComponent {}
```

### RouterModuleのimport

```typescript
import { Component } from '@angular/core';
import { RouterOutlet, RouterLink, RouterLinkActive } from '@angular/router';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    RouterOutlet,      // <router-outlet>
    RouterLink,        // routerLink
    RouterLinkActive   // routerLinkActive
  ],
  template: `
    <nav>
      <a routerLink="/home" routerLinkActive="active">Home</a>
      <a routerLink="/users" routerLinkActive="active">Users</a>
      <a routerLink="/about" routerLinkActive="active">About</a>
    </nav>
    <router-outlet></router-outlet>
  `,
  styles: [`
    .active { font-weight: bold; color: #007bff; }
  `]
})
export class AppComponent {}
```

### PipeとDirectiveのimport

```typescript
// custom.pipe.ts
import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'reverse',
  standalone: true
})
export class ReversePipe implements PipeTransform {
  transform(value: string): string {
    return value.split('').reverse().join('');
  }
}

// highlight.directive.ts
import { Directive, ElementRef, HostListener } from '@angular/core';

@Directive({
  selector: '[appHighlight]',
  standalone: true
})
export class HighlightDirective {
  constructor(private el: ElementRef) {}

  @HostListener('mouseenter') onMouseEnter() {
    this.el.nativeElement.style.backgroundColor = 'yellow';
  }

  @HostListener('mouseleave') onMouseLeave() {
    this.el.nativeElement.style.backgroundColor = '';
  }
}

// component.ts
import { Component } from '@angular/core';
import { ReversePipe } from './reverse.pipe';
import { HighlightDirective } from './highlight.directive';

@Component({
  selector: 'app-demo',
  standalone: true,
  imports: [
    ReversePipe,         // カスタムPipe
    HighlightDirective   // カスタムDirective
  ],
  template: `
    <p appHighlight>{{ 'Hello' | reverse }}</p>
  `
})
export class DemoComponent {}
```

### Material UIのimport

```typescript
import { Component } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';

@Component({
  selector: 'app-material-demo',
  standalone: true,
  imports: [
    MatButtonModule,
    MatCardModule,
    MatInputModule,
    MatFormFieldModule
  ],
  template: `
    <mat-card>
      <mat-card-header>
        <mat-card-title>Material UI Demo</mat-card-title>
      </mat-card-header>
      <mat-card-content>
        <mat-form-field>
          <mat-label>Name</mat-label>
          <input matInput>
        </mat-form-field>
      </mat-card-content>
      <mat-card-actions>
        <button mat-raised-button color="primary">Submit</button>
      </mat-card-actions>
    </mat-card>
  `
})
export class MaterialDemoComponent {}
```

### 複数Componentの一括import

```typescript
// ui/index.ts（Barrel export）
export { ButtonComponent } from './button.component';
export { CardComponent } from './card.component';
export { ModalComponent } from './modal.component';

// app.component.ts
import { Component } from '@angular/core';
import {
  ButtonComponent,
  CardComponent,
  ModalComponent
} from './ui';  // Barrel exportから一括import

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    ButtonComponent,
    CardComponent,
    ModalComponent
  ],
  template: `...`
})
export class AppComponent {}
```

### 条件付きimport

```typescript
import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { environment } from '../environments/environment';

// 開発環境専用Component
const DevToolsComponent = environment.production
  ? null
  : await import('./dev-tools.component').then(m => m.DevToolsComponent);

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    CommonModule,
    ...(DevToolsComponent ? [DevToolsComponent] : [])
  ],
  template: `
    <div>
      <app-dev-tools *ngIf="!isProduction"></app-dev-tools>
      <!-- アプリケーション本体 -->
    </div>
  `
})
export class AppComponent {
  isProduction = environment.production;
}
```

### よく使うimportsパターン

#### 基本セット
```typescript
@Component({
  standalone: true,
  imports: [
    CommonModule,      // 基本ディレクティブ・パイプ
    FormsModule        // テンプレート駆動フォーム
  ]
})
```

#### フォームセット
```typescript
@Component({
  standalone: true,
  imports: [
    CommonModule,
    ReactiveFormsModule  // リアクティブフォーム
  ]
})
```

#### ルーティングセット
```typescript
@Component({
  standalone: true,
  imports: [
    RouterOutlet,
    RouterLink,
    RouterLinkActive
  ]
})
```

#### HTTP通信セット
```typescript
@Component({
  standalone: true,
  imports: [
    CommonModule,
    HttpClient  // DI経由で使用
  ]
})
// main.tsでprovideHttpClient()が必要
```

### エラーハンドリング

```typescript
// ❌ importsを忘れた場合
@Component({
  selector: 'app-bad',
  standalone: true,
  // imports: [CommonModule],  // 忘れた！
  template: `
    <div *ngIf="show">Hello</div>
    <!-- エラー: Can't bind to 'ngIf' since it isn't a known property -->
  `
})
export class BadComponent {
  show = true;
}

// ✅ 正しい実装
@Component({
  selector: 'app-good',
  standalone: true,
  imports: [CommonModule],  // 追加
  template: `
    <div *ngIf="show">Hello</div>
  `
})
export class GoodComponent {
  show = true;
}
```

### imports配列の整理

```typescript
import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterLink } from '@angular/router';

// カスタムComponent
import { HeaderComponent } from './header.component';
import { FooterComponent } from './footer.component';
import { SidebarComponent } from './sidebar.component';

// カスタムPipe/Directive
import { DateFormatPipe } from './pipes/date-format.pipe';
import { HighlightDirective } from './directives/highlight.directive';

@Component({
  selector: 'app-layout',
  standalone: true,
  imports: [
    // Angularモジュール
    CommonModule,
    FormsModule,
    RouterLink,

    // レイアウトComponent
    HeaderComponent,
    FooterComponent,
    SidebarComponent,

    // Pipe/Directive
    DateFormatPipe,
    HighlightDirective
  ],
  template: `...`
})
export class LayoutComponent {}
```

## ベストプラクティス

1. **必要なものだけimport**: 使わない依存は追加しない
2. **グループ化**: モジュール、Component、Pipeで分類
3. **Barrel exportの活用**: 関連Componentをまとめる
4. **エディタの補完活用**: 自動importを利用

## 注意点

- importsを忘れるとテンプレートエラー
- 循環参照に注意
- 大量のimportsはComponentが複雑すぎる兆候
- 使わないimportsは削除する

## 関連技術
- Dependency Injection
- Module System
- Tree Shaking
- Code Splitting
