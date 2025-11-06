# #321 "Renderer2 Methods"

## Overview
Renderer2 provides various methods for DOM manipulation, allowing environment-independent handling of styles, classes, attributes, and event listeners.

## Learning Objectives
- Organize the major Renderer2 methods and their roles
- Understand when to use each method
- Utilize method return values (cleanup functions, etc.)

## Technical Points
- Use `setStyle`, `removeStyle` for style changes
- Use `addClass`, `removeClass` for class toggling
- Control attributes and events with `setAttribute`, `removeAttribute`, `listen`

## 📺 On-Screen Code (for video)
```typescript
@Directive({ selector: '[appRendererGuide]', standalone: true })
export class RendererGuideDirective implements OnInit {
  constructor(private readonly el: ElementRef<HTMLElement>, private readonly r: Renderer2) {}
  ngOnInit(): void {
    const host = this.el.nativeElement;
    this.r.setStyle(host, 'color', '#1f2937');
    this.r.addClass(host, 'is-ready');
    this.r.setAttribute(host, 'data-state', 'ready');
    this.r.listen(host, 'click', () => this.r.removeClass(host, 'is-ready'));
  }
}
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appRendererGuide]',
  standalone: true
})
export class RendererGuideDirective implements OnInit, OnDestroy {
  private removeClick?: () => void;

  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2) {}

  ngOnInit(): void {
    const host = this.el.nativeElement;
    this.renderer.setStyle(host, 'padding', '0.75rem 1rem');
    this.renderer.addClass(host, 'btn');
    this.renderer.addClass(host, 'btn--primary');
    this.renderer.setAttribute(host, 'role', 'button');
    this.removeClick = this.renderer.listen(host, 'click', () => {
      this.renderer.setStyle(host, 'opacity', '0.7');
      window.setTimeout(() => this.renderer.removeStyle(host, 'opacity'), 200);
    });
  }

  ngOnDestroy(): void {
    this.removeClick?.();
  }
}
```

## Best Practices
- When calling the same method consecutively, record the previous value and update only the diff
- Always retain the return value of `listen` and remove it in `ngOnDestroy`
- Separate responsibilities through method selection, prioritizing class assignment over `setStyle`

## Considerations
- Renderer2 is a synchronous API, so avoid heavy processing inside listeners
- Multiple directives manipulating the same property may conflict
- Expect that `listen` won't execute in SSR and verify behavior during browser initialization

## Related Technologies
- RendererStyleFlags2
- HostBinding / HostListener
- ChangeDetectorRef
