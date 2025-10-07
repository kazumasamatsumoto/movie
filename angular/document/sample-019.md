# #019 「Component 作成時のよくあるエラー」

## 概要
Component作成時によく発生するエラーとその解決方法を学びます。エラーを事前に防ぐためのチェックリストも提供します。

## 学習目標
- 典型的なエラーパターンを理解する
- エラーの原因と解決方法を習得する
- エラーを未然に防ぐ方法を学ぶ

## 技術ポイント
- **imports忘れ**: 必要なモジュールの追加
- **selector重複**: 一意な名前の使用
- **変更検知**: OnPush戦略の正しい使用

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
// エラー1: imports忘れ
// ❌ エラー
@Component({
  standalone: true,
  template: '<div *ngIf="show">Hello</div>'
})
// 解決: CommonModuleを追加
@Component({
  standalone: true,
  imports: [CommonModule],
  template: '<div *ngIf="show">Hello</div>'
})
```

```typescript
// エラー2: selector重複
// ❌ 重複
@Component({ selector: 'app-user' })
export class UserComponent {}
@Component({ selector: 'app-user' })  // 重複!
export class UserProfileComponent {}

// ✅ 一意な名前
@Component({ selector: 'app-user-profile' })
```

```typescript
// エラー3: Input型エラー
// ❌ 型不一致
@Input() user: User;  // undefinedの可能性

// ✅ 正しい型定義
@Input() user!: User;  // 必須
@Input() user?: User;  // オプショナル
```

## 💻 詳細実装例（学習用）

### よくあるエラー一覧

#### 1. imports忘れエラー
```typescript
// エラーメッセージ:
// Can't bind to 'ngIf' since it isn't a known property

// 原因
@Component({
  standalone: true,
  // imports: [CommonModule],  // 忘れた！
  template: `<div *ngIf="show">Content</div>`
})

// 解決
@Component({
  standalone: true,
  imports: [CommonModule],  // 追加
  template: `<div *ngIf="show">Content</div>`
})
```

#### 2. FormsModule忘れ
```typescript
// エラー: Can't bind to 'ngModel'
// 解決: FormsModuleを追加
@Component({
  standalone: true,
  imports: [FormsModule],
  template: `<input [(ngModel)]="name">`
})
```

#### 3. Component import忘れ
```typescript
// エラー: 'app-button' is not a known element
// 解決: Componentをimport
@Component({
  standalone: true,
  imports: [ButtonComponent],
  template: `<app-button>Click</app-button>`
})
```

#### 4. ExpressionChangedAfterItHasBeenCheckedError
```typescript
// 原因: 変更検知後にプロパティ変更
ngAfterViewInit() {
  this.value = 'changed';  // エラー！
}

// 解決: setTimeout使用
ngAfterViewInit() {
  setTimeout(() => {
    this.value = 'changed';
  });
}
```

## エラー解決チェックリスト

1. ✅ imports配列を確認
2. ✅ selector名の重複チェック
3. ✅ 型定義の確認
4. ✅ standalone: true の指定
5. ✅ ライフサイクルフックの使用確認

## 注意点

- エラーメッセージをよく読む
- コンソールを常に確認
- Angular DevToolsを活用
- 公式ドキュメントを参照

## 関連技術
- Error Handling
- Debugging
- Type Safety
- Angular Compiler
