# #421 「@Input() プロパティ」

## 概要
`@Input()`デコレータはテンプレートから値をディレクティブへ受け渡す仕組みで、エイリアス指定により属性名とプロパティ名を柔軟に管理できる。

## 学習目標
- `@Input()`の書き方とエイリアス設定を理解する
- 型注釈を付けた安全なInput設計を学ぶ
- Input変更時の処理フローを把握する

## 技術ポイント
- `@Input() color = '#facc15';`
- `@Input('appHighlight') set highlight(color: string) {...}`
- `ngOnChanges(changes: SimpleChanges)`で変更検知

## 📺 画面表示用コード（動画用）
```typescript
@Input('appHighlight') color = '#fde047';
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appHighlight]',
  standalone: true
})
export class HighlightDirective implements OnChanges {
  @Input('appHighlight') color = '#fde047';

  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2) {}

  ngOnChanges(): void {
    this.renderer.setStyle(this.el.nativeElement, 'backgroundColor', this.color);
  }
}
```

## ベストプラクティス
- 属性名エイリアスでテンプレートのバインディング名をわかりやすくする
- 型安全のため、Union型やインターフェースで受け取る値を制限
- 変更が起きたタイミングでのみ副作用を実行し、無駄な更新を避ける

## 注意点
- Inputプロパティは初期化前に使用しないようガードが必要
- 変更検知が走る頻度を意識し、重い処理は遅延させる
- Standaloneディレクティブでも`@Input`は利用できるが`imports`登録を忘れない

## 関連技術
- OnChanges
- SignalsとInput
- Directive APIの設計
