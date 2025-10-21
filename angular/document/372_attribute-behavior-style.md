# #372 「要素の振る舞いや見た目の変更」

## 概要
Attribute Directiveはホスト要素のクラス・スタイル・属性・イベントを制御することで、振る舞いや見た目を再利用可能な形で変更できる。

## 学習目標
- Attribute Directiveで変更できる要素の側面を列挙する
- Renderer2やHostメタデータを使った制御方法を理解する
- 実際の振る舞い追加例を把握する

## 技術ポイント
- `renderer.setStyle`, `renderer.addClass`, `renderer.listen`
- HostBindingで属性やプロパティの反映
- HostListenerでイベントをハンドリング

## 📺 画面表示用コード（動画用）
```typescript
@Directive({ selector: '[appHoverElevate]', standalone: true })
export class HoverElevateDirective {
  constructor(private readonly r: Renderer2, private readonly el: ElementRef<HTMLElement>) {}
  ngOnInit(): void { this.r.listen(this.el.nativeElement, 'mouseenter', () => this.r.addClass(this.el.nativeElement, 'is-hover')); }
}
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appHoverElevate]',
  standalone: true
})
export class HoverElevateDirective implements OnInit, OnDestroy {
  @Input() elevation = '0 10px 35px rgba(15,23,42,.2)';
  private removeEnter?: () => void;
  private removeLeave?: () => void;

  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2) {}

  ngOnInit(): void {
    const host = this.el.nativeElement;
    this.renderer.setStyle(host, 'transition', 'box-shadow .3s ease');
    this.removeEnter = this.renderer.listen(host, 'mouseenter', () =>
      this.renderer.setStyle(host, 'boxShadow', this.elevation)
    );
    this.removeLeave = this.renderer.listen(host, 'mouseleave', () =>
      this.renderer.removeStyle(host, 'boxShadow')
    );
  }

  ngOnDestroy(): void {
    this.removeEnter?.();
    this.removeLeave?.();
  }
}
```

## ベストプラクティス
- Renderer2経由で副作用を扱い、プラットフォーム非依存にする
- HostListenerで受け取ったイベントはクリーンアップ関数を保持して解除
- UI変更の意図をclass名や属性名に反映し、Accessibilityも考慮する

## 注意点
- 過剰なDOM操作はパフォーマンス低下を招く
- クラスやスタイルの競合を避けるため命名規則を統一
- 複雑な振る舞いはサービスやComposableな関数へ分割しテストしやすくする

## 関連技術
- Renderer2
- HostBinding / HostListener
- Angular Animation API
