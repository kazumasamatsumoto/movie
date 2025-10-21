# #447 「ClickOutside Directive - 外部クリック検知」

## 概要
ClickOutsideディレクティブはホスト要素の外側で発生したクリックやタッチを検知し、モーダルやドロップダウンを閉じる処理を共通化できる。

## 学習目標
- 外側クリック検知の基本パターンを理解する
- HostListenerでdocumentイベントを監視する方法を学ぶ
- EventEmitterで外部へ通知する設計を把握する

## 技術ポイント
- `@HostListener('document:click', ['$event'])`
- `event.target`がホスト要素内か判定
- Outputで閉じるイベントを通知

## 📺 画面表示用コード（動画用）
```typescript
@HostListener('document:click', ['$event']) handleClick(event: MouseEvent) { if (!this.el.nativeElement.contains(event.target)) this.clickedOutside.emit(); }
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appClickOutside]',
  standalone: true
})
export class ClickOutsideDirective {
  @Output() appClickOutside = new EventEmitter<void>();

  constructor(private readonly el: ElementRef<HTMLElement>) {}

  @HostListener('document:click', ['$event'])
  onDocumentClick(event: MouseEvent): void {
    if (!this.el.nativeElement.contains(event.target as Node)) {
      this.appClickOutside.emit();
    }
  }

  @HostListener('document:touchstart', ['$event'])
  onDocumentTouch(event: TouchEvent): void {
    if (!this.el.nativeElement.contains(event.target as Node)) {
      this.appClickOutside.emit();
    }
  }
}
```

## ベストプラクティス
- documentイベントを使う場合は`contains`で内部クリックを除外
- タッチイベントとクリックイベント両方に対応
- Outputで閉じる処理を外部へ委譲し、再利用性を高める

## 注意点
- SSRではdocumentが存在しないためガードが必要
- 同じページに複数ディレクティブがあるときはイベント順序に注意
- モーダル内でクリックが必要な場合は`stopPropagation`を適切に設定

## 関連技術
- HostListener
- EventEmitter
- Overlay/Modalコンポーネント
