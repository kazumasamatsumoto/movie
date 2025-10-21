# #456 「InfiniteScroll Directive - 無限スクロール」

## 概要
InfiniteScrollディレクティブはスクロール末尾に到達した際に追加データを読み込むイベントを発生させ、リストの自動拡張を実現する。

## 学習目標
- 無限スクロールの基本挙動と構造を理解する
- IntersectionObserverやスクロールイベントを用いた検知手法を学ぶ
- Outputイベントでデータ読み込みをトリガーする設計を把握する

## 技術ポイント
- Sentinel要素を監視するIntersectionObserver
- Inputでオフセットや無効化フラグを受け取る
- Outputで`loadMore`イベントを通知

## 📺 画面表示用コード（動画用）
```typescript
@Output() scrolled = new EventEmitter<void>();
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appInfiniteScroll]',
  standalone: true
})
export class InfiniteScrollDirective implements OnInit, OnDestroy {
  @Input() disabled = false;
  @Input() rootMargin = '0px 0px 200px 0px';
  @Output() scrolled = new EventEmitter<void>();

  private observer?: IntersectionObserver;
  private sentinel!: HTMLElement;

  constructor(
    private readonly el: ElementRef<HTMLElement>,
    private readonly renderer: Renderer2,
    @Inject(PLATFORM_ID) private readonly platformId: Object
  ) {}

  ngOnInit(): void {
    if (!isPlatformBrowser(this.platformId)) return;
    this.sentinel = this.renderer.createElement('div');
    this.renderer.setStyle(this.sentinel, 'width', '100%');
    this.renderer.setStyle(this.sentinel, 'height', '1px');
    this.renderer.appendChild(this.el.nativeElement, this.sentinel);

    this.observer = new IntersectionObserver(entries => {
      if (this.disabled) return;
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          this.scrolled.emit();
        }
      });
    }, { root: this.el.nativeElement, rootMargin: this.rootMargin });

    this.observer.observe(this.sentinel);
  }

  ngOnDestroy(): void {
    this.observer?.disconnect();
  }
}
```

## ベストプラクティス
- IntersectionObserverを用いてパフォーマンスを向上
- Inputで無効化できるようにし、読み込み中はイベントを抑制
- Sentinel要素を使い、余計なスクロールイベントを避ける

## 注意点
- 古いブラウザではIntersectionObserverをPolyfill
- リストが短くてすぐ末尾になる場合は初期読み込みを考慮
- データ読み込み中に複数回イベントが発火しないようガード

## 関連技術
- IntersectionObserver
- RxJS merge/concatMapでAPI呼び出し
- スクロールコンテナ設計
