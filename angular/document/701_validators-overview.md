# #701 「Validators とは？検証の仕組み」

## 概要
ValidatorsはReactive Formsで値を検証し、ValidationErrorsを返してフォームのvalid/invalid状態を管理する仕組み。

## 学習目標
- Validatorsの基本概念を理解する
- ValidationErrorsの仕組みを把握する
- フォームにバリデーションを適用する流れを掴む

## 技術ポイント
- Validatorsは関数でValidationErrors | nullを返す
- FormControlに同期/非同期バリデーターを設定できる
- errorsプロパティにエラー情報が格納される

## 📺 画面表示用コード（動画用）
```html
<input [formControl]="emailCtrl" type="email" />
<span *ngIf="emailCtrl.invalid">入力を確認してください</span>
```

## 💻 詳細実装例（学習用）
```typescript
protected emailCtrl = new FormControl('', {
  validators: [Validators.required, Validators.email]
});
```

## ベストプラクティス
- バリデーション結果はUIに即座に反映させる
- カスタムバリデーターは再利用可能にしておく
- サーバー側の検証と重複しないよう役割分担する

## 注意点
- 同期と非同期バリデーションが混在すると状態が複雑になる
- エラーキーの命名を揃えないとUIマッピングが難しい
- UIだけでなくサーバー側の最終検証も忘れない

## 関連技術
- Validators
- ValidationErrors
- FormControl
