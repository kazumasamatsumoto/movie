# #322 「setStyle() でのスタイル設定」

## 概要
`Renderer2.setStyle`はインラインスタイルを安全に追加する手段で、優先順位や`!important`指定も制御できる。

## 学習目標
- `setStyle`の引数と戻り値を理解する
- スタイル適用と解除のバランスを学ぶ
- `RendererStyleFlags2`の活用を知る

## 技術ポイント
- 引数は`(element, styleName, value, flags?)`
- `RendererStyleFlags2.Important`で`!important`指定
- 解除は`removeStyle`で行う

## 📺 画面表示用コード（動画用）
```typescript
@Directive({ selector: '[appDim]', standalone: true })
export class DimDirective implements OnChanges {
  @Input({ alias: 'appDim' }) level = 0.5;
  constructor(private readonly el: ElementRef<HTMLElement>, private readonly r: Renderer2) {}
  ngOnChanges(): void {
    this.r.setStyle(this.el.nativeElement, 'opacity', String(this.level));
  }
}
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appDim]',
  standalone: true
})
export class DimDirective implements OnChanges, OnDestroy {
  @Input({ alias: 'appDim' }) level = 0.5;
  @Input() important = false;

  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2) {}

  ngOnChanges(): void {
    const flags = this.important ? RendererStyleFlags2.Important : undefined;
    this.renderer.setStyle(this.el.nativeElement, 'opacity', String(this.level), flags);
  }

  ngOnDestroy(): void {
    this.renderer.removeStyle(this.el.nativeElement, 'opacity');
  }
}
```

## ベストプラクティス
- `removeStyle`でクリーンアップし、不要なインラインスタイルを残さない
- `RendererStyleFlags2.Important`の乱用を避け、CSS設計を優先する
- 数値を扱う場合は文字列化して単位を付与するなど一貫した形式で渡す

## 注意点
- 同じ要素で別ディレクティブが同一プロパティに触れると競合する
- トランジションを適用する際は遅延更新でちらつきを抑える
- SSRではスタイルがインラインで出力されるためCSSとの整合性を確認する

## 関連技術
- RendererStyleFlags2
- HostBinding
- CSS設計
