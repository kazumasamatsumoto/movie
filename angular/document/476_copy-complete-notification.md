# #476 「コピー完了の通知」

## 概要
コピー完了通知はユーザーがコピー操作の成否を即座に把握できるよう、TooltipやSnackbar、Outputイベントを利用してフィードバックを表示する。

## 学習目標
- コピーディレクティブから成功/失敗情報を取得する方法を理解する
- 成否に応じたUIフィードバック（メッセージ・アイコン）を学ぶ
- 通知表示の寿命やアクセシビリティを考慮した実装を把握する

## 技術ポイント
- Output`(copied)`イベントで成否を受信
- SnackbarやToastサービスを呼び出す
- ARIAライブリージョンで音声ユーザーにも通知

## 📺 画面表示用コード（動画用）
```html
<button appCopyToClipboard="text" (copied)="showToast($event)">コピー</button>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-copy-toast',
  standalone: true,
  imports: [CommonModule, CopyToClipboardDirective],
  template: `
    <button appCopyToClipboard="Angular Rocks!" (copied)="notify($event)">コピー</button>
    <div aria-live="polite">{{ message }}</div>
  `
})
export class CopyToastComponent {
  protected message = '';

  protected notify(success: boolean): void {
    this.message = success ? 'コピーしました ✅' : 'コピーに失敗しました ❌';
    setTimeout(() => (this.message = ''), 2000);
  }
}
```

## ベストプラクティス
- Snackbar/Toastコンポーネントを利用し視覚的にフィードバック
- ARIAライブリージョンでスクリーンリーダーにも通知
- 短時間でメッセージを消すか、再コピーで上書きする

## 注意点
- 成功/失敗どちらもハンドリングを実装しないと無反応になる
- 同一要素で連続コピーする際はメッセージが積み重ならないよう管理
- 通知が過剰になるとUXを損なうため要件に応じて調整

## 関連技術
- CopyToClipboardDirective
- Snackbar/Toastサービス
- ARIAライブリージョン
