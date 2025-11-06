# #457 "Scroll Position Monitoring"

## Overview
In infinite scroll and ScrollSpy, monitor scroll position to detect reaching the end or section display. Utilize IntersectionObserver or scroll events.

## Learning Objectives
- Understand scroll position monitoring techniques
- Learn distinction between IntersectionObserver and scroll events
- Ensure performance with throttling and debouncing

## Technical Points
- Monitor end with IntersectionObserver
- Calculate `scrollTop + clientHeight` with scroll event
- Control update frequency with RxJS `throttleTime`

## 📺 On-Screen Code (for video)
```typescript
const atBottom = container.scrollTop + container.clientHeight >= container.scrollHeight - threshold;
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appScrollWatcher]',
  standalone: true
})
export class ScrollWatcherDirective implements OnInit, OnDestroy {
  @Input() threshold = 16;
  @Output() reachBottom = new EventEmitter<void>();
  private destroy$ = new Subject<void>();

  constructor(private readonly el: ElementRef<HTMLElement>) {}

  ngOnInit(): void {
    fromEvent(this.el.nativeElement, 'scroll')
      .pipe(
        throttleTime(100),
        takeUntil(this.destroy$)
      )
      .subscribe(() => {
        const target = this.el.nativeElement;
        if (target.scrollTop + target.clientHeight >= target.scrollHeight - this.threshold) {
          this.reachBottom.emit();
        }
      });
  }

  ngOnDestroy(): void {
    this.destroy$.next();
    this.destroy$.complete();
  }
}
```

## Best Practices
- Prioritize IntersectionObserver when available to improve performance
- Reduce load with throttling when using scroll event
- Adjust threshold to load data slightly earlier

## Considerations
- Native scroll event bubbles, so ensure event handlers don't duplicate
- Prepare for cases where scrollHeight changes due to layout changes
- Guard needed as `window` does not exist in SSR

## Related Technologies
- RxJS fromEvent/throttleTime
- IntersectionObserver
- Virtual Scroll
