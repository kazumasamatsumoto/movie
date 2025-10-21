# #703 「Validators.requiredTrue - 真値必須」

## 概要
Validators.requiredTrueはFormControlの値がtrueでなければエラーを返し、利用規約同意などのチェックボックスに適している。

## 学習目標
- requiredTrueの用途を理解する
- チェックボックスとの連携を学ぶ
- エラーメッセージの表示方法を把握する

## 技術ポイント
- 値がtrueのときのみ有効
- boolean型FormControlと組み合わせる
- errors.requiredTrueでエラー判定

## 📺 画面表示用コード（動画用）
```html
<label>
  <input type="checkbox" [formControl]="agreeCtrl" /> 利用規約に同意
</label>
<span *ngIf="agreeCtrl.errors?.requiredTrue">同意が必要です</span>
```

## 💻 詳細実装例（学習用）
```typescript
protected agreeCtrl = new FormControl(false, Validators.requiredTrue);
```

## ベストプラクティス
- チェックボックスのラベルに必須であることを明記する
- フォーム送信時にエラーが出たらフォーカスを移動する
- アクセシビリティのためにaria-describedbyでエラーを紐づける

## 注意点
- 値が文字列"true"の場合はエラーになるのでboolean型で扱う
- テンプレート駆動フォームとは使い方が異なる点に注意
- 複数チェックが必要な場合はカスタムバリデーションを検討

## 関連技術
- Validators.requiredTrue
- チェックボックス
- アクセシビリティ
