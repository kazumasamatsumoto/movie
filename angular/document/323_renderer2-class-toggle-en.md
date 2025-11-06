# #323 "addClass() / removeClass()"

## Overview
`addClass` and `removeClass` are Renderer2 methods for safely toggling classes, allowing style management to be delegated to CSS.

## Learning Objectives
- Master the basic patterns of class manipulation
- Understand implementation for conditionally switching classes
- Avoid unnecessary DOM operations through differential application

## Technical Points
- For multiple classes, operate individually in a loop
- Retain previous state to reduce unnecessary calls
- Remove classes on teardown if necessary

## 📺 On-Screen Code (for video)
```typescript
@Directive({ selector: '[appActiveClass]', standalone: true })
export class ActiveClassDirective implements OnChanges {
  @Input({ alias: 'appActiveClass' }) active = false;
  constructor(private readonly el: ElementRef<HTMLElement>, private readonly r: Renderer2) {}
  ngOnChanges(): void {
    if (this.active) this.r.addClass(this.el.nativeElement, 'is-active');
    else this.r.removeClass(this.el.nativeElement, 'is-active');
  }
}
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appStateClasses]',
  standalone: true
})
export class StateClassesDirective implements OnChanges, OnDestroy {
  @Input() states: string[] = [];
  private applied = new Set<string>();

  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2) {}

  ngOnChanges(): void {
    const host = this.el.nativeElement;
    const next = new Set(this.states);
    for (const name of this.applied) {
      if (!next.has(name)) {
        this.renderer.removeClass(host, name);
        this.applied.delete(name);
      }
    }
    for (const name of next) {
      if (!this.applied.has(name)) {
        this.renderer.addClass(host, name);
        this.applied.add(name);
      }
    }
  }

  ngOnDestroy(): void {
    const host = this.el.nativeElement;
    for (const name of this.applied) {
      this.renderer.removeClass(host, name);
    }
    this.applied.clear();
  }
}
```

## Best Practices
- Use prefixes for class names to clarify responsibilities
- Track add/remove diffs to prevent unnecessary DOM operations
- Receive state through Input and manage boolean values from the template side

## Considerations
- Document naming conventions to avoid collisions with existing classes
- When using utility classes like Tailwind, limit the classes handled as they can become numerous
- In SSR, verify that the initial state matches the browser initialization state

## Related Technologies
- Renderer2
- CSS Utility classes
- Signals for state management
