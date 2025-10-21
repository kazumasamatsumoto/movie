# #311 「属性セレクタ [appXxx]」

## 概要
属性セレクタは最も一般的なディレクティブの適用方法で、既存要素に属性のように記述して振る舞いを付与できる。バインディングとも相性が良い。

## 学習目標
- 属性セレクタの構文と適用方法を理解する
- バインディングで値を渡す手順を習得する
- 複数属性と共存させる際の注意点を把握する

## 技術ポイント
- `selector: '[appHighlight]'`のようにブラケットで囲む
- テンプレートでは`<div appHighlight></div>`や`[appHighlight]="value"`といった書き方が可能
- `@Input({ alias: 'appHighlight' })`でプロパティ名と揃えられる

## 📺 画面表示用コード（動画用）
```typescript
@Directive({ selector: '[appHighlight]', standalone: true })
export class HighlightDirective {
  @Input({ alias: 'appHighlight' }) color = '#fde047';
  constructor(private readonly renderer: Renderer2, private readonly el: ElementRef<HTMLElement>) {}
  ngOnChanges(): void {
    this.renderer.setStyle(this.el.nativeElement, 'backgroundColor', this.color);
  }
}
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appHighlight]',
  standalone: true
})
export class HighlightDirective implements OnChanges {
  @Input({ alias: 'appHighlight' }) color = '#fde047';
  @Input() appHighlightHover?: string;

  constructor(private readonly renderer: Renderer2, private readonly el: ElementRef<HTMLElement>) {}

  ngOnChanges(): void {
    this.renderer.setStyle(this.el.nativeElement, 'backgroundColor', this.color);
  }

  @HostListener('mouseenter')
  onMouseEnter(): void {
    if (this.appHighlightHover) {
      this.renderer.setStyle(this.el.nativeElement, 'backgroundColor', this.appHighlightHover);
    }
  }

  @HostListener('mouseleave')
  onMouseLeave(): void {
    this.renderer.setStyle(this.el.nativeElement, 'backgroundColor', this.color);
  }
}

@Component({
  selector: 'app-attribute-selector-demo',
  standalone: true,
  imports: [CommonModule, HighlightDirective],
  template: `
    <p appHighlight="#fef3c7" [appHighlightHover]="'#facc15'">
      属性セレクタで背景色を切り替えます。
    </p>
  `
})
export class AttributeSelectorDemoComponent {}
```

## ベストプラクティス
- Inputエイリアスを利用してテンプレートの属性名とプロパティ名を一致させる
- デフォルト値を用意し、利用側が値を省略しても破綻しないようにする
- 他の属性と共存できるよう、スタイルの上書き範囲を限定する

## 注意点
- バインディングで複雑な式を書くと可読性が落ちるため、ビュー側で計算した値を渡す
- 属性の順序は意味がないが、チーム内で整形ルールを統一し差分を減らす
- SSRではDOMイベントが動かないため、初期状態が適切か確認する

## 関連技術
- HostBinding / HostListener
- Renderer2
- Angular Style Guide
