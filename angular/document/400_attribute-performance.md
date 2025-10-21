# #400 「パフォーマンス考慮事項」

## 概要
Attribute Directiveは小さいながら頻繁にDOM操作を行う場合があり、パフォーマンスを意識した実装が必要。無駄な描画やイベント登録を避ける工夫が重要である。

## 学習目標
- Attribute Directiveで発生しうるパフォーマンス課題を理解する
- Renderer2とSignalsを活用した差分更新の考え方を学ぶ
- イベントリスナーの管理やスロットリング方法を把握する

## 技術ポイント
- Renderer2の操作は必要最小限に絞り、前回値と比較して差分適用
- `effect`/`signal`で状態変化を監視し差分のみ更新
- イベントは`fromEvent`や`throttleTime`を使って制御

## 📺 画面表示用コード（動画用）
```typescript
@Directive({ selector: '[appThrottleHover]', standalone: true })
export class ThrottleHoverDirective {
  constructor(private readonly renderer: Renderer2, private readonly el: ElementRef<HTMLElement>) {}
  ngOnInit(): void {
    fromEvent(this.el.nativeElement, 'mousemove').pipe(throttleTime(100)).subscribe(() => this.renderer.addClass(this.el.nativeElement, 'is-active'));
  }
}
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appEfficientStyle]',
  standalone: true
})
export class EfficientStyleDirective implements OnDestroy {
  @Input({ required: true }) appEfficientStyle!: Signal<string>;
  private destroy = new Subject<void>();
  private previous?: string;

  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2) {}

  ngOnInit(): void {
    effect(() => {
      const color = this.appEfficientStyle();
      if (color === this.previous) return;
      this.previous = color;
      this.renderer.setStyle(this.el.nativeElement, 'color', color);
    });
  }

  ngOnDestroy(): void {
    this.destroy.next();
    this.destroy.complete();
  }
}
```

## ベストプラクティス
- 前回値を記録して不要なDOM書き換えを避ける
- 重い処理やイベントを扱う場合は`throttleTime`や`debounceTime`で制御
- SignalsやComputedを利用し、状態更新を局所化して再描画を減らす

## 注意点
- RxJSストリームを利用する場合は購読解除を忘れない
- `effect`はコンポーネント破棄時に自動解除されるがDestroyRefと組み合わせるとより安全
- 頻繁なDOM操作はレイアウトスラッシングを招くため、一括更新を検討

## 関連技術
- Angular Signals / effect
- RxJS throttleTime
- Performance Profiling (Chrome DevTools)
