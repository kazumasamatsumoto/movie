# #001 「Component とは？Angular の基本単位」

## 概要
Angular v20におけるComponentの基本概念を学びます。Componentはアプリケーションの基本構成要素で、UIを独立した再利用可能な部品として管理します。

## 学習目標
- Componentの役割を理解する
- @Componentデコレータの基本を習得する
- Componentの基本構造を理解する

## 技術ポイント
- **Component**: UIを独立した部品として管理
- **@Componentデコレータ**: Componentの定義
- **基本構成**: selector、template、styles

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
// 基本的なComponent
@Component({
  selector: 'app-hello',
  template: '<h1>Hello Angular!</h1>',
  styles: ['h1 { color: blue; }']
})
export class HelloComponent {}
```

```typescript
// Standalone Component（v20推奨）
@Component({
  selector: 'app-user',
  standalone: true,
  template: `<p>{{name}}</p>`
})
export class UserComponent {
  name = 'Angular Developer';
}
```

```typescript
// 3つの基本要素
@Component({
  selector: 'app-card',     // セレクタ
  template: '<div>{{title}}</div>',  // テンプレート
  styles: ['div { padding: 16px; }'] // スタイル
})
export class CardComponent {
  title = 'Card Title';
}
```

## 💻 詳細実装例（学習用）

### 完全なComponent例
```typescript
import { Component } from '@angular/core';

@Component({
  selector: 'app-user-profile',
  standalone: true,
  template: `
    <div class="profile-card">
      <h2>{{user.name}}</h2>
      <p>{{user.email}}</p>
      <p>Role: {{user.role}}</p>
    </div>
  `,
  styles: [`
    .profile-card {
      border: 1px solid #ccc;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    h2 {
      color: #333;
      margin-bottom: 8px;
    }
    p {
      color: #666;
      margin: 4px 0;
    }
  `]
})
export class UserProfileComponent {
  user = {
    name: '田中太郎',
    email: 'tanaka@example.com',
    role: 'Developer'
  };
}
```

### 再利用可能なComponent
```typescript
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-button',
  standalone: true,
  template: `
    <button [class]="variant" (click)="handleClick()">
      {{label}}
    </button>
  `,
  styles: [`
    button {
      padding: 8px 16px;
      border-radius: 4px;
      border: none;
      cursor: pointer;
    }
    .primary {
      background-color: #007bff;
      color: white;
    }
    .secondary {
      background-color: #6c757d;
      color: white;
    }
  `]
})
export class ButtonComponent {
  @Input() label = 'Click me';
  @Input() variant = 'primary';

  handleClick() {
    console.log('Button clicked!');
  }
}
```

### Componentの組み合わせ
```typescript
import { Component } from '@angular/core';
import { ButtonComponent } from './button.component';
import { UserProfileComponent } from './user-profile.component';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [ButtonComponent, UserProfileComponent],
  template: `
    <div class="dashboard">
      <h1>ダッシュボード</h1>
      <app-user-profile />
      <app-button label="保存" variant="primary" />
      <app-button label="キャンセル" variant="secondary" />
    </div>
  `,
  styles: [`
    .dashboard {
      max-width: 800px;
      margin: 0 auto;
      padding: 20px;
    }
  `]
})
export class DashboardComponent {}
```

## ベストプラクティス

1. **Standalone Componentを使用**: Angular v20ではstandaloneが推奨
2. **単一責任の原則**: 1つのComponentは1つの役割のみ
3. **再利用性を考慮**: 汎用的な部品として設計
4. **適切な命名**: 役割が明確な名前を付ける

## 注意点

- Componentは必ず@Componentデコレータが必要
- selectorはケバブケース（app-xxx）で命名
- Standalone Componentではimportsで依存関係を明示

## 関連技術
- Standalone APIs
- Component Lifecycle
- Dependency Injection
- Template Syntax
