# #004 「selector - コンポーネントの呼び出し方」台本

四国めたん「selector - コンポーネントの呼び出し方について解説します！」
ずんだもん「selectorって何をするものなの？」
四国めたん「selectorは、HTMLテンプレート内でComponentを使用する際のタグ名を定義します」
ずんだもん「どんな書き方があるの？」
四国めたん「要素セレクタ、属性セレクタ、クラスセレクタの3つのパターンがあります」
ずんだもん「使い分けはどうするの？」
四国めたん「用途に応じて選択します。要素セレクタが最も一般的です」

---

## 📺 画面表示用コード

// 要素セレクタ（最も一般的）
```typescript
@Component({
  selector: 'app-hello',
  template: '<h1>Hello World!</h1>'
})
export class HelloComponent {
  // 使用例: <app-hello></app-hello>
}
```

// 属性セレクタ
```typescript
@Component({
  selector: '[app-button]',
  template: '<button>Click me!</button>'
})
export class ButtonComponent {
  // 使用例: <div app-button></div>
}
```

// クラスセレクタ
```typescript
@Component({
  selector: '.app-card',
  template: '<div class="card">Card content</div>'
})
export class CardComponent {
  // 使用例: <div class="app-card"></div>
}
```

// 複合セレクタ
```typescript
@Component({
  selector: 'app-user[role="admin"]',
  template: '<div>Admin User</div>'
})
export class AdminUserComponent {
  // 使用例: <app-user role="admin"></app-user>
}
```

// 親子関係セレクタ
```typescript
@Component({
  selector: 'app-parent app-child',
  template: '<div>Child in parent</div>'
})
export class ChildComponent {
  // 使用例: <app-parent><app-child></app-child></app-parent>
}
```

// 隣接セレクタ
```typescript
@Component({
  selector: 'app-header + app-content',
  template: '<div>Content after header</div>'
})
export class ContentComponent {
  // 使用例: <app-header></app-header><app-content></app-content>
}
```

// セレクタの命名規則
```typescript
@Component({
  selector: 'app-user-profile',  // ✅ kebab-case
  template: '<div>User Profile</div>'
})
export class UserProfileComponent {
  // 推奨: app-プレフィックス + kebab-case
}

// ❌ 避けるべき命名
@Component({
  selector: 'UserProfile',       // ❌ PascalCase
  selector: 'userProfile',       // ❌ camelCase
  selector: 'user_profile',      // ❌ snake_case
})
```

// セレクタの実用例
```typescript
// 親Component
@Component({
  selector: 'app-dashboard',
  template: `
    <h1>ダッシュボード</h1>
    <app-user-card></app-user-card>
    <app-stats-widget></app-stats-widget>
    <div app-highlight>重要な情報</div>
  `
})
export class DashboardComponent {
  // 複数のセレクタパターンを使用
}
```
