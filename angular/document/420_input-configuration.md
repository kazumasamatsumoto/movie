# #420 「Input での設定受け取り」

## 概要
Directiveに`@Input`を定義すると利用側テンプレートから設定値を受け取れ、振る舞いを柔軟にカスタマイズできる。

## 学習目標
- `@Input`プロパティの宣言方法を理解する
- 属性名とプロパティ名のエイリアス設定を学ぶ
- 設定値のバリデーションとデフォルト適用パターンを把握する

## 技術ポイント
- `@Input() appHighlightColor = '#facc15';`
- `@Input('appHighlight') set config(value: HighlightOptions)`
- `ngOnChanges`でバリデーションやフォールバック処理

## 📺 画面表示用コード（動画用）
```typescript
@Input() appHighlight = '#fde047';
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appHighlight]',
  standalone: true
})
export class HighlightDirective implements OnChanges {
  @Input() appHighlight = '#fde047';

  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2) {}

  ngOnChanges(): void {
    this.renderer.setStyle(this.el.nativeElement, 'backgroundColor', this.appHighlight);
  }
}
```

## ベストプラクティス
- Inputは型安全にし、受け取る値の意味をドキュメント化
- Setterまたは`ngOnChanges`でバリデーション・変換を実施
- デフォルト値を設定し、設定がなくても安全に動作させる

## 注意点
- 引数をオブジェクトで受け取る場合は`trackBy`などで参照不変にする
- Input変更で副作用が必要な場合はライフサイクルフックを適切に利用
- 双方向バインディングが必要なら`@Output()`との組み合わせを検討

## 関連技術
- @Input装飾子
- OnChanges
- Directive API設計
