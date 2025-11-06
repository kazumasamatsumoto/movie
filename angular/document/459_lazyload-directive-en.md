# #459 "LazyLoad Directive - Lazy Loading"

## Overview
The LazyLoad directive loads images and content when they enter the viewport, lightening the initial load. IntersectionObserver is the primary implementation method.

## Learning Objectives
- Understand the basic structure of LazyLoad directive
- Learn the mechanism of lazy loading with IntersectionObserver
- Incorporate placeholder display and error handling

## Technical Points
- Monitor element visibility with `IntersectionObserver`
- Accept original src and content URL via Input
- Unregister Observer after observation to save unnecessary processing

## 📺 On-Screen Code (for video)
```typescript
@Input() appLazyLoad = '';
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appLazyLoad]',
  standalone: true
})
export class LazyLoadDirective implements OnInit, OnDestroy {
  @Input() appLazyLoad = '';
  @Input() placeholder = '';

  private observer?: IntersectionObserver;

  constructor(
    private readonly el: ElementRef<HTMLImageElement>,
    @Inject(PLATFORM_ID) private readonly platformId: Object
  ) {}

  ngOnInit(): void {
    if (!isPlatformBrowser(this.platformId)) return;
    if (this.placeholder) {
      this.el.nativeElement.src = this.placeholder;
    }
    this.observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          this.el.nativeElement.src = this.appLazyLoad;
          this.observer?.disconnect();
        }
      });
    }, { rootMargin: '100px' });
    this.observer.observe(this.el.nativeElement);
  }

  ngOnDestroy(): void {
    this.observer?.disconnect();
  }
}
```

## Best Practices
- Set rootMargin to start loading slightly earlier
- Use in combination with placeholder image or `loading="lazy"`
- Set fallback image for errors

## Considerations
- Consider combining with `loading="lazy"` for supported browsers
- Prepare Polyfill for environments without IntersectionObserver support
- Always disconnect on component destruction to prevent memory leaks

## Related Technologies
- IntersectionObserver
- Loading attribute
- Web Performance optimization
