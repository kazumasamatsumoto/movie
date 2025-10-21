# #398 「アニメーションとの組み合わせ」

## 概要
Attribute Directiveを使うと特定のイベントでCSSクラスを切り替えたり、Angular Animation APIを呼び出してアニメーションを再利用しやすくできる。

## 学習目標
- アニメーションをディレクティブ化するメリットを理解する
- Renderer2でクラス切り替えによるCSSアニメーションを実装する方法を学ぶ
- Angular Animation APIとの連携を把握する

## 技術ポイント
- `renderer.addClass/removeClass`でトリガーを制御
- IntersectionObserverやスクロールイベントをディレクティブで管理
- `AnimationBuilder`をDIしてプログラム的にアニメーションを開始

## 📺 画面表示用コード（動画用）
```typescript
@Directive({ selector: '[appFadeOnHover]', standalone: true })
export class FadeOnHoverDirective {
  constructor(private readonly r: Renderer2, private readonly el: ElementRef<HTMLElement>) {}
  ngOnInit(): void {
    this.r.listen(this.el.nativeElement, 'mouseenter', () => this.r.addClass(this.el.nativeElement, 'is-fade'));
  }
}
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appRevealOnScroll]',
  standalone: true
})
export class RevealOnScrollDirective implements OnInit, OnDestroy {
  private observer?: IntersectionObserver;

  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2) {}

  ngOnInit(): void {
    this.renderer.addClass(this.el.nativeElement, 'is-hidden');
    this.observer = new IntersectionObserver(entries => {
      for (const entry of entries) {
        if (entry.isIntersecting) {
          this.renderer.addClass(this.el.nativeElement, 'is-revealed');
          this.renderer.removeClass(this.el.nativeElement, 'is-hidden');
          this.observer?.disconnect();
        }
      }
    }, { threshold: 0.2 });
    this.observer.observe(this.el.nativeElement);
  }

  ngOnDestroy(): void {
    this.observer?.disconnect();
  }
}
```

## ベストプラクティス
- CSSアニメーションクラスを定義し、ディレクティブはトリガーに専念
- IntersectionObserverなどネイティブAPIはブラウザチェックを行いPolyfillを検討
- 再利用したいアニメーションは`AnimationBuilder`で抽象化しテスト可能な形にする

## 注意点
- IntersectionObserverはSSRで動作しないので`isPlatformBrowser`でガード
- アニメーション中のクラス競合を避けるため命名を整理
- パフォーマンスに影響するアニメーションはGPUフレンドリーなプロパティを使用

## 関連技術
- Angular Animation API
- IntersectionObserver
- CSSトランジション/アニメーション
