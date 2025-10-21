# #611 「submit ボタンの実装」

## 概要
送信ボタンはtype=submitでformタグと連携し、フォーム状態に応じて活性・非活性やラベルの切り替えを行う。

## 学習目標
- submitボタンの基本的な役割を理解する
- フォーム状態とボタンの活性制御を学ぶ
- UX向上のためのフィードバック手法を把握する

## 技術ポイント
- type=submitでngSubmitと連動
- [disabled]でform.invalidやisSubmittingを反映
- aria-liveで状態変化をスクリーンリーダーに伝達

## 📺 画面表示用コード（動画用）
```html
<button type="submit" [disabled]="form.invalid || isSubmitting">
  {{ isSubmitting ? '送信中...' : '送信' }}
</button>
```

## 💻 詳細実装例（学習用）
```typescript
protected isSubmitting = false;

protected async onSubmit(): Promise<void> {
  if (this.form.invalid) {
    return;
  }
  this.isSubmitting = true;
  try {
    await this.save(this.form.value);
  } finally {
    this.isSubmitting = false;
  }
}

private save(value: unknown): Promise<void> {
  return this.userService.update(value);
}
```

## ベストプラクティス
- 送信中はボタンを無効化して二重送信を防ぐ
- 状態に応じてラベルやアイコンを切り替えユーザーに通知する
- キーボード操作でアクセスできる位置に配置する

## 注意点
- buttonにtypeを指定しないとデフォルトsubmitで予期せぬ挙動になる
- form外にボタンを置くとngSubmitが動かない
- ローディング中に例外が起きた場合に再度有効化する処理を忘れない

## 関連技術
- HTMLButtonElement
- ngSubmit
- 状態管理
