# #464 「ドラッグイベントの処理」

## 概要
ドラッグイベント処理ではpointerイベントを監視し、移動量を計算してホスト要素に反映しつつ、EventEmitterで外部へドラッグ情報を通知する。

## 学習目標
- pointerイベントを用いたドラッグ処理フローを理解する
- 移動量の計算とState更新を学ぶ
- EventEmitterで外部へドラッグ状態を通知する方法を把握する

## 技術ポイント
- pointerdownで初期位置を記録
- pointermoveで移動量を算出しtransformを更新
- pointerupでドラッグ終了と後始末

## 📺 画面表示用コード（動画用）
```typescript
@Output() dragMove = new EventEmitter<{ x: number; y: number }>();
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appDragHandle]',
  standalone: true
})
export class DragHandleDirective implements OnDestroy {
  @Output() dragMove = new EventEmitter<{ x: number; y: number }>();
  @Output() dragEnd = new EventEmitter<void>();

  private startX = 0;
  private startY = 0;
  private boundMove = this.onPointerMove.bind(this);
  private boundUp = this.onPointerUp.bind(this);

  @HostListener('pointerdown', ['$event'])
  onPointerDown(event: PointerEvent): void {
    event.preventDefault();
    this.startX = event.clientX;
    this.startY = event.clientY;
    document.addEventListener('pointermove', this.boundMove);
    document.addEventListener('pointerup', this.boundUp);
  }

  private onPointerMove(event: PointerEvent): void {
    const deltaX = event.clientX - this.startX;
    const deltaY = event.clientY - this.startY;
    this.dragMove.emit({ x: deltaX, y: deltaY });
  }

  private onPointerUp(): void {
    document.removeEventListener('pointermove', this.boundMove);
    document.removeEventListener('pointerup', this.boundUp);
    this.dragEnd.emit();
  }

  ngOnDestroy(): void {
    document.removeEventListener('pointermove', this.boundMove);
    document.removeEventListener('pointerup', this.boundUp);
  }
}
```

## ベストプラクティス
- EventEmitterで移動量を外部へ通知し、位置適用は利用側で制御
- リスナーをバインドした関数で保持し、後から確実に解除
- ドラッグ終了時に後処理（スナップや保存）を実行できるようイベントを提供

## 注意点
- pointerイベントはすべてのブラウザでサポートされているわけではないため対応状況を確認
- ドラッグ中は`preventDefault`でテキスト選択を防ぐ
- 長押しによるコンテキストメニューなどの副作用に留意

## 関連技術
- EventEmitter
- Pointer Events API
- Drag & Drop実装パターン
