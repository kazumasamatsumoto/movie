# #373 "Don't Change DOM Structure"

## Overview
Attribute Directives only manipulate existing element attributes and styles without changing DOM tree structure itself, which is the critical difference from Structural Directives.

## Learning Objectives
- Understand why Attribute Directives don't change DOM structure
- Grasp design benefits from separation of responsibilities
- Explain alternative means when structure change is needed

## Technical Points
- Attribute Directives don't have templates and don't replace elements
- Use Structural Directives or components when structure manipulation is needed
- Minimal impact on layout and accessibility as DOM structure doesn't change

## 📺 Screen Display Code (For Video)
```typescript
@Directive({ selector: '[appPulse]', standalone: true })
export class PulseDirective {
  @HostBinding('class.is-pulse') isPulse = true;
}
```

## 💻 Detailed Implementation Example (For Learning)
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

## Best Practices
- Consider componentization or Structural Directive for requirements to change DOM structure
- Focus purely on adding styles and behavior with Attribute Directives
- Confirm element structure hasn't changed in tests for confidence

## Cautions
- Increasing custom attributes or classes may break consistency with stylesheets
- Evaluate layout impact when changing host element's display or position
- Avoid directly appending/removing DOM as it mixes responsibilities

## Related Technologies
- Structural Directive
- Renderer2
- CSS Design
