# #475 「クリックでコピー」

## 概要
クリックでコピーする実装はHostListenerでクリックを検知し、Clipboard APIを呼び出してテキストをコピーする。ボタンやアイコンに適用して簡単にコピー機能を提供できる。

## 学習目標
- クリックイベントとコピー処理の連携を理解する
- Clipboard API使用時のPromise処理を学ぶ
- コピー後のUIフィードバックを設計する方法を把握する

## 技術ポイント
- HostListenerでクリックを捕捉
- `navigator.clipboard.writeText`
- Outputで成功/失敗を通知

## 📺 画面表示用コード（動画用）
```html
<button appCopyToClipboard="https://example.com" (copied)="notify($event)">リンクをコピー</button>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-copy-button',
  standalone: true,
  imports: [CommonModule, CopyToClipboardDirective],
  template: `
    <button appCopyToClipboard="https://angular.dev" (copied)="notify($event)">URLをコピー</button>
    <span *ngIf="lastResult === true">コピーしました</span>
    <span *ngIf="lastResult === false">コピーに失敗しました</span>
  `
})
export class CopyButtonComponent {
  protected lastResult: boolean | null = null;
  protected notify(result: boolean): void {
    this.lastResult = result;
  }
}
```

## ベストプラクティス
- コピー成功時にTooltipやSnackbarで結果を伝える
- コピー文字列はInputで受け取り、ボタン内にセキュアな値を埋め込まない
- 同じボタンを連続クリックした際のステートリセットを考慮

## 注意点
- Clipboard APIはユーザー操作のコンテキスト内で呼び出す必要がある
- 失敗時は例外が発生するためエラーハンドリングを必ず実装
- クリップボードへ機微情報をコピーする際は慎重に扱う

## 関連技術
- Clipboard API
- Toast/Snackbar
- Tooltipsによるフィードバック
