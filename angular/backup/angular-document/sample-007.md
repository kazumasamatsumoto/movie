# #007 「styles - インラインスタイル」

## 概要
stylesプロパティを使用すると、TypeScriptファイル内に直接CSSを記述できます。Componentにスコープされたスタイルを定義します。

## 学習目標
- stylesプロパティの使い方を習得する
- スタイルのカプセル化を理解する
- インラインスタイルの適切な使用場面を学ぶ

## 技術ポイント
- **styles**: インラインCSS定義（配列形式）
- **スコープ**: Componentに限定されたスタイル
- **ViewEncapsulation**: スタイルのカプセル化方式

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
// 基本的なインラインスタイル
@Component({
  selector: 'app-button',
  template: '<button>Click me</button>',
  styles: ['button { background: blue; color: white; }']
})
export class ButtonComponent {}
```

```typescript
// 配列で複数のスタイル
@Component({
  selector: 'app-card',
  template: '<div class="card">{{title}}</div>',
  styles: [
    '.card { padding: 16px; }',
    '.card { border: 1px solid #ccc; }',
    '.card { border-radius: 8px; }'
  ]
})
export class CardComponent {
  title = 'Card';
}
```

```typescript
// バッククォートで複数行
@Component({
  selector: 'app-user',
  standalone: true,
  template: '<div class="user">{{name}}</div>',
  styles: [`
    .user {
      padding: 20px;
      background: #f0f0f0;
      border-radius: 4px;
    }
  `]
})
export class UserComponent {
  name = 'John';
}
```

## 💻 詳細実装例（学習用）

### スタイルのカプセル化
```typescript
import { Component } from '@angular/core';

// Componentスコープのスタイル（デフォルト）
@Component({
  selector: 'app-scoped-button',
  standalone: true,
  template: `
    <button class="primary">Primary</button>
    <button class="secondary">Secondary</button>
  `,
  styles: [`
    .primary {
      background-color: #007bff;
      color: white;
      border: none;
      padding: 10px 20px;
      border-radius: 4px;
      cursor: pointer;
    }

    .secondary {
      background-color: #6c757d;
      color: white;
      border: none;
      padding: 10px 20px;
      border-radius: 4px;
      cursor: pointer;
    }

    button:hover {
      opacity: 0.9;
    }
  `]
})
export class ScopedButtonComponent {}
```

### :host セレクタの使用
```typescript
import { Component } from '@angular/core';

@Component({
  selector: 'app-card',
  standalone: true,
  template: `
    <div class="card-content">
      <h3>{{title}}</h3>
      <p>{{content}}</p>
    </div>
  `,
  styles: [`
    /* Component自身にスタイルを適用 */
    :host {
      display: block;
      border: 1px solid #ddd;
      border-radius: 8px;
      padding: 16px;
      margin: 8px 0;
    }

    /* 条件付きスタイル */
    :host(.featured) {
      border-color: #007bff;
      background-color: #f0f8ff;
    }

    :host(.compact) {
      padding: 8px;
    }

    .card-content h3 {
      margin: 0 0 12px 0;
      color: #333;
    }

    .card-content p {
      margin: 0;
      color: #666;
    }
  `]
})
export class CardComponent {
  title = 'Card Title';
  content = 'Card content goes here';
}

// 使用例:
// <app-card class="featured"></app-card>
// <app-card class="compact"></app-card>
```

### :host-context セレクタ
```typescript
import { Component } from '@angular/core';

@Component({
  selector: 'app-theme-aware',
  standalone: true,
  template: `
    <div class="content">
      <p>This component adapts to parent theme</p>
    </div>
  `,
  styles: [`
    /* 親要素のクラスに応じてスタイルを変更 */
    :host-context(.dark-theme) .content {
      background-color: #333;
      color: white;
    }

    :host-context(.light-theme) .content {
      background-color: white;
      color: #333;
    }

    :host-context(.high-contrast) .content {
      border: 3px solid black;
      font-weight: bold;
    }

    .content {
      padding: 20px;
      border-radius: 4px;
    }
  `]
})
export class ThemeAwareComponent {}

// 使用例:
// <div class="dark-theme">
//   <app-theme-aware></app-theme-aware>
// </div>
```

### ::ng-deep（非推奨だが知っておくべき）
```typescript
import { Component } from '@angular/core';

@Component({
  selector: 'app-parent',
  standalone: true,
  template: `
    <div class="wrapper">
      <app-child></app-child>
    </div>
  `,
  styles: [`
    /* ⚠️ ::ng-deepは非推奨 */
    /* 子Componentのスタイルを強制的に変更 */
    ::ng-deep .child-element {
      color: red;
    }

    /* より良い方法: CSS変数を使用 */
    .wrapper {
      --child-color: blue;
      --child-padding: 16px;
    }
  `]
})
export class ParentComponent {}
```

### CSS変数を使ったテーマ対応
```typescript
import { Component } from '@angular/core';

