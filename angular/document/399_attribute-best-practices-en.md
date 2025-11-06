# #399 "Attribute Directive Best Practices"

## Overview
To maintain high-quality Attribute Directives, it's necessary to follow best practices from multiple perspectives including clarifying responsibilities, abstracting DOM operations, lifecycle management, and testing strategies.

## Learning Objectives
- Systematically understand points to be aware of in Attribute Directive design
- Learn side effect management and testing strategies
- Organize rules for sharing directives in team development

## Technical Points
- Handle side effects safely with `Renderer2`, `DestroyRef`, `Signals`
- Define explicit contracts with Inputs, declare required items with `@Input({ required: true })`
- In tests, prepare host components to verify expected classes/attributes

## 📺 Display Code (for video)
```typescript
@Directive({ selector: '[appSafeHover]', standalone: true })
export class SafeHoverDirective {
  constructor(private readonly renderer: Renderer2, private readonly el: ElementRef<HTMLElement>, destroyRef: DestroyRef) {
    const off = this.renderer.listen(this.el.nativeElement, 'mouseenter', () => this.renderer.addClass(this.el.nativeElement, 'is-hover'));
    destroyRef.onDestroy(off);
  }
}
```

## 💻 Detailed Implementation Example (for learning)
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

## Best Practices
- Centrally manage registration and deregistration of side effects with lifecycle hooks or DestroyRef
- Don't include business logic, limit responsibilities to DOM operations and display
- Share usage through tests, documentation, and Storybook to prevent breaking changes

## Considerations
- Clarify Input types and requirements to avoid receiving unexpected values
- Design priorities when multiple directives act on the same element
- Assume behavior in SSR and Web Workers, add guards to browser-dependent code

## Related Technologies
- DestroyRef
- Storybook / Documentation
- Angular Testing Library
