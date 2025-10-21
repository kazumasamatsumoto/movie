# #613 「フォームのリセット」

## 概要
フォームを初期状態に戻すにはテンプレート駆動とリアクティブで提供されるresetAPIを利用し、値と状態を同時にリセットする。

## 学習目標
- フォームリセットが必要なケースを理解する
- テンプレート駆動とリアクティブでのリセット方法を学ぶ
- 初期値の扱いと状態リセットの関係を把握する

## 技術ポイント
- ngFormではresetForm(initialValue)が利用可能
- FormGroupのreset(value)で値と状態を同時に更新
- type=resetボタンは独自処理と競合しないよう注意

## 📺 画面表示用コード（動画用）
```html
<button type="button" (click)="reset()">クリア</button>
```

## 💻 詳細実装例（学習用）
```typescript
protected readonly initialState = {
  name: '',
  email: ''
};

protected reset(): void {
  this.form.reset(this.initialState);
}

protected resetTemplate(form: NgForm): void {
  form.resetForm(this.initialState);
}
```

## ベストプラクティス
- 初期値は定数として管理しリセット時に再利用する
- 確認ダイアログを入れて誤操作を防ぐ
- リセット後のフォーカス位置を決めておく

## 注意点
- reset時に配列やネストしたグループが初期化されるか確認する
- type=resetボタンだけに頼ると独自状態が戻らない
- disabled状態のコントロールはreset後もdisabledのままになる

## 関連技術
- FormGroup.reset
- NgForm.resetForm
- UX設計
