# #316 "Cleanup with ngOnDestroy"

## Overview
`ngOnDestroy` is called when directives are destroyed, providing the last chance to unregister event listeners, timers, and Observable subscriptions to clean up side effects.

## Learning Objectives
- Identify resources that should be released in `ngOnDestroy`
- Learn how to unregister Renderer2 listeners and Signal effects
- Understand techniques for verifying cleanup in tests

## Technical Points
- Hold unsubscribe functions returned by `listen` and IDs from `setInterval`
- Utilize `takeUntilDestroyed` or `destroyRef.onDestroy`
- Return DOM to original state after cleanup

## 📺 Display Code (For Video)
```typescript
@Directive({ selector: '[appHoverIntent]', standalone: true })
export class HoverIntentDirective implements OnDestroy {
  private remove?: () => void;
  constructor(private readonly renderer: Renderer2, private readonly el: ElementRef<HTMLElement>) {
    this.remove = this.renderer.listen(this.el.nativeElement, 'mouseenter', () => {});
  }
  ngOnDestroy(): void { this.remove?.(); }
}
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
@Directive({
  selector: '[appHoverIntent]',
  standalone: true
})
export class HoverIntentDirective implements OnInit, OnDestroy {
  private removeEnter?: () => void;
  private removeLeave?: () => void;
  private timer?: number;

  constructor(private readonly renderer: Renderer2, private readonly el: ElementRef<HTMLElement>) {}

  ngOnInit(): void {
    const element = this.el.nativeElement;
    this.removeEnter = this.renderer.listen(element, 'mouseenter', () => {
      this.timer = window.setTimeout(() => this.renderer.addClass(element, 'is-hover'), 150);
    });
    this.removeLeave = this.renderer.listen(element, 'mouseleave', () => {
      if (this.timer) clearTimeout(this.timer);
      this.renderer.removeClass(element, 'is-hover');
    });
  }

  ngOnDestroy(): void {
    this.removeEnter?.();
    this.removeLeave?.();
    if (this.timer) {
      clearTimeout(this.timer);
      this.timer = undefined;
    }
  }
}
```

## Best Practices
- Hold all unsubscribe functions and timer IDs as properties, releasing them together in `ngOnDestroy`
- Centralize cleanup registration using `DestroyRef`
- Verify in unit tests that listeners are unregistered after `ngOnDestroy` invocation with Spy

## Cautions
- Assume cases where `ngOnDestroy` isn't called (forced app termination, etc.), ensuring side effects don't affect the system
- Return DOM to original state if modified
- Not removing handlers registered to services leads to memory leaks

## Related Technologies
- Renderer2.listen
- DestroyRef
- takeUntilDestroyed
