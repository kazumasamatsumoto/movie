# #445 "Hover Display"

## Overview
Tooltips display elements on hover (and focus) and hide them when the mouse leaves. Typically, element creation and destruction is done with Renderer2.

## Learning Objectives
- Understand how to toggle show/hide with hover/focus events
- Learn the timing of Tooltip element creation and destruction
- Incorporate accessibility support (focus)

## Technical Points
- `mouseenter`/`mouseleave`/`focus`/`blur`
- Append/remove DOM elements with Renderer2
- May also adjust dwell time via Input

## 📺 On-Screen Code (for video)
```typescript
@HostListener('mouseenter') show(): void { this.createTooltip(); }
@HostListener('mouseleave') hide(): void { this.destroyTooltip(); }
```

## 💻 Detailed Implementation Example (for learning)
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

## Best Practices
- Add Tooltip element directly under body to minimize position shift during scrolling
- Provide information to keyboard users with focus support
- Update with `ngOnChanges` if Tooltip content changes dynamically

## Considerations
- Add SSR guard when using `document`
- Consider delay if element is small, as tooltip disappears instantly with mouse movement
- Position calculation optimization is needed when there are many Tooltips

## Related Technologies
- Renderer2
- Tooltip CSS
- Accessibility (ARIA)
