# #444 「Tooltip Directive - ツールチップ」

## 概要
Tooltipディレクティブはホスト要素にマウスオーバーやフォーカス時に補足情報を表示し、Renderer2でテンプレート外にTooltip要素を生成して位置を調整する。

## 学習目標
- Tooltipディレクティブの構造を理解する
- ホバー/フォーカスイベントで表示・非表示を制御する方法を学ぶ
- 位置調整の基本パターンを把握する

## 技術ポイント
- HostListenerで`mouseenter`/`mouseleave`/`focus`/`blur`を監視
- Renderer2でDOM要素を動的生成・削除
- Inputでメッセージや位置指定を受け取る

## 📺 画面表示用コード（動画用）
```typescript
@Input() appTooltip = '説明';
@HostListener('mouseenter') show(): void { this.createTooltip(); }
@HostListener('mouseleave') hide(): void { this.destroyTooltip(); }
```

## 💻 詳細実装例（学習用）
```typescript
interface TooltipOptions {
  placement: 'top' | 'bottom' | 'left' | 'right';
  offset: number;
}

@Directive({
  selector: '[appTooltip]',
  standalone: true
})
export class TooltipDirective implements OnDestroy {
  @Input() appTooltip = '';
  @Input() tooltipOptions: Partial<TooltipOptions> = {};

  private tooltipEl?: HTMLElement;

  constructor(
    private readonly el: ElementRef<HTMLElement>,
    private readonly renderer: Renderer2,
    @Inject(DOCUMENT) private readonly document: Document
  ) {}

  @HostListener('mouseenter')
  @HostListener('focus')
  show(): void {
    if (!this.appTooltip || this.tooltipEl) return;
    this.tooltipEl = this.renderer.createElement('div');
    this.renderer.addClass(this.tooltipEl, 'tooltip');
    this.renderer.appendChild(this.tooltipEl, this.renderer.createText(this.appTooltip));
    this.renderer.appendChild(this.document.body, this.tooltipEl);
    this.positionTooltip();
  }

  @HostListener('mouseleave')
  @HostListener('blur')
  hide(): void {
    this.destroyTooltip();
  }

  ngOnDestroy(): void {
    this.destroyTooltip();
  }

  private positionTooltip(): void {
    if (!this.tooltipEl) return;
    const hostRect = this.el.nativeElement.getBoundingClientRect();
    const tooltipRect = this.tooltipEl.getBoundingClientRect();
    const { placement = 'top', offset = 8 } = this.tooltipOptions;
    let top = 0;
    let left = 0;
    switch (placement) {
      case 'bottom':
        top = hostRect.bottom + offset;
        left = hostRect.left + hostRect.width / 2 - tooltipRect.width / 2;
        break;
      case 'left':
        top = hostRect.top + hostRect.height / 2 - tooltipRect.height / 2;
        left = hostRect.left - tooltipRect.width - offset;
        break;
      case 'right':
        top = hostRect.top + hostRect.height / 2 - tooltipRect.height / 2;
        left = hostRect.right + offset;
        break;
      default:
        top = hostRect.top - tooltipRect.height - offset;
        left = hostRect.left + hostRect.width / 2 - tooltipRect.width / 2;
    }
    this.renderer.setStyle(this.tooltipEl, 'top', `${top}px`);
    this.renderer.setStyle(this.tooltipEl, 'left', `${left}px`);
    this.renderer.setStyle(this.tooltipEl, 'position', 'fixed');
  }

  private destroyTooltip(): void {
    if (this.tooltipEl) {
      this.renderer.removeChild(this.document.body, this.tooltipEl);
      this.tooltipEl = undefined;
    }
  }
}
```

## ベストプラクティス
- Tooltip要素はbody直下へ追加し、重なり順やoverflowに対応
- Inputでplacement/offset等のオプションを提供
- フォーカスにも対応し、キーボードユーザーにも情報提供

## 注意点
- SSRではdocumentが存在しないためブラウザ判定が必要
- viewport外に出ると見えないため位置補正を実装
- 多数のTooltip生成はパフォーマンスに影響するため再利用を検討

## 関連技術
- Renderer2
- IntersectionObserver（位置調整の高度化）
- Accessibility (aria-describedby)
