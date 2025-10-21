# #619 「untouched - 未タッチ状態」

## 概要
untouchedフラグはフォーカスされていない状態を示し、初期表示のガイダンスや送信時の一括バリデーション制御に役立つ。

## 学習目標
- untouchedの意味と利用シーンを理解する
- touchedとの関係性を把握する
- ユーザーガイダンスに活用する方法を学ぶ

## 技術ポイント
- 初期状態はuntouched=true
- markAllAsTouchedでuntouchedがfalseになる
- テンプレートからngModel.untouchedにアクセス可能

## 📺 画面表示用コード（動画用）
```html
<p *ngIf="control.untouched">入力を開始してください</p>
```

## 💻 詳細実装例（学習用）
```typescript
protected showHint(controlName: string): boolean {
  const control = this.form.get(controlName);
  return !!control && control.untouched;
}

protected focusFirstInvalid(): void {
  const firstInvalid = Object.entries(this.form.controls)
    .find(([, ctrl]) => ctrl.invalid && ctrl.untouched);
  if (firstInvalid) {
    this.scrollTo(firstInvalid[0]);
  }
}
```

## ベストプラクティス
- 未操作フィールドにはガイダンスを表示し入力誘導する
- untouchedを利用して初期状態と操作済みを区別する
- scrollToなどのUX向上施策と組み合わせる

## 注意点
- 自動入力やブラウザ補完でuntouchedが変化するケースを確認
- モバイルブラウザの挙動が異なるため実機テストを行う
- markAllAsTouchedを呼ぶとuntouchedがfalseになることを前提にする

## 関連技術
- touched
- ユーザーガイド
- スクロール制御
