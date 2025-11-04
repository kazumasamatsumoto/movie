# #320 "Renderer2 - Safe DOM Manipulation"

## Overview
Renderer2 is an abstracted DOM manipulation API provided by Angular, allowing safe operation while absorbing environment differences such as browsers, SSR, and Web Workers.

## Learning Objectives
- Understand the role and benefits of Renderer2
- Learn the purposes of main methods
- Study practical usage patterns combining with ElementRef

## Technical Points
- Obtain `Renderer2` through dependency injection
- Manipulate styles, attributes, classes, and listeners without environment dependency
- Hold unsubscribe functions for cleanup

## 📺 Display Code (For Video)
```typescript
@Directive({ selector: '[appElevate]', standalone: true })
export class ElevateDirective implements OnInit {
  constructor(private readonly el: ElementRef<HTMLElement>, private readonly r: Renderer2) {}
  ngOnInit(): void {
    const host = this.el.nativeElement;
    this.r.setStyle(host, 'transition', 'box-shadow .2s');
    this.r.listen(host, 'mouseenter', () => this.r.setStyle(host, 'boxShadow', '0 8px 24px rgba(15,23,42,.25)'));
  }
}
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
@Directive({
  selector: '[appElevate]',
  standalone: true
})
export class ElevateDirective implements OnInit, OnDestroy {
  private removeEnter?: () => void;
  private removeLeave?: () => void;

  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2) {}

  ngOnInit(): void {
    const host = this.el.nativeElement;
    this.renderer.setStyle(host, 'transition', 'box-shadow .2s');
    this.removeEnter = this.renderer.listen(host, 'mouseenter', () =>
      this.renderer.setStyle(host, 'boxShadow', '0 8px 24px rgba(15,23,42,.25)')
    );
    this.removeLeave = this.renderer.listen(host, 'mouseleave', () =>
      this.renderer.removeStyle(host, 'boxShadow')
    );
  }

  ngOnDestroy(): void {
    this.removeEnter?.();
    this.removeLeave?.();
  }
}
```

## Best Practices
- Delegate to Renderer2 instead of direct DOM manipulation to ensure platform compatibility
- Hold unsubscribe functions as properties and always call in `ngOnDestroy`
- Switch repeatedly applied styles to class assignment to reduce unnecessary inline styles

## Cautions
- Renderer2 is synchronous API, so heavy processing in listeners freezes UI
- Listeners are ignored in SSR, so verify browser initialization behavior
- Renderer2 is not a browser API, so there are limits to directly accessible functionality

## Related Technologies
- ElementRef
- HostBinding / HostListener
- Angular SSR
