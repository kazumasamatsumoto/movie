# #477 「ScrollSpy Directive - スクロール監視」

## 概要
ScrollSpyディレクティブはスクロール位置に応じて現在表示中のセクションを特定し、ナビゲーションをハイライトするための情報を提供する。

## 学習目標
- ScrollSpyの基本構造を理解する
- IntersectionObserverでセクションを監視する方法を学ぶ
- Outputイベントでアクティブセクションを通知する設計を把握する

## 技術ポイント
- Inputで監視対象セクションを登録
- IntersectionObserverで可視セクションを検知
- OutputでアクティブIDを通知

## 📺 画面表示用コード（動画用）
```typescript
@Output() sectionChange = new EventEmitter<string>();
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appScrollSpy]',
  standalone: true
})
export class ScrollSpyDirective implements OnInit, OnDestroy {
  @Input() spyTargets: NodeListOf<HTMLElement> | HTMLElement[] = [];
  @Output() sectionChange = new EventEmitter<string>();
  private observer?: IntersectionObserver;

  constructor(@Inject(PLATFORM_ID) private readonly platformId: Object) {}

  ngOnInit(): void {
    if (!isPlatformBrowser(this.platformId)) return;
    this.observer = new IntersectionObserver(entries => {
      const visible = entries
        .filter(entry => entry.isIntersecting)
        .sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];
      if (visible?.target) {
        const id = (visible.target as HTMLElement).id;
        if (id) this.sectionChange.emit(id);
      }
    }, { rootMargin: '-50% 0px -50% 0px', threshold: [0, 0.25, 0.5, 0.75, 1] });

    const targets = Array.isArray(this.spyTargets) ? this.spyTargets : Array.from(this.spyTargets);
    targets.forEach(target => this.observer?.observe(target));
  }

  ngOnDestroy(): void {
    this.observer?.disconnect();
  }
}
```

## ベストプラクティス
- rootMarginを設定し、セクション中央付近でアクティブ切り替え
- OutputでIDを通知しナビゲーションコンポーネントでハイライト
- Hash更新やスクロール位置同期と組み合わせてUX向上

## 注意点
- セクションが短い場合はthresholdを調整し検知精度を高める
- SSRでは監視できないためブラウザ判定を行う
- 高さが不安定な要素は高さ確定後に監視を開始

## 関連技術
- IntersectionObserver
- Router fragment/href
- Navigationコンポーネント
