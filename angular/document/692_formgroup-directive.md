# #692 「[formGroup] ディレクティブ」

## 概要
[formGroup]ディレクティブはテンプレートのフォーム要素とFormGroupインスタンスを同期させ、内部のformControlNameやformGroupNameが利用できるようにする。

## 学習目標
- [formGroup]の基本的な使い方を理解する
- テンプレート内の子ディレクティブとの連携を把握する
- フォーム送信処理との組み合わせを学ぶ

## 技術ポイント
- [formGroup]でフォーム要素とFormGroupをバインド
- ngSubmitと組み合わせて送信処理を呼び出す
- FormGroupを差し替えるとテンプレートが再評価される

## 📺 画面表示用コード（動画用）
```html
<form [formGroup]="profileForm" (ngSubmit)="onSubmit()">
  <input formControlName="name" />
  <button type="submit">送信</button>
</form>
```

## 💻 詳細実装例（学習用）
```typescript
protected profileForm = new FormGroup({
  name: new FormControl('', { nonNullable: true })
});

protected onSubmit(): void {
  console.log(this.profileForm.value);
}
```

## ベストプラクティス
- フォーム要素にroleやautocomplete属性も合わせて設定する
- フォーム差し替え時はmarkForCheckを検討する
- テンプレートでフォームがnullの場合に備えて安全演算子を使う

## 注意点
- formタグ以外に設定すると送信イベントが期待通りに動かない
- FormGroupインスタンスをnullにするとテンプレートで例外が出る
- テンプレートリファレンスと併用する場合は順序に注意

## 関連技術
- [formGroup]
- ngSubmit
- Reactive Formsテンプレート
