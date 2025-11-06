# #456 "InfiniteScroll Directive - Infinite Scroll"

## Overview
The InfiniteScroll directive triggers an event to load additional data when the scroll reaches the end, enabling automatic list expansion.

## Learning Objectives
- Understand the basic behavior and structure of infinite scroll
- Learn detection techniques using IntersectionObserver or scroll events
- Grasp the design of triggering data loading with Output events

## Technical Points
- IntersectionObserver monitoring sentinel element
- Accept offset and disable flag via Input
- Notify `loadMore` event with Output

## 📺 On-Screen Code (for video)
```typescript
@Output() scrolled = new EventEmitter<void>();
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appInfiniteScroll]',
  standalone: true
})
export class InfiniteScrollDirective implements OnInit, OnDestroy {
  @Input() disabled = false;
  @Input() rootMargin = '0px 0px 200px 0px';
  @Output() scrolled = new EventEmitter<void>();

  private observer?: IntersectionObserver;
  private sentinel!: HTMLElement;

  constructor(
    private readonly el: ElementRef<HTMLElement>,
    private readonly renderer: Renderer2,
    @Inject(PLATFORM_ID) private readonly platformId: Object
  ) {}

  ngOnInit(): void {
    if (!isPlatformBrowser(this.platformId)) return;
    this.sentinel = this.renderer.createElement('div');
    this.renderer.setStyle(this.sentinel, 'width', '100%');
    this.renderer.setStyle(this.sentinel, 'height', '1px');
    this.renderer.appendChild(this.el.nativeElement, this.sentinel);

    this.observer = new IntersectionObserver(entries => {
      if (this.disabled) return;
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          this.scrolled.emit();
        }
      });
    }, { root: this.el.nativeElement, rootMargin: this.rootMargin });

    this.observer.observe(this.sentinel);
  }

  ngOnDestroy(): void {
    this.observer?.disconnect();
  }
}
```

## Best Practices
- Improve performance using IntersectionObserver
- Make it possible to disable via Input to suppress events during loading
- Use sentinel element to avoid unnecessary scroll events

## Considerations
- Polyfill IntersectionObserver for older browsers
- Consider initial loading if list is short and immediately reaches end
- Guard to prevent multiple event fires while data is loading

## Related Technologies
- IntersectionObserver
- RxJS merge/concatMap for API calls
- Scroll container design
