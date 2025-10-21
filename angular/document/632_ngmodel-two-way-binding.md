# #632 「[(ngModel)] 双方向バインディング」

## 概要
[(ngModel)]構文は入力とコンポーネントプロパティの双方向バインディングを実現し、テンプレート駆動フォームで値同期を簡潔に記述できる。

## 学習目標
- [(ngModel)]の構文と動作原理を理解する
- ngModelとngModelChangeの関係を把握する
- 双方向バインディングの利点と注意点を学ぶ

## 技術ポイント
- [(ngModel)]はプロパティバインディングとイベントバインディングの糖衣構文
- ngModelChangeイベントで値変更をフックできる
- 双方向バインディングはシンプルだがロジックが複雑な場合は分離を検討

## 📺 画面表示用コード（動画用）
```html
<input [(ngModel)]="profile.email" (ngModelChange)="validateEmail()" />
```

## 💻 詳細実装例（学習用）
```typescript
protected profile = { email: '' };
protected emailHint = '';

protected validateEmail(): void {
    this.emailHint = this.profile.email.includes('@') ? '' : 'メール形式を確認してください';
}
```

## ベストプラクティス
- ngModelChangeを使って副作用を局所化する
- 双方向バインディングが複雑になる場合はコンポーネントメソッドで制御する
- フォームモデルをオブジェクトでまとめて扱う

## 注意点
- 大量の[(ngModel)]はコンポーネントの責務を肥大化させる
- 複雑な状態管理はリアクティブフォームを検討
- テンプレートでのロジック過多に注意

## 関連技術
- ngModelChange
- テンプレート駆動フォーム
- 双方向バインディング
