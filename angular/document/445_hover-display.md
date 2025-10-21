# #445 「ホバー時の表示」

## 概要
Tooltipではホバー時（およびフォーカス時）に要素を表示し、マウスが離れると非表示にする。Renderer2で要素の生成・破棄を行うのが一般的。

## 学習目標
- ホバー/フォーカスイベントで表示・非表示を切り替える方法を理解する
- Tooltip要素の生成と破棄のタイミングを学ぶ
- アクセシビリティ対応（フォーカス）を取り入れる

## 技術ポイント
- `mouseenter`/`mouseleave`/`focus`/`blur`
- Renderer2でDOM要素をappend/remove
- 滞留時間をInputで調整する場合もある

## 📺 画面表示用コード（動画用）
```typescript
@HostListener('mouseenter') show(): void { this.createTooltip(); }
@HostListener('mouseleave') hide(): void { this.destroyTooltip(); }
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appTooltip]',
  standalone: true
})
export class TooltipDirective {
  @Input() message = '';
  private tooltip?: HTMLElement;

  constructor(
    private readonly el: ElementRef<HTMLElement>,
    private readonly renderer: Renderer2,
    @Inject(DOCUMENT) private readonly document: Document
  ) {}

  @HostListener('mouseenter')
  @HostListener('focus')
  show(): void {
    if (!this.message || this.tooltip) return;
    this.tooltip = this.renderer.createElement('div');
    this.renderer.addClass(this.tooltip, 'tooltip');
    this.renderer.appendChild(this.tooltip, this.renderer.createText(this.message));
    this.renderer.appendChild(this.document.body, this.tooltip);
    const rect = this.el.nativeElement.getBoundingClientRect();
    this.renderer.setStyle(this.tooltip, 'position', 'fixed');
    this.renderer.setStyle(this.tooltip, 'top', `${rect.bottom + 8}px`);
    this.renderer.setStyle(this.tooltip, 'left', `${rect.left}px`);
  }

  @HostListener('mouseleave')
  @HostListener('blur')
  hide(): void {
    if (this.tooltip) {
      this.renderer.removeChild(this.document.body, this.tooltip);
      this.tooltip = undefined;
    }
  }
}
```

## ベストプラクティス
- Tooltip要素はbody直下に追加し、スクロール時も位置がずれにくくする
- フォーカス対応でキーボードユーザーにも情報を提供
- Tooltip内容が動的に変わる場合は`ngOnChanges`で更新

## 注意点
- `document`使用時はSSRガードを入れる
- 要素が小さい場合、マウス移動で一瞬で消えるのでdelayを検討
- Tooltipが多いときは位置計算の最適化が必要

## 関連技術
- Renderer2
- Tooltip CSS
- Accessibility (ARIA)
