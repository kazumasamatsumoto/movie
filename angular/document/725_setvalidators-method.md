# #725 「setValidators() メソッド」

## 概要
setValidatorsはコントロールのバリデーター配列を上書きし、変更後はupdateValueAndValidityで再評価する必要がある。

## 学習目標
- setValidatorsの挙動を理解する
- 再評価の必要性を把握する
- 既存バリデーターとの組み合わせ方を学ぶ

## 技術ポイント
- setValidators([...])で既存ルールを置き換える
- nullを渡すとバリデーション無しになる
- 変更後にupdateValueAndValidityが必須

## 📺 画面表示用コード（動画用）
```typescript
protected toggleValidators(required: boolean): void {
  if (required) {
    this.noteCtrl.setValidators([Validators.required, Validators.maxLength(200)]);
  } else {
    this.noteCtrl.setValidators([Validators.maxLength(200)]);
  }
  this.noteCtrl.updateValueAndValidity();
}
```

## 💻 詳細実装例（学習用）
```typescript
protected noteCtrl = new FormControl('');
```

## ベストプラクティス
- 既存バリデーターを保持したい場合は以前の配列をマージする
- バリデーション切り替えロジックをサービス化して再利用する
- 変更履歴をログ出力してデバッグしやすくする

## 注意点
- setValidatorsだけでは再評価されない
- nullを渡すとすべてのバリデーションが解除される
- 頻繁に切り替えるとパフォーマンスやUXに影響する

## 関連技術
- setValidators
- updateValueAndValidity
- 動的バリデーション
