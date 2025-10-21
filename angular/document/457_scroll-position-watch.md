# #457 「スクロール位置の監視」

## 概要
無限スクロールやScrollSpyではスクロール位置を監視し、末尾到達やセクション表示を検知する。IntersectionObserverやscrollイベントを活用する。

## 学習目標
- スクロール位置の監視手法を理解する
- IntersectionObserverとscrollイベントの使い分けを学ぶ
- スロットリング・デバウンスでパフォーマンスを確保する

## 技術ポイント
- IntersectionObserverで末尾監視
- scrollイベントで`scrollTop + clientHeight`を計算
- RxJS `throttleTime`で更新頻度を制御

## 📺 画面表示用コード（動画用）
```typescript
const atBottom = container.scrollTop + container.clientHeight >= container.scrollHeight - threshold;
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appScrollWatcher]',
  standalone: true
})
export class ScrollWatcherDirective implements OnInit, OnDestroy {
  @Input() threshold = 16;
  @Output() reachBottom = new EventEmitter<void>();
  private destroy$ = new Subject<void>();

  constructor(private readonly el: ElementRef<HTMLElement>) {}

  ngOnInit(): void {
    fromEvent(this.el.nativeElement, 'scroll')
      .pipe(
        throttleTime(100),
        takeUntil(this.destroy$)
      )
      .subscribe(() => {
        const target = this.el.nativeElement;
        if (target.scrollTop + target.clientHeight >= target.scrollHeight - this.threshold) {
          this.reachBottom.emit();
        }
      });
  }

  ngOnDestroy(): void {
    this.destroy$.next();
    this.destroy$.complete();
  }
}
```

## ベストプラクティス
- IntersectionObserverが使える場合はそちらを優先しパフォーマンスを向上
- scrollイベント使用時はスロットリングで負荷を軽減
- thresholdを調整して少し早めにデータ読み込みを行う

## 注意点
- ネイティブscrollイベントはバブリングするためイベントハンドラが重複しないようにする
- レイアウト変更でscrollHeightが変わる場合に備える
- SSRでは`window`が存在しないためガードが必要

## 関連技術
- RxJS fromEvent/throttleTime
- IntersectionObserver
- Virtual Scroll
