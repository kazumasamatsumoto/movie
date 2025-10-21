# #459 「LazyLoad Directive - 遅延読み込み」

## 概要
LazyLoadディレクティブは画像やコンテンツをビューポートに入ったタイミングで読み込み、初期ロードを軽量化する。IntersectionObserverが主要な実装手段となる。

## 学習目標
- LazyLoadディレクティブの基本構造を理解する
- IntersectionObserverによる遅延読み込みの仕組みを学ぶ
- プレースホルダー表示やエラーハンドリングを組み込む

## 技術ポイント
- `IntersectionObserver`で要素の可視状態を監視
- Inputで本来のsrcやコンテンツURLを受け取る
- 観測後はObserverを解除して不要な処理を省く

## 📺 画面表示用コード（動画用）
```typescript
@Input() appLazyLoad = '';
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appLazyLoad]',
  standalone: true
})
export class LazyLoadDirective implements OnInit, OnDestroy {
  @Input() appLazyLoad = '';
  @Input() placeholder = '';

  private observer?: IntersectionObserver;

  constructor(
    private readonly el: ElementRef<HTMLImageElement>,
    @Inject(PLATFORM_ID) private readonly platformId: Object
  ) {}

  ngOnInit(): void {
    if (!isPlatformBrowser(this.platformId)) return;
    if (this.placeholder) {
      this.el.nativeElement.src = this.placeholder;
    }
    this.observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          this.el.nativeElement.src = this.appLazyLoad;
          this.observer?.disconnect();
        }
      });
    }, { rootMargin: '100px' });
    this.observer.observe(this.el.nativeElement);
  }

  ngOnDestroy(): void {
    this.observer?.disconnect();
  }
}
```

## ベストプラクティス
- rootMarginを設定し、少し早めにロード開始
- プレースホルダー画像や`loading="lazy"`と併用
- エラー時のフォールバック画像を設定

## 注意点
- `loading="lazy"`対応ブラウザでは組み合わせを検討
- IntersectionObserver未対応環境ではPolyfillを用意
- コンポーネント破棄時に必ずdisconnectしメモリリークを防ぐ

## 関連技術
- IntersectionObserver
- Loading属性
- Web Performance最適化
