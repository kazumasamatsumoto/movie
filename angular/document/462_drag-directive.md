# #462 「Drag Directive - ドラッグ」

## 概要
Dragディレクティブは要素をドラッグ可能にし、マウスやタッチ操作で位置を変更できるようにする。pointerイベントを利用してPC・モバイル両方に対応する。

## 学習目標
- ドラッグ操作の基本フローを理解する
- pointerdown/move/upイベントを利用した実装を学ぶ
- ドラッグ状態を外部へ通知する仕組みを把握する

## 技術ポイント
- `pointerdown`でドラッグ開始、`pointermove`で位置更新、`pointerup`で終了
- HostBindingでtransformを更新
- Outputでドラッグ位置を通知

## 📺 画面表示用コード（動画用）
```typescript
@HostListener('pointerdown', ['$event']) startDrag(event: PointerEvent) { ... }
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appDrag]',
  standalone: true
})
export class DragDirective implements OnDestroy {
  @HostBinding('style.userSelect') userSelect = 'none';
  @HostBinding('style.touchAction') touchAction = 'none';
  @HostBinding('style.transform') transform = 'translate(0px, 0px)';
  @Output() dragged = new EventEmitter<{ x: number; y: number }>();

  private dragging = false;
  private startX = 0;
  private startY = 0;
  private currentX = 0;
  private currentY = 0;

  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2) {}

  @HostListener('pointerdown', ['$event'])
  onPointerDown(event: PointerEvent): void {
    event.preventDefault();
    this.dragging = true;
    this.startX = event.clientX - this.currentX;
    this.startY = event.clientY - this.currentY;
    this.renderer.listen('document', 'pointermove', this.onPointerMove);
    this.renderer.listen('document', 'pointerup', this.onPointerUp);
  }

  private onPointerMove = (event: PointerEvent): void => {
    if (!this.dragging) return;
    this.currentX = event.clientX - this.startX;
    this.currentY = event.clientY - this.startY;
    this.transform = `translate(${this.currentX}px, ${this.currentY}px)`;
    this.dragged.emit({ x: this.currentX, y: this.currentY });
  };

  private onPointerUp = (): void => {
    this.dragging = false;
  };

  ngOnDestroy(): void {
    this.dragging = false;
  }
}
```

## ベストプラクティス
- Pointer Eventsを利用してマウス/タッチ対応を一元化
- transformを使いレイアウト破壊を防ぐ
- ドラッグ中は`user-select: none`でテキスト選択を抑制

## 注意点
- ドラッグステートのリスナーを確実に解除してリークを防止
- スクロールとドラッグが競合しないよう`touchAction`を設定
- ドラッグ領域の制限が必要な場合は境界チェックを実装

## 関連技術
- Pointer Events API
- Drag & Dropライブラリ
- Renderer2
