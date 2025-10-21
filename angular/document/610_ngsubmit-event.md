# #610 「ngSubmit イベント」

## 概要
ngSubmitイベントはformタグの送信をフックし、Angular側でカスタム処理やバリデーションを実行するための主要イベントである。

## 学習目標
- ngSubmitの発火タイミングを理解する
- テンプレート駆動・リアクティブ両方での扱いを学ぶ
- バリデーション連携の基本フローを把握する

## 技術ポイント
- ngSubmitはsubmitイベントをラップしてpreventDefaultも実行
- テンプレート駆動ではngFormのvalueを引数に渡せる
- リアクティブではFormGroupを直接参照して処理する

## 📺 画面表示用コード（動画用）
```html
<form #f="ngForm" (ngSubmit)="onSubmit(f.value)">
  <input name="email" ngModel required />
</form>
```

## 💻 詳細実装例（学習用）
```typescript
protected onSubmit(value: Record<string, unknown>): void {
  if (!value['email']) {
    return;
  }
  console.log('submit', value);
}

protected onSubmitReactive(): void {
  if (this.form.invalid) {
    return;
  }
  console.log(this.form.value);
}
```

## ベストプラクティス
- ngSubmit内ではフォームの有効性を必ず確認する
- 送信後は成功・失敗のフィードバックをUIに表示する
- API呼び出し中は送信ボタンを無効化して二重送信を防ぐ

## 注意点
- formタグが無いとngSubmitは発火しない
- 同期処理で例外が発生するとpreventDefaultが効かない場合がある
- テンプレートで関数を直接呼ぶとテストが難しくなるのでサービスに委譲する

## 関連技術
- ngForm
- FormGroup
- submitイベント
