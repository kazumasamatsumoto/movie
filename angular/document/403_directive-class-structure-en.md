# #403 "Directive Class Basic Structure"

## Overview
A Directive class declares metadata with the `@Directive` decorator, and implements dependency injection, lifecycle hooks, and HostBinding/HostListener within the class.

## Learning Objectives
- Understand the components of a Directive class
- Learn the properties that can be specified in the `@Directive` decorator
- Learn how to utilize lifecycle hooks

## Technical Points
- `selector`, `standalone`, `providers`, `exportAs`
- Inject ElementRef, Renderer2, DestroyRef, etc. via DI
- Can implement `OnInit`, `OnDestroy`, `OnChanges`, etc.

## 📺 On-Screen Code (for video)
```typescript
@Directive({ selector: '[appFocus]', standalone: true })
export class FocusDirective implements OnInit, OnDestroy {
  constructor(private readonly el: ElementRef<HTMLInputElement>) {}
  ngOnInit(): void { this.el.nativeElement.focus(); }
  ngOnDestroy(): void { this.el.nativeElement.blur(); }
}
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appAutoFocus]',
  standalone: true,
  exportAs: 'appAutoFocus'
})
export class AutoFocusDirective implements OnInit, OnDestroy {
  @Input() focusDelay = 0;
  private timeoutId?: number;

  constructor(private readonly el: ElementRef<HTMLElement>) {}

  ngOnInit(): void {
    this.timeoutId = window.setTimeout(() => this.el.nativeElement.focus(), this.focusDelay);
  }

  ngOnDestroy(): void {
    if (this.timeoutId) {
      clearTimeout(this.timeoutId);
    }
  }
}
```

## Best Practices
- Declare DI with `private readonly` and perform host element manipulation safely
- Use hooks to explicitly show the start and end of side effects
- Providing `exportAs` for template references improves visibility

## Considerations
- Don't perform DOM manipulation in `constructor`, wait until `ngOnInit`
- Don't forget to add the interface when implementing hooks
- Understand that specifying providers in `@Directive` limits scope to the host element

## Related Technologies
- ElementRef / Renderer2
- DestroyRef
- Angular Lifecycle Hooks
