# #371 "What is an Attribute Directive?"

## Overview
Attribute Directives are lightweight extension mechanisms applied like attributes to existing DOM elements, adding or modifying appearance and behavior.

## Learning Objectives
- Explain the role and characteristics of Attribute Directives
- Understand differences from Structural Directives
- Grasp representative usage patterns

## Technical Points
- Defined like `@Directive({ selector: '[appX]' })`
- Manipulate host elements without having templates
- Add behavior with Renderer2 or HostBinding/HostListener

## 📺 Screen Display Code (For Video)
```typescript
@Directive({ selector: '[appAccent]', standalone: true })
export class AccentDirective {
  constructor(private readonly r: Renderer2, private readonly el: ElementRef<HTMLElement>) {}
  ngOnInit(): void { this.r.setStyle(this.el.nativeElement, 'outline', '2px solid #38bdf8'); }
}
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
@Directive({
  selector: '[appAccent]',
  standalone: true
})
export class AccentDirective implements OnInit, OnDestroy {
  @Input() appAccent = '#38bdf8';
  private removeHover?: () => void;

  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2) {}

  ngOnInit(): void {
    const host = this.el.nativeElement;
    this.renderer.setStyle(host, 'outline', `2px solid ${this.appAccent}`);
    this.removeHover = this.renderer.listen(host, 'mouseenter', () =>
      this.renderer.setStyle(host, 'outlineColor', '#0ea5e9')
    );
  }

  ngOnDestroy(): void {
    this.removeHover?.();
    this.renderer.removeStyle(this.el.nativeElement, 'outline');
  }
}
```

## Best Practices
- Perform DOM operations via Renderer2 to avoid platform dependencies
- Limit responsibilities to host element appearance and behavior, don't include business logic
- Manage side effect initialization and cleanup with lifecycle hooks

## Cautions
- Multiple directives modifying same property will conflict
- DOM doesn't exist in SSR, so guard with `isPlatformBrowser` if needed
- Verify host element state is as expected in tests

## Related Technologies
- HostBinding / HostListener
- Renderer2
- Comparison with Structural Directives
