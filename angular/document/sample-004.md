# #004 「selector - コンポーネントの呼び出し方」

## 概要
selectorはComponentをテンプレート内で使用するための識別子です。適切な命名規則に従うことで、可読性と保守性が向上します。

## 学習目標
- selectorの役割を理解する
- 命名規則とベストプラクティスを習得する
- 様々なselectorタイプを理解する

## 技術ポイント
- **selector**: Component識別子
- **ケバブケース**: 推奨される命名形式
- **プレフィックス**: 名前空間の衝突を防ぐ

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
// 基本的なselector
@Component({
  selector: 'app-user',
  template: '<p>User Component</p>'
})
export class UserComponent {}

// 使用方法
// <app-user></app-user>
```

```typescript
// プレフィックス付きselector（推奨）
@Component({
  selector: 'app-user-profile',
  template: '<div>{{name}}</div>'
})
export class UserProfileComponent {
  name = 'John Doe';
}
```

```typescript
// v20のStandalone Componentでの使用
@Component({
  selector: 'app-card',
  standalone: true,
  template: '<div class="card">Card Content</div>'
})
export class CardComponent {}

// 自己終了タグも可能
// <app-card />
```

## 💻 詳細実装例（学習用）

### Element Selector（要素セレクタ）
```typescript
// 最も一般的なセレクタタイプ
@Component({
  selector: 'app-header',
  standalone: true,
  template: `
    <header>
      <h1>My Application</h1>
      <nav>Navigation</nav>
    </header>
  `
})
export class HeaderComponent {}

// 使用例
// <app-header></app-header>
// または自己終了タグ
// <app-header />
```

### Attribute Selector（属性セレクタ）
```typescript
@Component({
  selector: '[appHighlight]',
  standalone: true,
  template: `<span><ng-content></ng-content></span>`,
  styles: [`
    :host {
      background-color: yellow;
      padding: 2px 4px;
    }
  `]
})
export class HighlightComponent {}

// 使用例
// <p appHighlight>This text is highlighted</p>
```

### Class Selector（クラスセレクタ）
```typescript
@Component({
  selector: '.app-special',
  template: `<div class="special-content"><ng-content></ng-content></div>`,
  styles: [`
    .special-content {
      border: 2px solid blue;
      padding: 16px;
    }
  `]
})
export class SpecialComponent {}

// 使用例
// <div class="app-special">Special content</div>
```

### 複数セレクタの組み合わせ
```typescript
@Component({
  selector: 'app-button, [appButton], .app-button',
  standalone: true,
  template: `
    <button>
      <ng-content></ng-content>
    </button>
  `
})
export class ButtonComponent {}

// 使用例（すべて有効）
// <app-button>Click</app-button>
// <div appButton>Click</div>
// <div class="app-button">Click</div>
```

### プレフィックスのカスタマイズ
```typescript
// angular.jsonで設定
{
  "projects": {
    "my-app": {
      "prefix": "myapp"
    }
  }
}

// CLIで生成時に自動的にプレフィックスが適用される
@Component({
  selector: 'myapp-user',  // "myapp-"が自動付与
  template: '<p>User</p>'
})
export class UserComponent {}

// 個別にプレフィックスを指定して生成
// ng g c custom-button --prefix=custom
```

### 機能別のプレフィックス戦略
```typescript
// UI Componentsグループ
@Component({
  selector: 'ui-button',
  standalone: true,
  template: '<button><ng-content></ng-content></button>'
})
export class ButtonComponent {}

@Component({
  selector: 'ui-card',
  standalone: true,
  template: '<div class="card"><ng-content></ng-content></div>'
})
export class CardComponent {}

// Feature Componentsグループ
@Component({
  selector: 'feature-user-list',
  standalone: true,
  template: '<div>User List</div>'
})
export class UserListComponent {}

@Component({
  selector: 'feature-dashboard',
  standalone: true,
  template: '<div>Dashboard</div>'
})
export class DashboardComponent {}

// Layout Componentsグループ
@Component({
  selector: 'layout-header',
  standalone: true,
  template: '<header>Header</header>'
})
export class HeaderComponent {}

@Component({
  selector: 'layout-footer',
  standalone: true,
  template: '<footer>Footer</footer>'
})
export class FooterComponent {}
```

### セレクタの命名パターン
```typescript
// パターン1: 機能を表す名前
@Component({
  selector: 'app-user-profile',
  template: '<div>User Profile</div>'
})
export class UserProfileComponent {}

// パターン2: UI要素を表す名前
@Component({
  selector: 'app-dropdown-menu',
  template: '<div>Dropdown Menu</div>'
})
export class DropdownMenuComponent {}

// パターン3: レイアウトを表す名前
@Component({
  selector: 'app-sidebar-nav',
  template: '<nav>Sidebar</nav>'
})
export class SidebarNavComponent {}

// パターン4: ビジネスロジックを表す名前
@Component({
  selector: 'app-order-summary',
  template: '<div>Order Summary</div>'
})
export class OrderSummaryComponent {}
```

### Componentの階層構造での使用
```typescript
// 親Component
@Component({
  selector: 'app-user-dashboard',
  standalone: true,
  imports: [UserProfileComponent, UserStatsComponent, UserSettingsComponent],
  template: `
    <div class="dashboard">
      <app-user-profile />
      <app-user-stats />
      <app-user-settings />
    </div>
  `
})
export class UserDashboardComponent {}

// 子Component 1
@Component({
  selector: 'app-user-profile',
  standalone: true,
  template: '<div class="profile">Profile</div>'
})
export class UserProfileComponent {}

// 子Component 2
@Component({
  selector: 'app-user-stats',
  standalone: true,
  template: '<div class="stats">Stats</div>'
})
export class UserStatsComponent {}

// 子Component 3
@Component({
  selector: 'app-user-settings',
  standalone: true,
  template: '<div class="settings">Settings</div>'
})
export class UserSettingsComponent {}
```

### セレクタの衝突を避ける例
```typescript
// ❌ 悪い例: 一般的すぎる名前
@Component({
  selector: 'button',  // ネイティブHTML要素と衝突
  template: '<button>Click</button>'
})
export class BadButtonComponent {}

// ❌ 悪い例: プレフィックスなし
@Component({
  selector: 'user-card',  // 他のライブラリと衝突の可能性
  template: '<div>User Card</div>'
})
export class BadUserCardComponent {}

// ✅ 良い例: 明確なプレフィックス
@Component({
  selector: 'app-user-card',
  standalone: true,
  template: '<div class="user-card">User Card</div>'
})
export class GoodUserCardComponent {}

// ✅ 良い例: 機能別プレフィックス
@Component({
  selector: 'admin-user-card',
  standalone: true,
  template: '<div class="admin-card">Admin User Card</div>'
})
export class AdminUserCardComponent {}
```

## ベストプラクティス

1. **ケバブケースを使用**: app-user-profile形式
2. **プレフィックスを必ず付ける**: 名前空間の衝突を防ぐ
3. **意味のある名前**: 機能が明確にわかる名前
4. **一貫性のある命名**: プロジェクト全体で統一

## 注意点

- HTML標準要素名は使用しない（button、div等）
- selectorは一意である必要がある
- ケバブケースが推奨（camelCaseは非推奨）
- プレフィックスは2-4文字が理想的

## 関連技術
- CSS Selectors
- Web Components
- Custom Elements
- Naming Conventions
