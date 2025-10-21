# #470 「リサイズハンドルの実装」

## 概要
リサイズハンドルは要素の角や辺に配置された小さなドラッグ領域で、pointerイベントを利用してサイズ変更の起点として機能する。

## 学習目標
- ハンドル要素の生成と配置方法を理解する
- ハンドル種別（右、下、角）に応じたサイズ計算を学ぶ
- 複数ハンドルを管理し、ユーザー操作を直感的にする方法を把握する

## 技術ポイント
- Renderer2でハンドルを追加してCSSでスタイリング
- ハンドルごとにドラッグ方向を判定
- pointerイベントでサイズ更新を委譲

## 📺 画面表示用コード（動画用）
```typescript
const handle = this.renderer.createElement('span');
this.renderer.addClass(handle, `resize-handle-${direction}`);
```

## 💻 詳細実装例（学習用）
```typescript
private createHandle(direction: 'right' | 'bottom' | 'corner'): void {
  const handle = this.renderer.createElement('span');
  this.renderer.addClass(handle, 'resize-handle');
  this.renderer.addClass(handle, `resize-handle-${direction}`);
  this.renderer.appendChild(this.el.nativeElement, handle);
  handle.addEventListener('pointerdown', (event: PointerEvent) => this.beginResize(event, direction));
}

private beginResize(event: PointerEvent, direction: string): void {
  event.preventDefault();
  this.startX = event.clientX;
  this.startY = event.clientY;
  this.startWidth = this.width;
  this.startHeight = this.height;
  this.currentDirection = direction;
  document.addEventListener('pointermove', this.onPointerMove);
  document.addEventListener('pointerup', this.onPointerUp);
}

private onPointerMove = (event: PointerEvent): void => {
  const deltaX = event.clientX - this.startX;
  const deltaY = event.clientY - this.startY;
  if (this.currentDirection === 'right' || this.currentDirection === 'corner') {
    this.width = Math.max(this.minWidth, Math.min(this.maxWidth, this.startWidth + deltaX));
  }
  if (this.currentDirection === 'bottom' || this.currentDirection === 'corner') {
    this.height = Math.max(this.minHeight, Math.min(this.maxHeight, this.startHeight + deltaY));
  }
};
```

## ベストプラクティス
- ハンドル方向をInputで制御し、必要な方向だけを有効化
- CSSでハンドルを視覚的にわかりやすくし、カーソルを変更
- リサイズ中は余計なテキスト選択を防ぐ設定を行う

## 注意点
- ハンドル追加によってレイアウトが崩れないようpositionを相対化
- イベントをbaseクラスで共有しハンドルが複数でも管理可能にする
- モバイルではハンドルが小さいと操作しにくいのでサイズ調整

## 関連技術
- ResizableDirective
- Pointer Events
- CSS styling
