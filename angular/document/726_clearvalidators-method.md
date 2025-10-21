# #726 「clearValidators() メソッド」

## 概要
clearValidatorsはコントロールに設定されたバリデーターをすべて削除し、再評価のためにupdateValueAndValidityを呼び出す必要がある。

## 学習目標
- clearValidatorsの役割を理解する
- 再評価の手順を学ぶ
- 条件的なバリデーション解除の設計を把握する

## 技術ポイント
- clearValidators()でバリデーターを全解除
- 解除後にupdateValueAndValidityで状態更新
- 再度setValidatorsで再設定できる

## 📺 画面表示用コード（動画用）
```typescript
protected disableValidation(): void {
  this.emailCtrl.clearValidators();
  this.emailCtrl.updateValueAndValidity();
}
```

## 💻 詳細実装例（学習用）
```typescript
protected emailCtrl = new FormControl('', [Validators.required, Validators.email]);
```

## ベストプラクティス
- 再度バリデーションを有効化する流れも用意する
- 解除後にエラーメッセージを隠すUI処理を行う
- 状態遷移をドキュメント化してレビューしやすくする

## 注意点
- clearValidators後にupdateValueAndValidityを呼ばないとエラーが残る
- 解除すると想定外の値が許容されないか確認する
- フォーム送信前に必要なバリデーションが外れていないかチェックする

## 関連技術
- clearValidators
- updateValueAndValidity
- 動的フォーム
