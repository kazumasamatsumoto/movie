# #008 「styleUrls - 外部スタイルファイル」

## 概要
styleUrlsを使用すると、CSSを外部ファイルに分離できます。複数のスタイルファイルを指定でき、SCSS/Sassもサポートされます。

## 学習目標
- styleUrlsの使い方を習得する
- 複数スタイルファイルの管理方法を学ぶ
- SCSS/Sassの設定方法を理解する

## 技術ポイント
- **styleUrls**: 外部CSSファイル参照（配列形式）
- **複数ファイル**: 複数のスタイルシートを組み合わせ可能
- **プリプロセッサ**: SCSS/Sass/Lessに対応

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
// 基本的なstyleUrls
@Component({
  selector: 'app-user',
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.css']
})
export class UserComponent {}
```

```typescript
// 複数のスタイルファイル
@Component({
  selector: 'app-dashboard',
  standalone: true,
  templateUrl: './dashboard.component.html',
  styleUrls: [
    './dashboard.component.css',
    './dashboard-theme.css'
  ]
})
export class DashboardComponent {}
```

```typescript
// SCSSファイルの使用
@Component({
  selector: 'app-card',
  standalone: true,
  templateUrl: './card.component.html',
  styleUrls: ['./card.component.scss']
})
export class CardComponent {}
```

## 💻 詳細実装例（学習用）

### 基本的な外部スタイル
```typescript
// user-profile.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-user-profile',
  standalone: true,
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.css']
})
export class UserProfileComponent {
  user = {
    name: 'John Doe',
    avatar: 'https://via.placeholder.com/100',
    email: 'john@example.com'
  };
}
```

```css
/* user-profile.component.css */
.profile-container {
  max-width: 600px;
  margin: 20px auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: white;
}

.profile-header {
  display: flex;
  align-items: center;
  gap: 20px;
  margin-bottom: 20px;
}

.avatar {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  object-fit: cover;
}

.user-info h2 {
  margin: 0 0 8px 0;
  color: #333;
  font-size: 24px;
}

.user-info p {
  margin: 0;
  color: #666;
}
```

### 複数スタイルファイルの組み合わせ
```typescript
// product-card.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-product-card',
  standalone: true,
  templateUrl: './product-card.component.html',
  styleUrls: [
    './product-card.component.css',      // 基本スタイル
    './product-card-layout.css',         // レイアウト
    './product-card-animations.css'      // アニメーション
  ]
})
export class ProductCardComponent {
  product = {
    name: 'Laptop',
    price: 1200,
    image: 'laptop.jpg'
  };
}
```

```css
/* product-card.component.css - 基本スタイル */
.card {
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  background: white;
}

.card-image {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.card-title {
  font-size: 18px;
  font-weight: bold;
  color: #333;
}

.card-price {
  font-size: 20px;
  color: #007bff;
  font-weight: bold;
}
```

```css
/* product-card-layout.css - レイアウト */
.card {
  display: flex;
  flex-direction: column;
}

.card-body {
  padding: 16px;
  flex: 1;
}

.card-footer {
  padding: 12px 16px;
  border-top: 1px solid #eee;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
```

```css
/* product-card-animations.css - アニメーション */
.card {
  transition: all 0.3s ease;
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 16px rgba(0,0,0,0.2);
}

.card-image {
  transition: transform 0.3s ease;
}

.card:hover .card-image {
  transform: scale(1.05);
}
```

### SCSSの使用
```typescript
// button.component.ts
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-button',
  standalone: true,
  template: `
    <button [class]="'btn btn-' + variant" [disabled]="disabled">
      {{label}}
    </button>
  `,
  styleUrls: ['./button.component.scss']
})
export class ButtonComponent {
  @Input() label = 'Click me';
  @Input() variant: 'primary' | 'secondary' | 'success' | 'danger' = 'primary';
  @Input() disabled = false;
}
```

```scss
/* button.component.scss */
// 変数定義
$primary-color: #007bff;
$secondary-color: #6c757d;
$success-color: #28a745;
$danger-color: #dc3545;

$btn-padding: 10px 20px;
$btn-border-radius: 4px;
$btn-transition: all 0.3s ease;

// ミックスイン
@mixin button-variant($bg-color, $text-color: white) {
  background-color: $bg-color;
  color: $text-color;

  &:hover:not(:disabled) {
    background-color: darken($bg-color, 10%);
  }

  &:active:not(:disabled) {
    background-color: darken($bg-color, 15%);
  }
}

// 基本スタイル
.btn {
  padding: $btn-padding;
  border: none;
  border-radius: $btn-border-radius;
  cursor: pointer;
  font-weight: bold;
  transition: $btn-transition;

  &:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }
}

// バリアント
.btn-primary {
  @include button-variant($primary-color);
}

.btn-secondary {
  @include button-variant($secondary-color);
}

