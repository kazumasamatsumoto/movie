# #708 「Validators.email - メールアドレス」

## 概要
Validators.emailは簡易的なメールアドレス形式をチェックし、type="email"属性と併用するとユーザー体験が向上する。

## 学習目標
- Validators.emailの働きを理解する
- HTML属性との連携を把握する
- 厳密な検証との使い分けを学ぶ

## 技術ポイント
- RFC完全対応ではない簡易チェック
- type="email"でモバイルキーボードが最適化
- 追加ルールはカスタムバリデーターで実装

## 📺 画面表示用コード（動画用）
```html
<input type="email" [formControl]="emailCtrl" />
<span *ngIf="emailCtrl.errors?.email">メール形式を確認してください</span>
```

## 💻 詳細実装例（学習用）
```typescript
protected emailCtrl = new FormControl('', [Validators.required, Validators.email]);
```

## ベストプラクティス
- type="email"属性とバリデーションを併用する
- ドメイン制限など追加要件はカスタムバリデーターで実装する
- 送信前にtrimして空白を除去する

## 注意点
- Validators.emailだけではすべての形式を網羅できない
- モバイルブラウザによって挙動が異なる
- 国際化ドメインなど特殊ケースを考慮する

## 関連技術
- Validators.email
- type="email"
- カスタム検証
