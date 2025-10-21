# #371 「Attribute Directive とは？」

## 概要
Attribute Directiveは既存DOM要素に属性のように付与し、見た目や振る舞いを追加・変更する軽量な拡張手段である。

## 学習目標
- Attribute Directiveの役割と特徴を説明できる
- Structural Directiveとの違いを理解する
- 代表的な利用パターンを把握する

## 技術ポイント
- `@Directive({ selector: '[appX]' })`のように定義
- テンプレートを持たずホスト要素を操作
- Renderer2やHostBinding/HostListenerで振る舞いを付与

## 📺 画面表示用コード（動画用）
```typescript
@Directive({ selector: '[appAccent]', standalone: true })
export class AccentDirective {
  constructor(private readonly r: Renderer2, private readonly el: ElementRef<HTMLElement>) {}
  ngOnInit(): void { this.r.setStyle(this.el.nativeElement, 'outline', '2px solid #38bdf8'); }
}
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appAccent]',
  standalone: true
})
export class AccentDirective implements OnInit, OnDestroy {
  @Input() appAccent = '#38bdf8';
  private removeHover?: () => void;

  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2) {}

  ngOnInit(): void {
    const host = this.el.nativeElement;
    this.renderer.setStyle(host, 'outline', `2px solid ${this.appAccent}`);
    this.removeHover = this.renderer.listen(host, 'mouseenter', () =>
      this.renderer.setStyle(host, 'outlineColor', '#0ea5e9')
    );
  }

  ngOnDestroy(): void {
    this.removeHover?.();
    this.renderer.removeStyle(this.el.nativeElement, 'outline');
  }
}
```

## ベストプラクティス
- DOM操作はRenderer2経由で行い、プラットフォーム依存を避ける
- 責務はホスト要素の見た目や振る舞いに限定し、ビジネスロジックを持たせない
- ライフサイクルフックで副作用の初期化と解放を管理する

## 注意点
- 複数ディレクティブで同一プロパティを変更すると競合する
- SSRではDOMが存在しないため、必要なら`isPlatformBrowser`でガード
- テストでホスト要素の状態が期待通りか確認する

## 関連技術
- HostBinding / HostListener
- Renderer2
- Structural Directiveとの比較
