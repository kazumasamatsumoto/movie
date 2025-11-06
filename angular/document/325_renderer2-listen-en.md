# #325 "Event Monitoring with listen()"

## Overview
`Renderer2.listen` is an environment-independent API for monitoring events, making cleanup easy through a removal function.

## Learning Objectives
- Understand how to call `listen` and its return value
- Learn how to apply to global targets (document/window)
- Master patterns to prevent forgetting to remove listeners

## Technical Points
- Specify `'document'`, `'window'`, or element reference in the first argument
- Call the returned removal function in `ngOnDestroy`
- Properly update ChangeDetection or Signals within callbacks

## 📺 On-Screen Code (for video)
```typescript
@Directive({ selector: '[appHoverLog]', standalone: true })
export class HoverLogDirective implements OnInit, OnDestroy {
  private detach?: () => void;
  constructor(private readonly el: ElementRef<HTMLElement>, private readonly r: Renderer2) {}
  ngOnInit(): void {
    this.detach = this.r.listen(this.el.nativeElement, 'mouseenter', () => console.log('hover'));
  }
  ngOnDestroy(): void { this.detach?.(); }
}
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appOutsideClick]',
  standalone: true
})
export class OutsideClickDirective implements OnInit, OnDestroy {
  @Output() outside = new EventEmitter<void>();
  private detach?: () => void;

  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2) {}

  ngOnInit(): void {
    this.detach = this.renderer.listen('document', 'click', event => {
      if (!this.el.nativeElement.contains(event.target as Node)) {
        this.outside.emit();
      }
    });
  }

  ngOnDestroy(): void {
    this.detach?.();
  }
}
```

## Best Practices
- Retain the removal function in a property and always execute it in `ngOnDestroy`
- If ChangeDetection is needed, use `NgZone.run` or Signals to synchronize with UI updates
- Manage global listeners collectively to avoid duplicate registrations and memory leaks

## Considerations
- Events don't fire in SSR, so provide safe processing for browser initialization
- Registering many listeners can impact performance, so consolidate them
- Long processing within callbacks blocks the UI thread

## Related Technologies
- NgZone
- takeUntilDestroyed
- Renderer2
