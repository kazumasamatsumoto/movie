# #621 「invalid - 無効状態」

## 概要
invalidフラグはフォームやコントロールがバリデーションエラーを抱えている状態を示し、エラー表示や送信制御の中心となる。

## 学習目標
- invalidの意味と発生条件を理解する
- errorsオブジェクトの扱い方を学ぶ
- フォーム全体のinvalid判定を活用する

## 技術ポイント
- 任意のバリデーション失敗でinvalid=true
- errorsプロパティにエラー内容が格納
- FormGroup.invalidで全体の送信可否を判定

## 📺 画面表示用コード（動画用）
```html
<div *ngIf="control.invalid && control.touched">
  {{ control.errors | json }}
</div>
```

## 💻 詳細実装例（学習用）
```typescript
protected getErrorKeys(controlName: string): string[] {
  const errors = this.form.get(controlName)?.errors;
  return errors ? Object.keys(errors) : [];
}

protected hasFormError(): boolean {
  return this.form.invalid;
}
```

## ベストプラクティス
- errorsキーをメッセージ辞書に変換して表示する
- フォーム全体のinvalidを利用し送信ボタンを制御する
- ログや監視にinvalid発生状況を記録する

## 注意点
- errorsがnullになるタイミングを考慮する
- 複数エラーがある場合の表示優先順位を決める
- ネストしたFormGroupのinvalidは親にも伝搬する

## 関連技術
- Validators
- エラーメッセージ設計
- FormGroup