@Component({
  selector: 'app-themed-button',
  standalone: true,
  template: `
    <button [class]="variant">
      {{label}}
    </button>
  `,
  styles: [`
    /* CSS変数の定義 */
    :host {
      --primary-color: #007bff;
      --secondary-color: #6c757d;
      --success-color: #28a745;
      --danger-color: #dc3545;
    }

    button {
      padding: 10px 20px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-weight: bold;
      transition: all 0.3s ease;
    }

    .primary {
      background-color: var(--primary-color);
      color: white;
    }

    .secondary {
      background-color: var(--secondary-color);
      color: white;
    }

    .success {
      background-color: var(--success-color);
      color: white;
    }

    .danger {
      background-color: var(--danger-color);
      color: white;
    }

    button:hover {
      opacity: 0.9;
      transform: translateY(-2px);
      box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
  `]
})
export class ThemedButtonComponent {
  label = 'Click me';
  variant: 'primary' | 'secondary' | 'success' | 'danger' = 'primary';
}
```

### レスポンシブデザイン
```typescript
import { Component } from '@angular/core';

@Component({
  selector: 'app-responsive-grid',
  standalone: true,
  template: `
    <div class="grid">
      <div class="grid-item" *ngFor="let item of items">
        {{item}}
      </div>
    </div>
  `,
  styles: [`
    .grid {
      display: grid;
      gap: 16px;
      padding: 16px;
    }

    /* デスクトップ: 3カラム */
    @media (min-width: 992px) {
      .grid {
        grid-template-columns: repeat(3, 1fr);
      }
    }

    /* タブレット: 2カラム */
    @media (min-width: 576px) and (max-width: 991px) {
      .grid {
        grid-template-columns: repeat(2, 1fr);
      }
    }

    /* モバイル: 1カラム */
    @media (max-width: 575px) {
      .grid {
        grid-template-columns: 1fr;
      }
    }

    .grid-item {
      background-color: #f0f0f0;
      padding: 20px;
      border-radius: 8px;
      text-align: center;
    }
  `]
})
export class ResponsiveGridComponent {
  items = ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5', 'Item 6'];
}
```

### アニメーションを含むスタイル
```typescript
import { Component } from '@angular/core';

@Component({
  selector: 'app-animated-card',
  standalone: true,
  template: `
    <div class="card" (mouseenter)="isHovered = true" (mouseleave)="isHovered = false">
      <div class="card-header" [class.expanded]="isHovered">
        <h3>{{title}}</h3>
      </div>
      <div class="card-body" [class.visible]="isHovered">
        <p>{{content}}</p>
      </div>
    </div>
  `,
  styles: [`
    .card {
      border: 1px solid #ddd;
      border-radius: 8px;
      overflow: hidden;
      transition: all 0.3s ease;
      cursor: pointer;
    }

    .card:hover {
      box-shadow: 0 8px 16px rgba(0,0,0,0.2);
      transform: translateY(-4px);
    }

    .card-header {
      background-color: #007bff;
      color: white;
      padding: 16px;
      transition: all 0.3s ease;
    }

    .card-header.expanded {
      padding: 24px;
      background-color: #0056b3;
    }

    .card-header h3 {
      margin: 0;
      transition: transform 0.3s ease;
    }

    .card-header.expanded h3 {
      transform: scale(1.1);
    }

    .card-body {
      padding: 0 16px;
      max-height: 0;
      opacity: 0;
      overflow: hidden;
      transition: all 0.3s ease;
    }

    .card-body.visible {
      padding: 16px;
      max-height: 200px;
      opacity: 1;
    }

    @keyframes fadeIn {
      from {
        opacity: 0;
        transform: translateY(-10px);
      }
      to {
        opacity: 1;
        transform: translateY(0);
      }
    }

    .card-body.visible p {
      animation: fadeIn 0.4s ease;
    }
  `]
})
export class AnimatedCardComponent {
  title = 'Hover Me';
  content = 'This content appears on hover with a smooth animation!';
  isHovered = false;
}
```

### Flexbox レイアウト
```typescript
import { Component } from '@angular/core';

@Component({
  selector: 'app-flex-layout',
  standalone: true,
  template: `
    <div class="container">
      <header class="header">Header</header>
      <main class="main">Main Content</main>
      <aside class="sidebar">Sidebar</aside>
      <footer class="footer">Footer</footer>
    </div>
  `,
  styles: [`
    :host {
      display: block;
      height: 100vh;
    }

    .container {
      display: flex;
      flex-direction: column;
      height: 100%;
    }

    .header {
      background-color: #007bff;
      color: white;
      padding: 20px;
      text-align: center;
    }

    .main {
      display: flex;
      flex: 1;
      overflow: hidden;
    }

    .main {
      flex: 1;
      padding: 20px;
      background-color: #f8f9fa;
    }

    .sidebar {
      width: 250px;
      padding: 20px;
      background-color: #e9ecef;
      overflow-y: auto;
    }

    .footer {
      background-color: #6c757d;
      color: white;
      padding: 20px;
      text-align: center;
    }

    @media (max-width: 768px) {
      .main {
        flex-direction: column;
      }

      .sidebar {
        width: 100%;
      }
    }
  `]
})
export class FlexLayoutComponent {}
```

## ベストプラクティス

1. **小規模スタイルにstylesを使用**: シンプルなComponentに最適
2. **:hostセレクタの活用**: Component自身のスタイリング
3. **CSS変数の使用**: テーマ対応とカスタマイズ性向上
4. **::ng-deepは避ける**: 非推奨、代わりにCSS変数を使用

## 注意点

- stylesは配列形式で指定
- デフォルトでComponentにスコープされる
- 長いスタイルはstyleUrlsで外部化を推奨
- ::ng-deepは将来削除される予定

## 関連技術
- ViewEncapsulation
- Shadow DOM
- CSS Scoping
- CSS Variables
