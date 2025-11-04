# #318 "Using nativeElement"

## Overview
`ElementRef.nativeElement` points to the actual DOM node, allowing performance optimization through direct manipulation, but comes with platform dependency and security issues.

## Learning Objectives
- Understand risks and benefits of directly handling `nativeElement`
- Learn methods to verify environment before access
- Compare with alternatives like Renderer2

## Technical Points
- `nativeElement` may not be available in SSR or Web Workers
- Clarify element type with type casting
- Branch environments with `isPlatformBrowser` as needed

## 📺 Display Code (For Video)
```typescript
@Directive({ selector: '[appNativeSelect]', standalone: true })
export class NativeSelectDirective {
  constructor(private readonly el: ElementRef<HTMLSelectElement>) {}
  ngOnInit(): void {
    const select = this.el.nativeElement;
    if (select.options.length === 0) select.disabled = true;
  }
}
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
@Directive({
  selector: '[appNativeSelect]',
  standalone: true
})
export class NativeSelectDirective implements OnInit {
  constructor(
    private readonly el: ElementRef<HTMLSelectElement>,
    @Inject(PLATFORM_ID) private readonly platformId: Object
  ) {}

  ngOnInit(): void {
    if (!isPlatformBrowser(this.platformId)) return;
    const select = this.el.nativeElement;
    if (select.options.length === 0) {
      select.disabled = true;
      select.title = 'No options available';
    }
  }
}
```

## Best Practices
- Verify with `isPlatformBrowser` before touching `nativeElement` to prevent SSR breakage
- Use Renderer2 if possible, limiting `nativeElement` to minimal essential cases
- Revert side effects from DOM changes in `ngOnDestroy`

## Cautions
- Direct assignment increases XSS risk, so don't embed user input
- Manipulating styles without ViewEncapsulation causes side effects to spread
- In test environments, APIs may differ with JSDOM, etc., so add guards

## Related Technologies
- PLATFORM_ID
- isPlatformBrowser
- Renderer2
