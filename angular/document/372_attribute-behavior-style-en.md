# #372 "Changing Element Behavior and Appearance"

## Overview
Attribute Directives can modify element behavior and appearance in reusable ways by controlling host element classes, styles, attributes, and events.

## Learning Objectives
- Enumerate aspects of elements that can be modified with Attribute Directives
- Understand control methods using Renderer2 and Host metadata
- Grasp practical examples of adding behavior

## Technical Points
- `renderer.setStyle`, `renderer.addClass`, `renderer.listen`
- Reflect attributes and properties with HostBinding
- Handle events with HostListener

## 📺 Screen Display Code (For Video)
```typescript
@Directive({ selector: '[appHoverElevate]', standalone: true })
export class HoverElevateDirective {
  constructor(private readonly r: Renderer2, private readonly el: ElementRef<HTMLElement>) {}
  ngOnInit(): void { this.r.listen(this.el.nativeElement, 'mouseenter', () => this.r.addClass(this.el.nativeElement, 'is-hover')); }
}
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
@Directive({
  selector: '[appHoverElevate]',
  standalone: true
})
export class HoverElevateDirective implements OnInit, OnDestroy {
  @Input() elevation = '0 10px 35px rgba(15,23,42,.2)';
  private removeEnter?: () => void;
  private removeLeave?: () => void;

  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2) {}

  ngOnInit(): void {
    const host = this.el.nativeElement;
    this.renderer.setStyle(host, 'transition', 'box-shadow .3s ease');
    this.removeEnter = this.renderer.listen(host, 'mouseenter', () =>
      this.renderer.setStyle(host, 'boxShadow', this.elevation)
    );
    this.removeLeave = this.renderer.listen(host, 'mouseleave', () =>
      this.renderer.removeStyle(host, 'boxShadow')
    );
  }

  ngOnDestroy(): void {
    this.removeEnter?.();
    this.removeLeave?.();
  }
}
```

## Best Practices
- Handle side effects via Renderer2 for platform independence
- Keep cleanup functions for events received by HostListener to release them
- Reflect UI change intent in class names or attribute names, considering Accessibility

## Cautions
- Excessive DOM manipulation causes performance degradation
- Unify naming conventions to avoid class or style conflicts
- Split complex behavior into services or Composable functions for testability

## Related Technologies
- Renderer2
- HostBinding / HostListener
- Angular Animation API
