# #011 「Component のファイル構成」

## 概要
AngularのComponentは通常4つのファイルで構成されます。各ファイルには明確な役割があり、統一された命名規則に従います。

## 学習目標
- Componentのファイル構成を理解する
- 各ファイルの役割を把握する
- ファイル命名規則を習得する

## 技術ポイント
- **4つのファイル**: TypeScript、HTML、CSS、テスト
- **命名規則**: [name].component.[拡張子]
- **ファイル配置**: 専用ディレクトリにまとめる

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```bash
# 標準的なComponentのファイル構成
user-profile/
  ├── user-profile.component.ts      # TypeScript
  ├── user-profile.component.html    # HTML
  ├── user-profile.component.css     # CSS
  └── user-profile.component.spec.ts # テスト
```

```typescript
// user-profile.component.ts
@Component({
  selector: 'app-user-profile',
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.css']
})
export class UserProfileComponent {
  user = { name: 'John' };
}
```

```html
<!-- user-profile.component.html -->
<div class="profile">
  <h2>{{user.name}}</h2>
  <p>User Profile</p>
</div>
```

## 💻 詳細実装例（学習用）

### 標準的なファイル構成
```bash
src/app/components/user-profile/
├── user-profile.component.ts       # Component本体
├── user-profile.component.html     # テンプレート
├── user-profile.component.css      # スタイル
└── user-profile.component.spec.ts  # ユニットテスト
```

各ファイルの内容：

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
    id: 1,
    name: 'John Doe',
    email: 'john@example.com',
    avatar: 'https://via.placeholder.com/100'
  };

  editProfile() {
    console.log('Editing profile');
  }
}
```

```html
<!-- user-profile.component.html -->
<div class="profile-container">
  <div class="profile-header">
    <img [src]="user.avatar" [alt]="user.name" class="avatar">
    <div class="user-info">
      <h2>{{user.name}}</h2>
      <p>{{user.email}}</p>
    </div>
  </div>
  <button (click)="editProfile()">Edit Profile</button>
</div>
```

```css
/* user-profile.component.css */
.profile-container {
  max-width: 600px;
  margin: 20px auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
}

.profile-header {
  display: flex;
  gap: 20px;
  margin-bottom: 20px;
}

.avatar {
  width: 100px;
  height: 100px;
  border-radius: 50%;
}

.user-info h2 {
  margin: 0 0 8px 0;
}

button {
  padding: 10px 20px;
  background: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
```

```typescript
// user-profile.component.spec.ts
import { ComponentFixture, TestBed } from '@angular/core/testing';
import { UserProfileComponent } from './user-profile.component';

describe('UserProfileComponent', () => {
  let component: UserProfileComponent;
  let fixture: ComponentFixture<UserProfileComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [UserProfileComponent]
    }).compileComponents();

    fixture = TestBed.createComponent(UserProfileComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should display user name', () => {
    const compiled = fixture.nativeElement;
    expect(compiled.querySelector('h2').textContent).toContain('John Doe');
  });
});
```

### インラインテンプレート/スタイルの場合
```bash
# ファイル数が少ない構成
button/
  ├── button.component.ts      # すべてを含む
  └── button.component.spec.ts # テストのみ別ファイル
```

```typescript
// button.component.ts
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-button',
  standalone: true,
  template: `
    <button [class]="variant">
      {{label}}
    </button>
  `,
  styles: [`
    button {
      padding: 10px 20px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    .primary { background: #007bff; color: white; }
    .secondary { background: #6c757d; color: white; }
  `]
})
export class ButtonComponent {
  @Input() label = 'Click me';
  @Input() variant = 'primary';
}
```

### SCSSを使用する場合
```bash
# SCSS使用時
product-card/
  ├── product-card.component.ts
  ├── product-card.component.html
  ├── product-card.component.scss    # .scss拡張子
  └── product-card.component.spec.ts
```

```typescript
// product-card.component.ts
@Component({
  selector: 'app-product-card',
  standalone: true,
  templateUrl: './product-card.component.html',
  styleUrls: ['./product-card.component.scss']  // .scss
})
export class ProductCardComponent {
  product = {
    name: 'Laptop',
    price: 1200
  };
}
```

```scss
// product-card.component.scss
$card-padding: 16px;
$primary-color: #007bff;

