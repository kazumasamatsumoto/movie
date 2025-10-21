# #638 「NgForm の活用」

## 概要
NgFormはテンプレート駆動フォーム全体を表現するディレクティブで、値・状態・操作メソッドを備えており送信処理やリセットに利用できる。

## 学習目標
- NgFormが提供する主なプロパティを把握する
- resetFormやsubmittedなどの活用方法を学ぶ
- テンプレートとコンポーネントの連携パターンを理解する

## 技術ポイント
- NgForm.valueでフォーム値を取得
- NgForm.validやdirtyなどの状態を参照
- NgForm.resetForm()で値と状態を初期化

## 📺 画面表示用コード（動画用）
```html
<form #form="ngForm" (ngSubmit)="submit(form)">
  <button type="submit">送信</button>
  <button type="button" (click)="form.resetForm()">リセット</button>
</form>
```

## 💻 詳細実装例（学習用）
```typescript
protected submit(form: NgForm): void {
    if (form.invalid) {
        form.control.markAllAsTouched();
        return;
    }
    console.log('submit', form.value);
    form.resetForm();
}
```

## ベストプラクティス
- NgFormをViewChildで取得して状態をログ出力する
- resetFormに初期値を渡して再入力をサポートする
- submittedフラグで送信後のUI制御を行う

## 注意点
- NgFormへのアクセスはundefinedチェックを行う
- resetFormでdisabled状態が維持される点に注意
- 大規模フォームではNgFormだけで状態把握しづらい

## 関連技術
- NgForm
- resetForm
- テンプレート駆動フォーム
