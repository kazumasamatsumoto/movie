# #460 「画像の遅延ロード」

## 概要
画像の遅延ロードではIntersectionObserverで画像要素を監視し、表示領域に入ったら`src`属性を設定してダウンロードを開始する。placeholderやフェードイン演出も付与できる。

## 学習目標
- 画像遅延ロードの具体的な実装を理解する
- プレースホルダーと実画像の切り替え方法を学ぶ
- ネットワークパフォーマンスを向上させる利点を把握する

## 技術ポイント
- `data-src`などで本来のURLを保持
- IntersectionObserverで表示タイミングを検知
- `loading="lazy"`と組み合わせてブラウザネイティブ機能も利用

## 📺 画面表示用コード（動画用）
```html
<img appLazyLoad [appLazyLoad]="imageUrl" placeholder="assets/placeholder.jpg" />
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: 'img[appLazyLoad]',
  standalone: true
})
export class ImageLazyLoadDirective implements OnInit, OnDestroy {
  @Input() appLazyLoad = '';
  @Input() placeholder = '';
  @Input() fadeIn = true;
  private observer?: IntersectionObserver;

  constructor(
    private readonly el: ElementRef<HTMLImageElement>,
    @Inject(PLATFORM_ID) private readonly platformId: Object
  ) {}

  ngOnInit(): void {
    if (!isPlatformBrowser(this.platformId)) return;
    const img = this.el.nativeElement;
    if (this.placeholder) {
      img.src = this.placeholder;
    }
    if (this.fadeIn) {
      img.style.transition = 'opacity .3s ease';
      img.style.opacity = '0';
    }
    this.observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          img.src = this.appLazyLoad;
          img.onload = () => {
            if (this.fadeIn) {
              img.style.opacity = '1';
            }
          };
          this.observer?.disconnect();
        }
      });
    }, { rootMargin: '200px 0px' });
    this.observer.observe(img);
  }

  ngOnDestroy(): void {
    this.observer?.disconnect();
  }
}
```

## ベストプラクティス
- placeholderでローディング中の視覚的空白を防ぐ
- rootMarginを大きめにして早めにロード開始し、スクロール時のちらつきを防止
- onloadでフェードイン演出を加えるとUXが向上

## 注意点
- SSRでは画像のsrcが設定されずプレースホルダーのみになるため、必要に応じプリレンダリングを考慮
- IntersectionObserver未対応環境ではPolyfillが必要
- エラー時のfallback画像を検討

## 関連技術
- IntersectionObserver
- loading="lazy"
- WebP/AVIF対応でさらに最適化
