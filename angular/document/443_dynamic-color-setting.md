# #443 「動的な色指定」

## 概要
HighlightディレクティブにInputで色を渡せば、コンポーネントごとに異なる強調色を使用できる。デフォルト値を持たせつつ柔軟な設定を提供する。

## 学習目標
- Inputで色を動的に受け取る手法を理解する
- `ngOnChanges`やsetterで値を反映する方法を学ぶ
- デフォルト値とのマージやバリデーションを把握する

## 技術ポイント
- `@Input('appHighlight') color = '#fde047';`
- setterや`ngOnChanges`でスタイルへ反映
- 無効な色コードへのfallback

## 📺 画面表示用コード（動画用）
```typescript
@Input('appHighlight') set color(value: string) { this.background = value ?? '#fde047'; }
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appHighlight]',
  standalone: true
})
export class HighlightDirective implements OnChanges {
  private readonly defaultColor = '#fde047';
  @Input('appHighlight') color?: string;
  @HostBinding('style.backgroundColor') background = this.defaultColor;

  ngOnChanges(): void {
    this.background = this.isValidColor(this.color) ? this.color! : this.defaultColor;
  }

  private isValidColor(value?: string): boolean {
    return !!value && /^#([0-9a-f]{3}|[0-9a-f]{6})$/i.test(value);
  }
}
```

## ベストプラクティス
- 不正値に備えてバリデーションとデフォルト値を用意
- 色コードだけでなく`CSSColorValue`を受け取る構造も検討
- ドキュメントで受け付ける形式（HEX, RGB等）を明記

## 注意点
- 色コードのフォーマットを統一しなければスタイル競合が起きる
- Inputが頻繁に変わる場合はパフォーマンスを考慮
- SSRで初期色が確実に反映されるよう初期背景を設定

## 関連技術
- Input Transform
- HostBinding
- カラーバリデーションユーティリティ
