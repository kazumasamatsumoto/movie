# #399 「Attribute Directive のベストプラクティス」

## 概要
Attribute Directiveを品質高く保つには責務の明確化、DOM操作の抽象化、ライフサイクル管理、テスト戦略など複数の観点からベストプラクティスを押さえる必要がある。

## 学習目標
- Attribute Directive設計で意識すべきポイントを体系的に理解する
- 副作用管理とテスト戦略を学ぶ
- チーム開発でディレクティブを共有するためのルールを整える

## 技術ポイント
- `Renderer2`, `DestroyRef`, `Signals`で副作用を安全に扱う
- Inputsで明示的な契約を定義し、必須項目を`@Input({ required: true })`で宣言
- テストではホストコンポーネントを用意して期待するクラス・属性を検証

## 📺 画面表示用コード（動画用）
```typescript
@Directive({ selector: '[appSafeHover]', standalone: true })
export class SafeHoverDirective {
  constructor(private readonly renderer: Renderer2, private readonly el: ElementRef<HTMLElement>, destroyRef: DestroyRef) {
    const off = this.renderer.listen(this.el.nativeElement, 'mouseenter', () => this.renderer.addClass(this.el.nativeElement, 'is-hover'));
    destroyRef.onDestroy(off);
  }
}
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appSafeHover]',
  standalone: true
})
export class SafeHoverDirective implements OnInit {
  @Input({ required: true }) hoverClass!: string;
  private off?: () => void;

  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2, destroyRef: DestroyRef) {
    destroyRef.onDestroy(() => this.off?.());
  }

  ngOnInit(): void {
    this.off = this.renderer.listen(this.el.nativeElement, 'mouseenter', () =>
      this.renderer.addClass(this.el.nativeElement, this.hoverClass)
    );
  }
}
```

## ベストプラクティス
- 副作用の登録と解除をライフサイクルフックまたはDestroyRefで一元管理
- ビジネスロジックを含めず、DOM操作と表示に責務を限定
- テスト・ドキュメント・Storybookで利用方法を共有し、破壊的変更を防ぐ

## 注意点
- Inputsの型や必須性を明示し、予期せぬ値を受け取らないようにする
- 複数のディレクティブが同じ要素へ作用する場合の優先順位を設計
- SSRやWeb Workerでの挙動も想定し、ブラウザ依存コードにガードを入れる

## 関連技術
- DestroyRef
- Storybook / ドキュメント
- Angular Testing Library
