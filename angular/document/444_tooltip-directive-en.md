# #444 "Tooltip Directive - Tooltip"

## Overview
The Tooltip directive displays supplementary information on mouseover or focus on the host element, generating a Tooltip element outside the template using Renderer2 and adjusting its position.

## Learning Objectives
- Understand the structure of the Tooltip directive
- Learn how to control show/hide with hover/focus events
- Grasp basic patterns for position adjustment

## Technical Points
- Monitor `mouseenter`/`mouseleave`/`focus`/`blur` with HostListener
- Dynamically create/delete DOM elements with Renderer2
- Accept message and position specification via Input

## 📺 On-Screen Code (for video)
```typescript
@Input() appTooltip = '説明';
@HostListener('mouseenter') show(): void { this.createTooltip(); }
@HostListener('mouseleave') hide(): void { this.destroyTooltip(); }
```

## 💻 Detailed Implementation Example (for learning)
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

## Best Practices
- Add Tooltip element directly under body to handle stacking order and overflow
- Provide options like placement/offset via Input
- Support focus to provide information to keyboard users as well

## Considerations
- Browser detection is necessary because document does not exist in SSR
- Implement position correction as it becomes invisible when outside viewport
- Consider reuse as generating many Tooltips affects performance

## Related Technologies
- Renderer2
- IntersectionObserver (advanced position adjustment)
- Accessibility (aria-describedby)
