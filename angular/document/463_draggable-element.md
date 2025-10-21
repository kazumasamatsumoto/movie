# #463 「ドラッグ可能要素の実装」

## 概要
ドラッグ可能要素はドラッグ中にtransformなどで位置を更新し、開始・終了位置を保持することでスムーズな移動を実現する。Inputで初期位置や制限を設定できる。

## 学習目標
- transformを用いた位置更新の手法を理解する
- 初期位置や制限をInputで受け取る方法を学ぶ
- ドラッグ状態をアニメーションで表示するテクニックを把握する

## 技術ポイント
- `translate(x, y)`で位置を更新
- `@Input() bounds`で移動範囲を制限
- CSSでドラッグ中の影やカーソルを変更

## 📺 画面表示用コード（動画用）
```typescript
@HostBinding('style.transform') transform = `translate(${this.x}px, ${this.y}px)`;
```

## 💻 詳細実装例（学習用）
```typescript
interface Bounds {
  minX: number;
  maxX: number;
  minY: number;
  maxY: number;
}

@Directive({
  selector: '[appDraggable]',
  standalone: true
})
export class DraggableDirective {
  @Input() bounds?: Bounds;
  @HostBinding('class.is-dragging') dragging = false;
  @HostBinding('style.transform') transform = 'translate(0px, 0px)';

  private startX = 0;
  private startY = 0;
  private positionX = 0;
  private positionY = 0;

  @HostListener('pointerdown', ['$event'])
  onPointerDown(event: PointerEvent): void {
    event.preventDefault();
    this.dragging = true;
    this.startX = event.clientX - this.positionX;
    this.startY = event.clientY - this.positionY;
    document.addEventListener('pointermove', this.onPointerMove);
    document.addEventListener('pointerup', this.onPointerUp);
  }

  private onPointerMove = (event: PointerEvent): void => {
    if (!this.dragging) return;
    let x = event.clientX - this.startX;
    let y = event.clientY - this.startY;
    if (this.bounds) {
      x = Math.max(this.bounds.minX, Math.min(x, this.bounds.maxX));
      y = Math.max(this.bounds.minY, Math.min(y, this.bounds.maxY));
    }
    this.positionX = x;
    this.positionY = y;
    this.transform = `translate(${this.positionX}px, ${this.positionY}px)`;
  };

  private onPointerUp = (): void => {
    this.dragging = false;
    document.removeEventListener('pointermove', this.onPointerMove);
    document.removeEventListener('pointerup', this.onPointerUp);
  };
}
```

## ベストプラクティス
- 移動範囲をInputで制御し、ユーザー操作を予測可能に
- transformを使用しパフォーマンスとレイアウト維持を両立
- CSSで`cursor: grab`/`grabbing`を設定し操作性を高める

## 注意点
- ドラッグ中は`pointer-events`や`user-select`に留意し意図しない動作を防ぐ
- モバイル端末ではスクロールと衝突するため適宜`touch-action`を設定
- ドラッグ終了時に必ずリスナーを解除しリークを防ぐ

## 関連技術
- DragDirective
- CSS transform
- Pointer Events
