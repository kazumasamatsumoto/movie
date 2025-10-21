# #469 「要素のサイズ変更」

## 概要
要素のサイズ変更ではドラッグ距離を計算してwidth/heightを更新し、境界条件（min/max）を満たすよう制限する。レイアウト崩れを防ぐために`box-sizing`の考慮も必要。

## 学習目標
- ドラッグ距離からサイズを算出する方法を理解する
- min/max制約の適用方法を学ぶ
- `box-sizing`やpaddingの影響を考慮した実装を把握する

## 技術ポイント
- ドラッグ開始時の幅とポインタ座標を記録
- 移動量を加算して制限範囲内の幅/高さに設定
- `box-sizing: border-box`を活用し計算を簡略化

## 📺 画面表示用コード（動画用）
```typescript
this.width = Math.min(this.maxWidth, Math.max(this.minWidth, this.startWidth + deltaX));
```

## 💻 詳細実装例（学習用）
```typescript
private updateSize(deltaX: number, deltaY: number): void {
  const newWidth = this.startWidth + deltaX;
  const newHeight = this.startHeight + deltaY;
  this.width = Math.min(this.maxWidth, Math.max(this.minWidth, newWidth));
  this.height = Math.min(this.maxHeight, Math.max(this.minHeight, newHeight));
}
```

## ベストプラクティス
- `box-sizing: border-box`でpaddingやborderを含めて計算
- 双方向バインディングが必要ならOutputでサイズ変更イベントを発火
- 変更中はtransformやoutlineで視覚的フィードバックを提供

## 注意点
- CSS GridやFlexbox要素はサイズ変更に制約があるためレイアウトを確認
- 最小サイズを下回った場合の挙動を明確に（固定する、スナップする等）
- リサイズ中にテキスト選択が起きないよう`user-select: none`を設定

## 関連技術
- ResizableDirective
- CSS box-sizing
- Dragイベント処理
