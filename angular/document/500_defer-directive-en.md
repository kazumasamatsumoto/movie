# #500 "Defer Directive - Deferred Display"

## Overview
The Defer directive delays template display until conditions are met, improving performance and UX by rendering content only at necessary timing.

## Learning Objectives
- Understand structure of deferred display directive
- Learn mechanism to generate view when conditions are ready
- Grasp management methods for release conditions and re-display

## Technical Points
- Accept boolean/Promise/Observable via Input
- `createEmbeddedView` when condition becomes true
- Decide in design whether to hide again

## 📺 On-Screen Code (for video)
```html
<app-heavy *appDefer="isReady"></app-heavy>
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appDefer]',
  standalone: true
})
export class DeferDirective implements OnChanges {
  @Input('appDefer') condition: boolean | Promise<unknown> | Observable<unknown> = false;
  private viewCreated = false;
  private destroyRef = inject(DestroyRef);

  constructor(
    private readonly template: TemplateRef<unknown>,
    private readonly viewContainer: ViewContainerRef
  ) {}

  ngOnChanges(): void {
    this.viewContainer.clear();
    this.viewCreated = false;
    this.resolveCondition(this.condition);
  }

  private resolveCondition(value: boolean | Promise<unknown> | Observable<unknown>): void {
    if (value instanceof Promise) {
      value.then(() => this.show());
    } else if (isObservable(value)) {
      value.pipe(takeUntilDestroyed(this.destroyRef)).subscribe(() => this.show());
    } else if (value) {
      this.show();
    }
  }

  private show(): void {
    if (!this.viewCreated) {
      this.viewContainer.createEmbeddedView(this.template);
      this.viewCreated = true;
    }
  }
}
```

## Best Practices
- Support three types boolean/Promise/Observable to increase flexibility
- Control with `viewCreated` flag if view generation is only once
- Use `takeUntilDestroyed` for cancellation on asynchronous release

## Considerations
- Implement response when Promise/Observable errors
- Clarify specification whether to `clear` if re-display is needed
- Also consider initial state as asynchronous result delays in SSR

## Related Technologies
- Promise/Observable
- DestroyRef / takeUntilDestroyed
- Structural Directive implementation
