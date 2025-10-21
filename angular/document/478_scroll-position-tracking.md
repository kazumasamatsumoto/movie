# #478 「スクロール位置の追跡」

## 概要
ScrollSpyでは表示中セクションを追跡する必要があり、IntersectionObserverやscrollイベントで位置を監視してアクティブセクションIDを更新する。

## 学習目標
- スクロール位置追跡の手法を理解する
- IntersectionObserverとscrollイベントの併用を学ぶ
- アクティブセクションの決定ロジックを把握する

## 技術ポイント
- 監視ターゲットのリストを指定
- IntersectionObserverがない場合のfallbackとしてscrollイベントを使用
- 最も表示領域が大きいセクションをアクティブとして選定

## 📺 画面表示用コード（動画用）
```typescript
entries.filter(e => e.isIntersecting).sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];
```

## 💻 詳細実装例（学習用）
```typescript
private handleScrollFallback(): void {
  const scrollTop = window.scrollY;
  const targets = document.querySelectorAll<HTMLElement>('[data-spy]');
  const current = Array.from(targets)
    .map(section => {
      const rect = section.getBoundingClientRect();
      return { id: section.id, offset: Math.abs(rect.top) };
    })
    .sort((a, b) => a.offset - b.offset)[0];
  if (current) {
    this.sectionChange.emit(current.id);
  }
}
```

## ベストプラクティス
- IntersectionObserverで実装し、非対応環境ではscrollイベントfallback
- section要素に`data-spy`やIDを必ず付与
- Debounceやthrottleでscrollイベント処理を最適化

## 注意点
- 高頻度のscrollイベントはパフォーマンスに影響するため最適化
- セクションの高さがダイナミックに変わる場合はリサイズ時に再計算
- ヘッダー固定の場合はoffsetを調整し正しい位置を検知

## 関連技術
- IntersectionObserver
- RxJS throttleTime
- Router fragment
