# #400 "Performance Considerations"

## Overview
Attribute Directives, while small, may frequently perform DOM operations, requiring performance-conscious implementation. Ingenuity to avoid unnecessary rendering and event registration is important.

## Learning Objectives
- Understand potential performance issues with Attribute Directives
- Learn the concept of differential updates using Renderer2 and Signals
- Grasp event listener management and throttling methods

## Technical Points
- Minimize Renderer2 operations, compare with previous values and apply differences
- Monitor state changes with `effect`/`signal` and update only differences
- Control events using `fromEvent` or `throttleTime`

## 📺 Display Code (for video)
```typescript
@Directive({ selector: '[appThrottleHover]', standalone: true })
export class ThrottleHoverDirective {
  constructor(private readonly renderer: Renderer2, private readonly el: ElementRef<HTMLElement>) {}
  ngOnInit(): void {
    fromEvent(this.el.nativeElement, 'mousemove').pipe(throttleTime(100)).subscribe(() => this.renderer.addClass(this.el.nativeElement, 'is-active'));
  }
}
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appEfficientStyle]',
  standalone: true
})
export class EfficientStyleDirective implements OnDestroy {
  @Input({ required: true }) appEfficientStyle!: Signal<string>;
  private destroy = new Subject<void>();
  private previous?: string;

  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2) {}

  ngOnInit(): void {
    effect(() => {
      const color = this.appEfficientStyle();
      if (color === this.previous) return;
      this.previous = color;
      this.renderer.setStyle(this.el.nativeElement, 'color', color);
    });
  }

  ngOnDestroy(): void {
    this.destroy.next();
    this.destroy.complete();
  }
}
```

## Best Practices
- Record previous values to avoid unnecessary DOM rewrites
- Control heavy processing or events with `throttleTime` or `debounceTime`
- Use Signals or Computed to localize state updates and reduce re-rendering

## Considerations
- Don't forget to unsubscribe when using RxJS streams
- `effect` is automatically released when components are destroyed, but combining with DestroyRef is safer
- Frequent DOM operations can cause layout thrashing, so consider batch updates

## Related Technologies
- Angular Signals / effect
- RxJS throttleTime
- Performance Profiling (Chrome DevTools)
