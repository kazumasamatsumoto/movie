# #012 「Component の命名規則」

## 概要
Angularには明確な命名規則があります。クラス名、ファイル名、selectorそれぞれに適切な命名形式を使用することで、可読性と保守性が向上します。

## 学習目標
- Componentの命名規則を理解する
- PascalCaseとケバブケースの使い分けを習得する
- 一貫した命名パターンを身につける

## 技術ポイント
- **クラス名**: PascalCase + Component接尾辞
- **ファイル名**: ケバブケース + .component.拡張子
- **selector**: ケバブケース + プレフィックス

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
// クラス名: PascalCase + Component
export class UserProfileComponent {
  // ファイル名: user-profile.component.ts
  // selector: app-user-profile
}
```

```typescript
// 正しい命名例
@Component({
  selector: 'app-user-profile',  // ケバブケース
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.css']
})
export class UserProfileComponent {}  // PascalCase
```

```typescript
// 命名パターン
// クラス: ProductListComponent
// ファイル: product-list.component.ts
// selector: app-product-list
@Component({
  selector: 'app-product-list',
  template: '<div>Products</div>'
})
export class ProductListComponent {}
```

## 💻 詳細実装例（学習用）

### 基本的な命名規則
```typescript
// ✅ 正しい命名
// クラス名: PascalCase + "Component"
export class UserProfileComponent {}

// ファイル名: ケバブケース + ".component.ts"
// user-profile.component.ts

// selector: プレフィックス + ケバブケース
@Component({
  selector: 'app-user-profile'
})

// ❌ 間違った命名
export class userprofile {}           // PascalCaseでない
export class User_Profile_Component {} // アンダースコア使用
export class Userprofile {}            // Component接尾辞なし
```

### 命名パターン一覧
```typescript
// 1. シンプルなComponent
// クラス: ButtonComponent
// ファイル: button.component.ts
// selector: app-button
@Component({
  selector: 'app-button',
  template: '<button>Click</button>'
})
export class ButtonComponent {}

// 2. 複合語のComponent
// クラス: UserProfileCardComponent
// ファイル: user-profile-card.component.ts
// selector: app-user-profile-card
@Component({
  selector: 'app-user-profile-card',
  templateUrl: './user-profile-card.component.html'
})
export class UserProfileCardComponent {}

// 3. 機能を表すComponent
// クラス: LoginFormComponent
// ファイル: login-form.component.ts
// selector: app-login-form
@Component({
  selector: 'app-login-form',
  templateUrl: './login-form.component.html'
})
export class LoginFormComponent {}

// 4. レイアウトComponent
// クラス: MainHeaderComponent
// ファイル: main-header.component.ts
// selector: app-main-header
@Component({
  selector: 'app-main-header',
  templateUrl: './main-header.component.html'
})
export class MainHeaderComponent {}
```

### プレフィックスのカスタマイズ
```typescript
// デフォルト: app
@Component({
  selector: 'app-user',
  template: '<p>User</p>'
})
export class UserComponent {}

// カスタムプレフィックス: admin
@Component({
  selector: 'admin-dashboard',
  template: '<div>Admin Dashboard</div>'
})
export class AdminDashboardComponent {}

// UIライブラリ用: ui
@Component({
  selector: 'ui-button',
  template: '<button><ng-content></ng-content></button>'
})
export class ButtonComponent {}

// 機能別プレフィックス: feature-
@Component({
  selector: 'feature-user-list',
  template: '<div>User List</div>'
})
export class FeatureUserListComponent {}
```

### angular.jsonでプレフィックス設定
```json
{
  "projects": {
    "my-app": {
      "prefix": "app",
      // CLIで生成時に自動適用
    },
    "admin-dashboard": {
      "prefix": "admin"
    },
    "ui-library": {
      "prefix": "ui"
    }
  }
}
```

### 特殊な命名パターン

#### ページComponent
```typescript
// ページComponent: [Name]PageComponent
// ファイル: home-page.component.ts
// selector: app-home-page
@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html'
})
export class HomePageComponent {}

// または Page接尾辞
// about-page.component.ts
export class AboutPageComponent {}
```

#### ダイアログComponent
```typescript
// ダイアログ: [Name]DialogComponent
// ファイル: confirm-dialog.component.ts
// selector: app-confirm-dialog
@Component({
  selector: 'app-confirm-dialog',
  templateUrl: './confirm-dialog.component.html'
})
export class ConfirmDialogComponent {}
```

#### モーダルComponent
```typescript
// モーダル: [Name]ModalComponent
// ファイル: user-settings-modal.component.ts
// selector: app-user-settings-modal
@Component({
  selector: 'app-user-settings-modal',
  templateUrl: './user-settings-modal.component.html'
})
export class UserSettingsModalComponent {}
```

#### ウィジェットComponent
```typescript
// ウィジェット: [Name]WidgetComponent
// ファイル: weather-widget.component.ts
// selector: app-weather-widget
@Component({
  selector: 'app-weather-widget',
  templateUrl: './weather-widget.component.html'
})
export class WeatherWidgetComponent {}
```

### ディレクトリとファイルの命名
```bash
# 標準的な構成
user-profile/
  ├── user-profile.component.ts      # PascalCase: UserProfileComponent
  ├── user-profile.component.html
  ├── user-profile.component.css
  └── user-profile.component.spec.ts

