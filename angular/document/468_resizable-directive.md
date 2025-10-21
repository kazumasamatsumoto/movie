# #468 「Resizable Directive - リサイズ」

## 概要
Resizableディレクティブは要素にリサイズハンドルを追加し、ドラッグ操作で幅や高さを変更できるようにする。最小・最大サイズや方向制限をInputで設定できる。

## 学習目標
- リサイズディレクティブの構造を理解する
- ハンドルを生成しドラッグでサイズを変更する方法を学ぶ
- 制約（min/max）や方向オプションの設計を把握する

## 技術ポイント
- Renderer2でハンドル要素を追加
- pointerイベントでサイズを更新
- HostBindingでwidth/heightを更新またはstyle操作

## 📺 画面表示用コード（動画用）
```typescript
@HostBinding('style.width.px') width = 300;
@HostBinding('style.height.px') height = 200;
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appResizable]',
  standalone: true
})
export class ResizableDirective implements OnInit, OnDestroy {
  @Input() minWidth = 150;
  @Input() minHeight = 100;
  @Input() maxWidth = Infinity;
  @Input() maxHeight = Infinity;

  @HostBinding('style.position') position = 'relative';
  @HostBinding('style.width.px') width = 300;
  @HostBinding('style.height.px') height = 200;

  private handle!: HTMLElement;
  private startX = 0;
  private startY = 0;
  private startWidth = 0;
  private startHeight = 0;

  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2) {}

  ngOnInit(): void {
    this.handle = this.renderer.createElement('span');
    this.renderer.addClass(this.handle, 'resize-handle');
    this.renderer.setStyle(this.handle, 'position', 'absolute');
    this.renderer.setStyle(this.handle, 'right', '0');
    this.renderer.setStyle(this.handle, 'bottom', '0');
    this.renderer.setStyle(this.handle, 'width', '12px');
    this.renderer.setStyle(this.handle, 'height', '12px');
    this.renderer.setStyle(this.handle, 'cursor', 'nwse-resize');
    this.renderer.appendChild(this.el.nativeElement, this.handle);
    this.handle.addEventListener('pointerdown', this.onPointerDown);
  }

  private onPointerDown = (event: PointerEvent): void => {
    event.preventDefault();
    this.startX = event.clientX;
    this.startY = event.clientY;
    this.startWidth = this.width;
    this.startHeight = this.height;
    document.addEventListener('pointermove', this.onPointerMove);
    document.addEventListener('pointerup', this.onPointerUp);
  };

  private onPointerMove = (event: PointerEvent): void => {
    const deltaX = event.clientX - this.startX;
    const deltaY = event.clientY - this.startY;
    this.width = Math.min(this.maxWidth, Math.max(this.minWidth, this.startWidth + deltaX));
    this.height = Math.min(this.maxHeight, Math.max(this.minHeight, this.startHeight + deltaY));
  };

  private onPointerUp = (): void => {
    document.removeEventListener('pointermove', this.onPointerMove);
    document.removeEventListener('pointerup', this.onPointerUp);
  };

  ngOnDestroy(): void {
    this.handle.removeEventListener('pointerdown', this.onPointerDown);
    document.removeEventListener('pointermove', this.onPointerMove);
    document.removeEventListener('pointerup', this.onPointerUp);
  }
}
```

## ベストプラクティス
- ハンドルをRenderer2で生成しコンポーネントテンプレートを汚さない
- 最小/最大サイズをInputで設定し予期しないサイズにならないよう制限
- CSSでハンドルの見た目やアニメーションを設定しUX向上

## 注意点
- リサイズとスクロールが干渉しないよう`pointer-events`や`touch-action`を設定
- モバイルではリサイズ操作が難しいためデバイス別のUIを提供
- ハンドル追加によるレイアウト変化に注意し、positionをrelativeなどに設定

## 関連技術
- Renderer2
- Pointer Events
- Drag & Resizeライブラリ
