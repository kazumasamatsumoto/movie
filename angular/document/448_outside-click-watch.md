# #448 「要素外クリックの監視」

## 概要
要素外クリックを監視して操作を抑止するには、`document`レベルのイベントを監視し、クリック対象がホスト要素内か判定する。

## 学習目標
- `contains`メソッドを用いた外部クリック判定を理解する
- フォーカスやタッチイベントへの拡張方法を学ぶ
- デバイスごとの挙動を意識した実装を把握する

## 技術ポイント
- `this.el.nativeElement.contains(event.target)`
- documentクリックとdocumentタッチの両方を監視
- Outputイベントで結果を通知

## 📺 画面表示用コード（動画用）
```typescript
if (!this.el.nativeElement.contains(event.target as Node)) this.clickedOutside.emit();
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appOutsideWatcher]',
  standalone: true
})
export class OutsideWatcherDirective {
  @Output() outside = new EventEmitter<Event>();

  constructor(private readonly el: ElementRef<HTMLElement>) {}

  @HostListener('document:click', ['$event'])
  onDocumentClick(event: MouseEvent): void {
    if (!this.el.nativeElement.contains(event.target as Node)) {
      this.outside.emit(event);
    }
  }

  @HostListener('document:focusin', ['$event'])
  onDocumentFocus(event: FocusEvent): void {
    if (!this.el.nativeElement.contains(event.target as Node)) {
      this.outside.emit(event);
    }
  }
}
```

## ベストプラクティス
- ドロップダウン内部でクリックしても閉じないよう`contains`判定を正しく行う
- フォーカス移動にも対応し、キーボード操作で閉じるシナリオもカバー
- EventEmitterで外部へイベント情報を渡し、利用側で処理を決定

## 注意点
- documentイベントを解除し忘れるとメモリリークを招く（Angularが自動解除するが意識しておく）
- Shadow DOM内の要素の場合は`composedPath`を確認する必要がある
- 非同期処理で閉じる場合は競合しないよう状態管理する

## 関連技術
- EventEmitter
- Overlay/Modal設計
- Shadow DOM
