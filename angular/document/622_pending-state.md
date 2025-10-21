# #622 「pending - 検証中状態」

## 概要
pendingフラグは非同期バリデーションが完了していない状態を示し、送信抑制やローディング表示で重要な役割を持つ。

## 学習目標
- pendingが発生するタイミングを理解する
- 非同期バリデーションとの関係を学ぶ
- UX向上のための表示制御に活用する

## 技術ポイント
- AsyncValidator実行中はpending=true
- pending中はvalid/invalidが確定しない
- フォーム全体にもpending状態が伝播する

## 📺 画面表示用コード（動画用）
```html
<p *ngIf="control.pending">ユーザー名を確認中...</p>
```

## 💻 詳細実装例（学習用）
```typescript
protected watchStatus(): void {
  this.form.statusChanges.subscribe(status => {
    this.isChecking = status === 'PENDING';
  });
}

protected disableWhilePending(): boolean {
  return this.form.pending || this.isSubmitting;
}
```

## ベストプラクティス
- pending中はボタンを無効化し不正送信を防ぐ
- ローディング表示で検証中であることを伝える
- 非同期バリデーションのキャンセル処理を検討する

## 注意点
- 長時間pendingが続く場合はタイムアウトを設ける
- 複数の非同期バリデーションがある場合は状態を統合する
- pending状態を無視して送信するとサーバーエラーになる可能性がある

## 関連技術
- AsyncValidator
- statusChanges
- ローディングUI
