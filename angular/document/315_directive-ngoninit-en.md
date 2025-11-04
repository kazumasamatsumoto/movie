# #315 "Initialization with ngOnInit"

## Overview
`ngOnInit` is the initialization timing for directives, allowing safe setup of side effects after the host element becomes available.

## Learning Objectives
- Understand when `ngOnInit` is called
- Learn reasons to separate initialization processing from constructor
- Set up coordination with services and external resources

## Technical Points
- Receive DI in constructor, perform processing in `ngOnInit`
- Safely execute initialization requiring DOM references in `ngOnInit`
- Combine asynchronous processing with `takeUntilDestroyed`, etc.

## 📺 Display Code (For Video)
```typescript
@Directive({ selector: '[appLazyLoad]', standalone: true })
export class LazyLoadDirective implements OnInit {
  constructor(private readonly observer: LazyObserverService, private readonly el: ElementRef<HTMLElement>) {}
  ngOnInit(): void {
    this.observer.observe(this.el.nativeElement);
  }
}
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
@Directive({
  selector: '[appLazyLoad]',
  standalone: true
})
export class LazyLoadDirective implements OnInit, OnDestroy {
  @Output() visible = new EventEmitter<void>();
  private disconnect?: () => void;

  constructor(
    private readonly el: ElementRef<HTMLElement>,
    private readonly observer: IntersectionObserverService,
    private readonly renderer: Renderer2
  ) {}

  ngOnInit(): void {
    this.disconnect = this.observer.observe(this.el.nativeElement, entry => {
      if (entry.isIntersecting) {
        this.visible.emit();
        this.renderer.addClass(this.el.nativeElement, 'is-visible');
      }
    });
  }

  ngOnDestroy(): void {
    this.disconnect?.();
  }
}
```

## Best Practices
- Perform only dependency injection in constructor, move DOM access and side effects to `ngOnInit`
- Hold unsubscribe with `takeUntilDestroyed` or unsubscribe functions for asynchronous subscriptions to prevent leaks
- When depending on Input initial values, check first invocation in `ngOnChanges`

## Cautions
- `ngOnInit` is only called once, so use different hooks for re-rendering
- In SSR, DOM API doesn't exist, so perform browser detection if needed
- Running heavy processing synchronously blocks initial rendering, so be careful

## Related Technologies
- IntersectionObserver
- takeUntilDestroyed
- Renderer2
