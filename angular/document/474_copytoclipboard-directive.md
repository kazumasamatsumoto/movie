# #474 「CopyToClipboard Directive - クリップボード」

## 概要
CopyToClipboardディレクティブはクリックなどの操作で指定したテキストをクリップボードへコピーし、完了イベントを通知してユーザーへフィードバックを与える。

## 学習目標
- Clipboard APIを利用したコピー処理を理解する
- HostListenerでクリックを検知しコピーする実装を学ぶ
- コピー結果をOutputで通知しUIに反映する方法を把握する

## 技術ポイント
- `navigator.clipboard.writeText(text)`
- HTTPS環境でのみ動作するため注意
- FallbackとしてexecCommandを検討

## 📺 画面表示用コード（動画用）
```typescript
@HostListener('click') async copy(): Promise<void> { await navigator.clipboard.writeText(this.text); }
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appCopyToClipboard]',
  standalone: true
})
export class CopyToClipboardDirective {
  @Input('appCopyToClipboard') text = '';
  @Output() copied = new EventEmitter<boolean>();

  @HostListener('click')
  async onClick(): Promise<void> {
    if (!this.text) return;
    try {
      await navigator.clipboard.writeText(this.text);
      this.copied.emit(true);
    } catch (error) {
      console.error('copy failed', error);
      this.copied.emit(false);
    }
  }
}
```

## ベストプラクティス
- コピー成功/失敗をOutputで通知し、ユーザーへフィードバックを表示
- Clipboard API非対応環境に備え、fallbackを実装するか警告を表示
- Inputでコピー文字列を受け取り、テンプレートを簡潔に保つ

## 注意点
- Clipboard APIはHTTPSまたはlocalhostでのみ動作する
- 同期的に呼び出せずPromiseなのでエラーハンドリングが必要
- 大量のテキストやバイナリコピーはブラウザごとに制約がある

## 関連技術
- Clipboard API
- EventEmitter
- Toast/Tooltipによる通知
