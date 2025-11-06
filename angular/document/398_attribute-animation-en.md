# #398 "Combination with Animation"

## Overview
Using Attribute Directives makes it easier to reuse animations by switching CSS classes on specific events or calling the Angular Animation API.

## Learning Objectives
- Understand the benefits of making animations into directives
- Learn how to implement CSS animations through class switching with Renderer2
- Grasp coordination with Angular Animation API

## Technical Points
- Control triggers with `renderer.addClass/removeClass`
- Manage IntersectionObserver and scroll events with directives
- DI `AnimationBuilder` to programmatically start animations

## 📺 Display Code (for video)
```typescript
@Directive({ selector: '[appFadeOnHover]', standalone: true })
export class FadeOnHoverDirective {
  constructor(private readonly r: Renderer2, private readonly el: ElementRef<HTMLElement>) {}
  ngOnInit(): void {
    this.r.listen(this.el.nativeElement, 'mouseenter', () => this.r.addClass(this.el.nativeElement, 'is-fade'));
  }
}
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appRevealOnScroll]',
  standalone: true
})
export class RevealOnScrollDirective implements OnInit, OnDestroy {
  private observer?: IntersectionObserver;

  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2) {}

  ngOnInit(): void {
    this.renderer.addClass(this.el.nativeElement, 'is-hidden');
    this.observer = new IntersectionObserver(entries => {
      for (const entry of entries) {
        if (entry.isIntersecting) {
          this.renderer.addClass(this.el.nativeElement, 'is-revealed');
          this.renderer.removeClass(this.el.nativeElement, 'is-hidden');
          this.observer?.disconnect();
        }
      }
    }, { threshold: 0.2 });
    this.observer.observe(this.el.nativeElement);
  }

  ngOnDestroy(): void {
    this.observer?.disconnect();
  }
}
```

## Best Practices
- Define CSS animation classes and let directives focus on triggers
- Perform browser checks for native APIs like IntersectionObserver and consider polyfills
- Abstract animations you want to reuse with `AnimationBuilder` in testable form

## Considerations
- IntersectionObserver doesn't work in SSR, so guard with `isPlatformBrowser`
- Organize naming to avoid class conflicts during animations
- For animations affecting performance, use GPU-friendly properties

## Related Technologies
- Angular Animation API
- IntersectionObserver
- CSS Transitions/Animations
