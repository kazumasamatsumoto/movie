# #317 "ElementRef - Element Reference"

## Overview
`ElementRef` is a class that encapsulates references to host elements, providing access to DOM nodes through the `nativeElement` property.

## Learning Objectives
- Understand the role and mechanism of ElementRef
- Learn how to safely handle DOM elements with type parameters
- Understand recommended patterns combining with Renderer2

## Technical Points
- Can specify type like `ElementRef<HTMLElement>`
- Prioritize Renderer2 over direct DOM manipulation
- In tests, easily reproduce with `new ElementRef(document.createElement('div'))`

## 📺 Display Code (For Video)
```typescript
@Directive({ selector: '[appFocusRing]', standalone: true })
export class FocusRingDirective {
  constructor(private readonly el: ElementRef<HTMLButtonElement>, private readonly renderer: Renderer2) {}
  ngOnInit(): void {
    this.renderer.setStyle(this.el.nativeElement, 'outline', '2px solid #38bdf8');
  }
}
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
@Directive({
  selector: '[appFocusRing]',
  standalone: true
})
export class FocusRingDirective implements OnInit, OnDestroy {
  @Input() appFocusRing = '#38bdf8';
  private removeFocus?: () => void;
  private removeBlur?: () => void;

  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2) {}

  ngOnInit(): void {
    const host = this.el.nativeElement;
    this.renderer.setStyle(host, 'outline', `2px solid ${this.appFocusRing}`);
    this.removeFocus = this.renderer.listen(host, 'focus', () => this.renderer.setStyle(host, 'outline-style', 'solid'));
    this.removeBlur = this.renderer.listen(host, 'blur', () => this.renderer.setStyle(host, 'outline-style', 'dashed'));
  }

  ngOnDestroy(): void {
    this.removeFocus?.();
    this.removeBlur?.();
    this.renderer.removeStyle(this.el.nativeElement, 'outline');
  }
}
```

## Best Practices
- Make target element explicit with type parameter to improve type safety when using `nativeElement`
- Do DOM manipulation via Renderer2, limiting `ElementRef` to obtaining element references only
- In tests, generate elements with `document.createElement` and pass to `ElementRef` for verification

## Cautions
- Holding `ElementRef` in services causes memory leaks, so limit to within Directive
- In SSR, `nativeElement` may be undefined, so check before access
- Passing directly to external libraries risks the library destroying DOM

## Related Technologies
- Renderer2
- Dependency Injection
- Angular Testing Utilities
