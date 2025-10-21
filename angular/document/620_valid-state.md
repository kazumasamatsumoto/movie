# #620 「valid - 有効状態」

## 概要
validフラグはフォームまたはコントロールが同期バリデーションを満たしている状態を表し、送信可否やUI制御の基準として利用される。

## 学習目標
- validの意味と同期バリデーションの関係を理解する
- pendingとの状態遷移を把握する
- UI制御にvalidを活用する方法を学ぶ

## 技術ポイント
- 全ての同期バリデーションが成功するとvalid=true
- FormGroupは子コントロールが全てvalidのときにvalid
- 非同期バリデーション中はpendingになる

## 📺 画面表示用コード（動画用）
```html
<button type="submit" [disabled]="!form.valid">保存</button>
```

## 💻 詳細実装例（学習用）
```typescript
protected statusLabel(): string {
  if (this.form.pending) {
    return '検証中';
  }
  return this.form.valid ? '送信できます' : '入力を確認してください';
}

protected save(): void {
  if (!this.form.valid) {
    return;
  }
  // 送信処理
}
```

## ベストプラクティス
- validをボタン制御や成功表示に活用する
- pending状態との切り替えをUXに反映する
- FormGroupと個別コントロールのvalidを両方チェックする

## 注意点
- 非同期バリデーションが完了する前にvalidを参照しない
- カスタムバリデーションの戻り値が適切か確認する
- フォーム初期化後はvalid=trueでもデータをそのまま送らないよう注意

## 関連技術
- pending
- Validators
- UI制御
