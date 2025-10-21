# #317 「ElementRef - 要素参照」

## 概要
`ElementRef`はホスト要素への参照をカプセル化するクラスで、`nativeElement`プロパティを通じてDOMノードへアクセスできる。

## 学習目標
- ElementRefの役割と仕組みを理解する
- 型パラメータで安全にDOM要素を扱う方法を学ぶ
- Renderer2と組み合わせた推奨パターンを把握する

## 技術ポイント
- `ElementRef<HTMLElement>`のように型を指定可能
- 直接DOM操作よりもRenderer2を優先
- テストでは`new ElementRef(document.createElement('div'))`などで容易に再現

## 📺 画面表示用コード（動画用）
```typescript
@Directive({ selector: '[appFocusRing]', standalone: true })
export class FocusRingDirective {
  constructor(private readonly el: ElementRef<HTMLButtonElement>, private readonly renderer: Renderer2) {}
  ngOnInit(): void {
    this.renderer.setStyle(this.el.nativeElement, 'outline', '2px solid #38bdf8');
  }
}
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appFocusRing]',
  standalone: true
})
export class FocusRingDirective implements OnInit, OnDestroy {
  @Input() appFocusRing = '#38bdf8';
  private removeFocus?: () => void;
  private removeBlur?: () => void;

  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2) {}

  ngOnInit(): void {
    const host = this.el.nativeElement;
    this.renderer.setStyle(host, 'outline', `2px solid ${this.appFocusRing}`);
    this.removeFocus = this.renderer.listen(host, 'focus', () => this.renderer.setStyle(host, 'outline-style', 'solid'));
    this.removeBlur = this.renderer.listen(host, 'blur', () => this.renderer.setStyle(host, 'outline-style', 'dashed'));
  }

  ngOnDestroy(): void {
    this.removeFocus?.();
    this.removeBlur?.();
    this.renderer.removeStyle(this.el.nativeElement, 'outline');
  }
}
```

## ベストプラクティス
- 型パラメータで対象要素を明示し、`nativeElement`利用時の型安全性を向上させる
- DOM操作はRenderer2経由にし、`ElementRef`は要素参照の取得のみにとどめる
- テストでは`document.createElement`で要素を生成し、`ElementRef`に渡して検証する

## 注意点
- `ElementRef`をサービスへ保持するとメモリリークの原因になるため、Directive内に限定する
- SSRでは`nativeElement`が未定義のことがあるため、アクセス前にチェックする
- 外部ライブラリへ直接渡すとそのライブラリがDOMを破壊する恐れがある

## 関連技術
- Renderer2
- Dependency Injection
- Angular Testing Utilities
