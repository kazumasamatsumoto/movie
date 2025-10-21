# #461 「Intersection Observer の活用」

## 概要
IntersectionObserverは要素とビューポートの交差状態を非同期に監視するAPIで、LazyLoadやInfiniteScrollなどスクロール系ディレクティブの基盤となる。

## 学習目標
- IntersectionObserverの仕組みと使い方を理解する
- root/rootMargin/thresholdなどの設定項目を学ぶ
- 監視開始・解除のタイミング管理を把握する

## 技術ポイント
- `new IntersectionObserver(callback, options)`
- `observer.observe(element)` / `observer.disconnect()`
- rootMarginで予測ロード、thresholdで検知精度を調整

## 📺 画面表示用コード（動画用）
```typescript
const observer = new IntersectionObserver(entries => { ... }, { rootMargin: '100px' });
observer.observe(this.el.nativeElement);
```

## 💻 詳細実装例（学習用）
```typescript
private setupObserver(): void {
  this.observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        this.loadContent();
        this.observer?.disconnect();
      }
    });
  }, { root: null, rootMargin: '120px', threshold: 0 });
  this.observer.observe(this.el.nativeElement);
}
```

## ベストプラクティス
- rootMarginを活用して早めにイベントを発火させユーザー体験を改善
- 監視が不要になったら`disconnect()`で停止
- Observer生成は1回にし、複数要素をまとめて監視することで性能向上

## 注意点
- 古いブラウザでは未対応のためPolyfillが必要
- rootにスクロールコンテナを指定する場合はレイアウトを考慮
- 監視対象が頻繁に入れ替わる場合は`unobserve`で適切に管理

## 関連技術
- LazyLoadDirective
- InfiniteScrollDirective
- ResizeObserver
