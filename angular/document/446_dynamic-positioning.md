# #446 「位置の動的調整」

## 概要
Tooltipの位置を動的に調整するには、ホスト要素のBoundingClientRectを取得し、placementオプションとviewport境界を考慮して位置を計算する。

## 学習目標
- Tooltip位置計算の基本を理解する
- placementオプションに応じた座標計算を学ぶ
- viewport外に出ないよう補正する手法を把握する

## 技術ポイント
- `getBoundingClientRect()`で座標取得
- `clientWidth/Height`でTooltipサイズを取得
- viewport超過時に反転やオフセット調整

## 📺 画面表示用コード（動画用）
```typescript
const host = this.el.nativeElement.getBoundingClientRect();
const tooltip = this.tooltip!.getBoundingClientRect();
```

## 💻 詳細実装例（学習用）
```typescript
private setPosition(placement: 'top' | 'bottom' | 'left' | 'right', offset: number): void {
  if (!this.tooltip) return;
  const host = this.el.nativeElement.getBoundingClientRect();
  const tip = this.tooltip.getBoundingClientRect();
  const viewportWidth = window.innerWidth;
  const viewportHeight = window.innerHeight;
  let top = 0;
  let left = 0;
  switch (placement) {
    case 'bottom':
      top = host.bottom + offset;
      left = host.left + host.width / 2 - tip.width / 2;
      break;
    case 'left':
      top = host.top + host.height / 2 - tip.height / 2;
      left = host.left - tip.width - offset;
      break;
    case 'right':
      top = host.top + host.height / 2 - tip.height / 2;
      left = host.right + offset;
      break;
    default:
      top = host.top - tip.height - offset;
      left = host.left + host.width / 2 - tip.width / 2;
  }
  top = Math.max(0, Math.min(top, viewportHeight - tip.height));
  left = Math.max(0, Math.min(left, viewportWidth - tip.width));
  this.renderer.setStyle(this.tooltip, 'top', `${top}px`);
  this.renderer.setStyle(this.tooltip, 'left', `${left}px`);
}
```

## ベストプラクティス
- placementオプションとoffsetをInputで受け取り柔軟に
- viewport境界で反転/補正し、表示が途切れないようにする
- スクロール時の再計算やレスポンシブ対応を検討

## 注意点
- ページスクロールで位置がズレるため`position: fixed`を利用
- スクロールコンテナ内の場合は`position: absolute`＋親要素基準で計算
- 高頻度で再計算するとパフォーマンスに影響するので最適化

## 関連技術
- IntersectionObserver
- ResizeObserver
- Tooltipライブラリの配置ロジック