.card {
  padding: $card-padding;
  border: 1px solid #ddd;

  .card-title {
    color: $primary-color;
    font-weight: bold;
  }
}
```

### 複数スタイルファイルの構成
```bash
# 大規模Componentの例
dashboard/
  ├── dashboard.component.ts
  ├── dashboard.component.html
  ├── dashboard.component.css          # 基本スタイル
  ├── dashboard-layout.css             # レイアウト
  ├── dashboard-responsive.css         # レスポンシブ
  └── dashboard.component.spec.ts
```

```typescript
// dashboard.component.ts
@Component({
  selector: 'app-dashboard',
  standalone: true,
  templateUrl: './dashboard.component.html',
  styleUrls: [
    './dashboard.component.css',
    './dashboard-layout.css',
    './dashboard-responsive.css'
  ]
})
export class DashboardComponent {}
```

### 機能別ディレクトリ構造
```bash
# 機能ごとにグループ化
src/app/
├── features/
│   ├── user/
│   │   ├── user-list/
│   │   │   ├── user-list.component.ts
│   │   │   ├── user-list.component.html
│   │   │   ├── user-list.component.css
│   │   │   └── user-list.component.spec.ts
│   │   ├── user-detail/
│   │   │   ├── user-detail.component.ts
│   │   │   ├── user-detail.component.html
│   │   │   ├── user-detail.component.css
│   │   │   └── user-detail.component.spec.ts
│   │   └── user-form/
│   │       ├── user-form.component.ts
│   │       ├── user-form.component.html
│   │       ├── user-form.component.css
│   │       └── user-form.component.spec.ts
│   └── product/
│       └── ...
└── shared/
    └── components/
        └── ...
```

### Barrel Exportsを使った構成
```bash
# Componentのエクスポート管理
user/
  ├── user-list/
  │   └── user-list.component.ts
  ├── user-detail/
  │   └── user-detail.component.ts
  └── index.ts  # Barrel export
```

```typescript
// user/index.ts
export { UserListComponent } from './user-list/user-list.component';
export { UserDetailComponent } from './user-detail/user-detail.component';

// 使用側
import { UserListComponent, UserDetailComponent } from './user';
```

### モノレポ構成
```bash
# ライブラリとして管理
projects/
├── ui-components/
│   └── src/
│       └── lib/
│           ├── button/
│           │   ├── button.component.ts
│           │   ├── button.component.html
│           │   ├── button.component.css
│           │   └── button.component.spec.ts
│           ├── card/
│           │   └── ...
│           └── public-api.ts
└── my-app/
    └── src/
        └── app/
            └── ...
```

### CLIによる自動生成の設定
```json
// angular.json
{
  "schematics": {
    "@schematics/angular:component": {
      "style": "scss",              // デフォルトのスタイル形式
      "skipTests": false,           // テスト生成
      "inlineTemplate": false,      // 外部HTML
      "inlineStyle": false,         // 外部CSS
      "standalone": true,           // Standalone
      "changeDetection": "OnPush",  // 変更検知戦略
      "prefix": "app"               // プレフィックス
    }
  }
}
```

### テストファイルなしの構成
```bash
# --skip-tests オプション使用
ng g c simple-button --skip-tests

simple-button/
  ├── simple-button.component.ts
  ├── simple-button.component.html
  └── simple-button.component.css
```

### フラット構成
```bash
# --flat オプション使用（ディレクトリ作成なし）
ng g c app-header --flat

src/app/
├── app-header.component.ts
├── app-header.component.html
├── app-header.component.css
├── app-header.component.spec.ts
└── app.component.ts
```

### 推奨ディレクトリ構造
```bash
src/app/
├── core/                      # シングルトンサービス
│   ├── services/
│   └── guards/
├── shared/                    # 共有Component
│   ├── components/
│   │   ├── button/
│   │   ├── card/
│   │   └── modal/
│   └── directives/
├── features/                  # 機能別Component
│   ├── home/
│   ├── user/
│   └── product/
└── layout/                    # レイアウトComponent
    ├── header/
    ├── footer/
    └── sidebar/
```

## ベストプラクティス

1. **一貫した命名**: [name].component.[ext] 形式を厳守
2. **専用ディレクトリ**: 各Componentは専用フォルダに
3. **適切な配置**: 機能や用途でグループ化
4. **CLIの活用**: ng generateで標準構成を生成

## 注意点

- ファイル名は必ずケバブケース
- Componentごとに専用ディレクトリを作成
- 関連ファイルは同じディレクトリに配置
- テストファイルはComponent名.spec.ts

## 関連技術
- Angular CLI
- File Organization
- Project Structure
- Naming Conventions
