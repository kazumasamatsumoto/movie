# #630 「フォームのアクセシビリティ」

## 概要
フォームのアクセシビリティはラベル関連付け、フォーカス制御、エラーメッセージの通知などを整え、全てのユーザーが利用できる体験を提供することを目的とする。

## 学習目標
- フォームアクセシビリティの基本要素を理解する
- aria属性とエラーメッセージの扱い方を学ぶ
- キーボード操作とフォーカス制御のポイントを把握する

## 技術ポイント
- label for/idで入力とラベルを関連付け
- aria-describedbyでエラーやヒントを読み上げ
- フォーカス移動でエラー箇所へ誘導

## 📺 画面表示用コード（動画用）
```html
<label for="email">メールアドレス</label>
<input id="email" name="email" aria-describedby="emailError" />
<p id="emailError" role="alert">必須です</p>
```

## 💻 詳細実装例（学習用）
```typescript
protected onSubmit(): void {
  if (this.form.invalid) {
    const firstError = this.findFirstInvalid();
    firstError?.focus();
    return;
  }
  // 送信処理
}

private findFirstInvalid(): HTMLElement | null {
  const invalidControl = Object.entries(this.form.controls)
    .find(([, control]) => control.invalid)?.[0];
  return invalidControl ? document.getElementById(invalidControl) : null;
}
```

## ベストプラクティス
- labelと入力要素の関連付けを徹底する
- エラーはrole=alertなどで即座に読み上げる
- フォーカスをエラー先頭に移動し再入力を支援する

## 注意点
- aria属性の付けすぎで逆に混乱を招かないよう設計する
- 見た目だけでエラーを伝えず音声でも伝える
- フォーカス制御はSPA遷移との競合に注意

## 関連技術
- WCAG
- aria属性
- フォーカスマネジメント
