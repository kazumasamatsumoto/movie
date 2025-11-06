# #460 "Image Lazy Load"

## Overview
In image lazy loading, monitor image elements with IntersectionObserver and set the `src` attribute to start download when they enter the display area. Can also add placeholder and fade-in effects.

## Learning Objectives
- Understand specific implementation of image lazy loading
- Learn how to switch between placeholder and actual image
- Grasp benefits of improving network performance

## Technical Points
- Hold original URL in `data-src` etc.
- Detect display timing with IntersectionObserver
- Use browser native functionality in combination with `loading="lazy"`

## 📺 On-Screen Code (for video)
```html
<img appLazyLoad [appLazyLoad]="imageUrl" placeholder="assets/placeholder.jpg" />
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: 'img[appLazyLoad]',
  standalone: true
})
export class ImageLazyLoadDirective implements OnInit, OnDestroy {
  @Input() appLazyLoad = '';
  @Input() placeholder = '';
  @Input() fadeIn = true;
  private observer?: IntersectionObserver;

  constructor(
    private readonly el: ElementRef<HTMLImageElement>,
    @Inject(PLATFORM_ID) private readonly platformId: Object
  ) {}

  ngOnInit(): void {
    if (!isPlatformBrowser(this.platformId)) return;
    const img = this.el.nativeElement;
    if (this.placeholder) {
      img.src = this.placeholder;
    }
    if (this.fadeIn) {
      img.style.transition = 'opacity .3s ease';
      img.style.opacity = '0';
    }
    this.observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          img.src = this.appLazyLoad;
          img.onload = () => {
            if (this.fadeIn) {
              img.style.opacity = '1';
            }
          };
          this.observer?.disconnect();
        }
      });
    }, { rootMargin: '200px 0px' });
    this.observer.observe(img);
  }

  ngOnDestroy(): void {
    this.observer?.disconnect();
  }
}
```

## Best Practices
- Prevent visual blank during loading with placeholder
- Make rootMargin larger to start loading earlier and prevent flicker during scrolling
- Adding fade-in effect on onload improves UX

## Considerations
- Image src is not set in SSR leaving only placeholder, so consider prerendering if needed
- Polyfill needed for environments without IntersectionObserver support
- Consider fallback image for errors

## Related Technologies
- IntersectionObserver
- loading="lazy"
- Further optimization with WebP/AVIF support
