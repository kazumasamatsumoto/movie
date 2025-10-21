# #315 「ngOnInit での初期化」

## 概要
`ngOnInit`はディレクティブの初期化タイミングであり、ホスト要素が利用可能になった後に副作用を安全に設定できる。

## 学習目標
- `ngOnInit`の呼ばれるタイミングを理解する
- 初期化処理をconstructorから分離する理由を把握する
- サービスや外部リソースとの連携をセットアップする

## 技術ポイント
- DIはconstructorで受け取り、処理は`ngOnInit`で行う
- DOM参照が必要な初期化は`ngOnInit`で安全に実行
- 非同期処理は`takeUntilDestroyed`などと組み合わせる

## 📺 画面表示用コード（動画用）
```typescript
@Directive({ selector: '[appLazyLoad]', standalone: true })
export class LazyLoadDirective implements OnInit {
  constructor(private readonly observer: LazyObserverService, private readonly el: ElementRef<HTMLElement>) {}
  ngOnInit(): void {
    this.observer.observe(this.el.nativeElement);
  }
}
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appLazyLoad]',
  standalone: true
})
export class LazyLoadDirective implements OnInit, OnDestroy {
  @Output() visible = new EventEmitter<void>();
  private disconnect?: () => void;

  constructor(
    private readonly el: ElementRef<HTMLElement>,
    private readonly observer: IntersectionObserverService,
    private readonly renderer: Renderer2
  ) {}

  ngOnInit(): void {
    this.disconnect = this.observer.observe(this.el.nativeElement, entry => {
      if (entry.isIntersecting) {
        this.visible.emit();
        this.renderer.addClass(this.el.nativeElement, 'is-visible');
      }
    });
  }

  ngOnDestroy(): void {
    this.disconnect?.();
  }
}
```

## ベストプラクティス
- constructorでは依存の注入だけ行い、DOMアクセスや副作用は`ngOnInit`へ移す
- 非同期購読は`takeUntilDestroyed`や解除関数を保持しリークを防ぐ
- Inputの初期値に依存する場合は`ngOnChanges`で初回呼び出しを確認する

## 注意点
- `ngOnInit`は一度しか呼ばれないため、再レンダリング時は別のフックを利用する
- SSRではDOM APIが存在しないので、必要ならブラウザ判定を行う
- 重い処理を同期で実行すると初期描画を阻害するため注意する

## 関連技術
- IntersectionObserver
- takeUntilDestroyed
- Renderer2