.btn-success {
  @include button-variant($success-color);
}

.btn-danger {
  @include button-variant($danger-color);
}
```

### ネストしたSCSSスタイル
```typescript
// navigation.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-navigation',
  standalone: true,
  templateUrl: './navigation.component.html',
  styleUrls: ['./navigation.component.scss']
})
export class NavigationComponent {
  menuItems = [
    { label: 'Home', link: '/home' },
    { label: 'About', link: '/about' },
    { label: 'Contact', link: '/contact' }
  ];
}
```

```scss
/* navigation.component.scss */
$nav-bg: #333;
$nav-text: white;
$nav-hover-bg: #555;

.navigation {
  background-color: $nav-bg;

  .nav-list {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;

    .nav-item {
      .nav-link {
        display: block;
        padding: 15px 20px;
        color: $nav-text;
        text-decoration: none;
        transition: background-color 0.3s ease;

        &:hover {
          background-color: $nav-hover-bg;
        }

        &.active {
          background-color: darken($nav-bg, 10%);
          border-bottom: 3px solid #007bff;
        }
      }
    }
  }

  // レスポンシブ
  @media (max-width: 768px) {
    .nav-list {
      flex-direction: column;

      .nav-item {
        width: 100%;

        .nav-link {
          padding: 12px 16px;
        }
      }
    }
  }
}
```

### CSS変数とSCSSの組み合わせ
```typescript
// themed-card.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-themed-card',
  standalone: true,
  templateUrl: './themed-card.component.html',
  styleUrls: ['./themed-card.component.scss']
})
export class ThemedCardComponent {
  title = 'Themed Card';
  content = 'This card uses CSS variables for theming';
}
```

```scss
/* themed-card.component.scss */
:host {
  // デフォルトのCSS変数
  --card-bg: white;
  --card-text: #333;
  --card-border: #ddd;
  --card-shadow: rgba(0, 0, 0, 0.1);

  display: block;
}

.card {
  background-color: var(--card-bg);
  color: var(--card-text);
  border: 1px solid var(--card-border);
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 4px var(--card-shadow);

  .card-title {
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 12px;
  }

  .card-content {
    line-height: 1.6;
  }
}

// ダークテーマ対応
:host-context(.dark-theme) {
  --card-bg: #2d2d2d;
  --card-text: #f0f0f0;
  --card-border: #444;
  --card-shadow: rgba(0, 0, 0, 0.3);
}
```

### グローバルスタイルとの組み合わせ
```typescript
// app.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: [
    './app.component.scss',
    './styles/global-overrides.scss'  // グローバルオーバーライド
  ]
})
export class AppComponent {}
```

```scss
/* app.component.scss */
.app-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.main-content {
  flex: 1;
  padding: 20px;
}
```

```scss
/* styles/global-overrides.scss */
// このComponentでのみ有効なグローバルオーバーライド
::ng-deep {
  .mat-button {
    text-transform: uppercase;
  }

  .mat-form-field {
    width: 100%;
  }
}
```

### angular.jsonでSCSSを設定
```json
{
  "projects": {
    "my-app": {
      "architect": {
        "build": {
          "options": {
            "styles": [
              "src/styles.scss"
            ],
            "stylePreprocessorOptions": {
              "includePaths": [
                "src/styles"
              ]
            }
          }
        }
      },
      "schematics": {
        "@schematics/angular:component": {
          "style": "scss"
        }
      }
    }
  }
}
```

### 共有SCSSファイルのインポート
```scss
/* _variables.scss */
$primary-color: #007bff;
$secondary-color: #6c757d;
$success-color: #28a745;
$danger-color: #dc3545;

$spacing-unit: 8px;
$border-radius: 4px;
```

```scss
/* _mixins.scss */
@mixin flex-center {
  display: flex;
  align-items: center;
  justify-content: center;
}

@mixin card-shadow {
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.3s ease;

  &:hover {
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  }
}
```

```scss
/* component.component.scss */
@import 'variables';
@import 'mixins';

.my-card {
  @include card-shadow;

  padding: $spacing-unit * 2;
  border-radius: $border-radius;

  .card-header {
    @include flex-center;
    background-color: $primary-color;
    color: white;
  }
}
```

## ベストプラクティス

1. **外部ファイルを使用**: 10行以上のスタイルは外部化
2. **SCSSの活用**: 変数・ミックスイン・ネストを活用
3. **ファイル分割**: 目的別に複数ファイルに分ける
4. **相対パス使用**: `./`から始まるパス指定

## 注意点

- styleUrlsは配列形式で指定
- 複数ファイルの読み込み順序に注意
- SCSSを使う場合はangular.jsonで設定が必要
- スタイルはComponentにスコープされる

## 関連技術
- SCSS/Sass
- CSS Preprocessors
- Style Encapsulation
- Build Configuration
