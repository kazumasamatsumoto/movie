# #373 「DOMの構造は変えない」

## 概要
Attribute Directiveは既存要素の属性やスタイルを操作するだけで、DOMツリー構造そのものを変更しない点がStructural Directiveとの決定的な違いである。

## 学習目標
- Attribute DirectiveがDOM構造を変えない理由を理解する
- 責務分離による設計メリットを把握する
- 構造を変えたい場合の代替手段を説明できる

## 技術ポイント
- Attribute Directiveはテンプレートを持たず要素を置き換えない
- 構造操作が必要ならStructural Directiveやコンポーネントを使う
- DOM構造を変えないため、レイアウトやアクセシビリティへ影響が少ない

## 📺 画面表示用コード（動画用）
```typescript
@Directive({ selector: '[appPulse]', standalone: true })
export class PulseDirective {
  @HostBinding('class.is-pulse') isPulse = true;
}
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appPulse]',
  standalone: true
})
export class PulseDirective implements OnInit, OnDestroy {
  private removeAnimation?: () => void;

  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2) {}

  ngOnInit(): void {
    this.renderer.addClass(this.el.nativeElement, 'is-pulse');
    this.removeAnimation = this.renderer.listen(this.el.nativeElement, 'animationend', () =>
      this.renderer.removeClass(this.el.nativeElement, 'is-pulse')
    );
  }

  ngOnDestroy(): void {
    this.removeAnimation?.();
  }
}
```

## ベストプラクティス
- DOM構造を変えたい要件はコンポーネント化やStructural Directive化を検討する
- Attribute Directiveでは純粋にスタイルや振る舞いの付与だけに集中する
- テストで要素の構造が変わっていないことを確認して安心感を得る

## 注意点
- カスタム属性やクラスが増えるとスタイルシートとの整合性を崩す可能性がある
- ホスト要素のdisplayやpositionを変更する際はレイアウト影響を評価する
- DOMを直接append/removeすると責務が混ざるので避ける

## 関連技術
- Structural Directive
- Renderer2
- CSS設計
