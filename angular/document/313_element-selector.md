# #313 「要素セレクタ xxx」

## 概要
要素セレクタはカスタムタグ名でディレクティブを適用する方法で、テンプレートを持たないまま意味付けやアクセシビリティ補助を行える。

## 学習目標
- 要素セレクタの定義方法を理解する
- カスタム要素とアクセシビリティのバランスを取る
- コンポーネントではなくディレクティブとして扱う判断基準を学ぶ

## 技術ポイント
- `selector: 'app-marquee'`のようにタグ名で指定
- DOM構造は既存要素で構成し、Directiveは振る舞いと属性補完に集中
- `role`や`aria-*`などアクセシビリティ属性をDirectiveが補う

## 📺 画面表示用コード（動画用）
```typescript
@Directive({ selector: 'app-marquee', standalone: true })
export class MarqueeDirective {
  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2) {}
  ngOnInit(): void {
    this.renderer.setAttribute(this.el.nativeElement, 'role', 'marquee');
  }
}
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: 'app-marquee',
  standalone: true
})
export class MarqueeDirective implements OnInit, OnDestroy {
  @Input() speed = 50;
  private animationId?: number;

  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2) {}

  ngOnInit(): void {
    const element = this.el.nativeElement;
    this.renderer.setAttribute(element, 'role', 'marquee');
    this.renderer.setAttribute(element, 'aria-live', 'polite');
    const animate = () => {
      element.scrollLeft = (element.scrollLeft + 1) % element.scrollWidth;
      this.animationId = requestAnimationFrame(animate);
    };
    this.animationId = requestAnimationFrame(animate);
  }

  ngOnDestroy(): void {
    if (this.animationId) cancelAnimationFrame(this.animationId);
  }
}

@Component({
  selector: 'app-marquee-demo',
  standalone: true,
  imports: [CommonModule, MarqueeDirective],
  template: `
    <app-marquee class="marquee">
      <span>Directiveでカスタム要素ライクな挙動を追加。</span>
    </app-marquee>
  `,
  styles: [`
    .marquee { display: block; overflow: hidden; white-space: nowrap; }
    .marquee span { display: inline-block; padding-right: 2rem; }
  `]
})
export class MarqueeDemoComponent {}
```

## ベストプラクティス
- カスタムタグにはプレフィックスを付け、ブラウザのネイティブ要素と衝突させない
- アクセシビリティを考慮し、roleやaria属性を自動で補完する
- DOM構造の変更は最小限に留め、Directiveが責務を持ちすぎないようにする

## 注意点
- SEOやSSRで未知タグが正しく扱われるかをテストする
- スタイル指定はCSS側で行い、Directiveは意味・振る舞いに集中する
- カスタム要素(Angular Elements)とは異なるため、混同しない

## 関連技術
- Angular Elements
- Renderer2
- Accessibility (ARIA)
