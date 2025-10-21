# #616 「pristine - 未変更状態」

## 概要
pristineフラグはユーザーがコントロールを変更していない状態を示し、初期表示のエラー制御やリセット処理で重要な役割を担う。

## 学習目標
- pristineの意味と初期状態を理解する
- dirtyとの組み合わせでエラー表示を制御する
- リセット操作との関連性を把握する

## 技術ポイント
- 初期状態やreset後はpristine=true
- ユーザー入力でdirty=trueになりpristine=false
- エラー表示の条件にpristineを組み合わせる

## 📺 画面表示用コード（動画用）
```html
<span *ngIf="control.invalid && !control.pristine">必須です</span>
```

## 💻 詳細実装例（学習用）
```typescript
protected showError(controlName: string): boolean {
  const control = this.form.get(controlName);
  return !!control && control.invalid && !control.pristine;
}

protected reset(): void {
  this.form.reset();
  // ここでpristineがtrueに戻る
}
```

## ベストプラクティス
- pristineを使って初期表示でエラーを隠す
- reset後に状態が戻ったかテストで検証する
- UI側でpristineとdirtyの意味を共有しておく

## 注意点
- プログラムでsetValueするとpristineがfalseになる
- 複数コントロールをまとめて判定する場合はFormGroupのpristineも確認
- カスタムディレクティブで状態を変更するときは副作用に注意

## 関連技術
- dirty
- FormControlState
- reset()