# 複雑なComponent
product-detail-card/
  ├── product-detail-card.component.ts      # ProductDetailCardComponent
  ├── product-detail-card.component.html
  ├── product-detail-card.component.scss
  └── product-detail-card.component.spec.ts
```

### 略語の扱い
```typescript
// ✅ 推奨: 略語も通常の単語として扱う
export class HttpClientComponent {}      // HTTPではなくHttp
export class ApiServiceComponent {}      // APIではなくApi
export class HtmlEditorComponent {}      // HTMLではなくHtml
export class CssProcessorComponent {}    // CSSではなくCss

// ファイル名も同様
// http-client.component.ts
// api-service.component.ts
// html-editor.component.ts

// ❌ 避けるべき
export class HTTPClientComponent {}
export class APIServiceComponent {}
```

### 数字を含む命名
```typescript
// ✅ 数字は単語の一部として扱う
export class Card3dComponent {}
// ファイル: card3d.component.ts
// selector: app-card3d

export class Player2Component {}
// ファイル: player2.component.ts
// selector: app-player2

// または明示的に分離
export class Card3DComponent {}
// ファイル: card-3d.component.ts
// selector: app-card-3d
```

### 機能別命名パターン
```typescript
// リストComponent
export class UserListComponent {}        // user-list.component.ts
export class ProductListComponent {}     // product-list.component.ts

// 詳細Component
export class UserDetailComponent {}      // user-detail.component.ts
export class ProductDetailComponent {}   // product-detail.component.ts

// フォームComponent
export class UserFormComponent {}        // user-form.component.ts
export class LoginFormComponent {}       // login-form.component.ts

// カードComponent
export class UserCardComponent {}        // user-card.component.ts
export class ProductCardComponent {}     // product-card.component.ts

// テーブルComponent
export class UserTableComponent {}       // user-table.component.ts
export class DataTableComponent {}       // data-table.component.ts
```

### 共有Componentの命名
```bash
# 共有Component専用のプレフィックス
shared/components/
├── button/
│   └── button.component.ts          # SharedButtonComponent または ButtonComponent
├── card/
│   └── card.component.ts            # SharedCardComponent または CardComponent
└── modal/
    └── modal.component.ts           # SharedModalComponent または ModalComponent
```

```typescript
// オプション1: 通常の命名
@Component({
  selector: 'app-button',  // 共有でも通常のプレフィックス
  template: '<button><ng-content></ng-content></button>'
})
export class ButtonComponent {}

// オプション2: 明示的なプレフィックス
@Component({
  selector: 'shared-button',  // sharedプレフィックス
  template: '<button><ng-content></ng-content></button>'
})
export class SharedButtonComponent {}
```

### 命名のチェックリスト
```typescript
// ✅ チェックポイント
// 1. クラス名はPascalCase？
export class UserProfileComponent {}  // ✅

// 2. Component接尾辞がある？
export class UserProfileComponent {}  // ✅
export class UserProfile {}           // ❌

// 3. ファイル名はケバブケース？
// user-profile.component.ts  // ✅
// UserProfile.component.ts   // ❌

// 4. selectorはケバブケース？
@Component({
  selector: 'app-user-profile',  // ✅
  selector: 'appUserProfile',    // ❌
  selector: 'app_user_profile'   // ❌
})

// 5. プレフィックスがある？
@Component({
  selector: 'app-user',    // ✅
  selector: 'user',        // ❌ (プレフィックスなし)
})
```

### CLIによる自動命名
```bash
# CLIは自動的に正しい命名を適用
ng generate component user-profile

# 生成されるファイル
user-profile/
  ├── user-profile.component.ts      # export class UserProfileComponent
  ├── user-profile.component.html
  ├── user-profile.component.css
  └── user-profile.component.spec.ts

# selector も自動設定
# selector: 'app-user-profile'
```

## ベストプラクティス

1. **CLIを活用**: 自動生成で命名規則を統一
2. **Component接尾辞**: クラス名には必ずComponentを付ける
3. **プレフィックス使用**: selectorには必ずプレフィックス
4. **一貫性の維持**: プロジェクト全体で統一された命名

## 注意点

- クラス名とファイル名は対応させる
- selectorは一意の名前にする
- 略語は通常の単語として扱う
- 数字の扱いはプロジェクト内で統一

## 関連技術
- Naming Conventions
- Code Style Guide
- Angular Style Guide
- File Organization
