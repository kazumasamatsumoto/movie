# #319 "Cautions for Direct DOM Manipulation"

## Overview
Direct DOM manipulation is fast but requires careful handling as it risks platform dependency, security issues, and change detection breakdown.

## Learning Objectives
- Enumerate risks caused by direct DOM manipulation
- Master guarding methods for safe DOM handling
- Understand alternatives through coordination with Renderer2 and Signals

## Technical Points
- DOM APIs don't exist in SSR/Web Worker
- Consider sanitization or `innerText` use for XSS protection
- Use ChangeDetectorRef to synchronize UI updates

## 📺 Display Code (For Video)
```typescript
@Directive({ selector: '[appUnsafeDom]', standalone: true })
export class UnsafeDomDirective {
  constructor(private readonly el: ElementRef<HTMLElement>) {}
  ngOnInit(): void {
    if (typeof window === 'undefined') return;
    this.el.nativeElement.innerHTML = '<strong>Dangerous</strong>';
  }
}
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
@Directive({
  selector: '[appSafeDom]',
  standalone: true
})
export class SafeDomDirective implements OnInit {
  @Input({ alias: 'appSafeDom', required: true }) content!: string;

  constructor(
    private readonly renderer: Renderer2,
    private readonly el: ElementRef<HTMLElement>,
    @Inject(PLATFORM_ID) private readonly platformId: Object,
    private readonly sanitizer: DomSanitizer
  ) {}

  ngOnInit(): void {
    if (!isPlatformBrowser(this.platformId)) return;
    const safe = this.sanitizer.sanitize(SecurityContext.HTML, this.content) ?? '';
    this.renderer.setProperty(this.el.nativeElement, 'innerHTML', safe);
  }
}
```

## Best Practices
- Avoid direct DOM manipulation if expressible with Renderer2 or Angular template syntax
- When necessary, perform environment checks and sanitization to ensure safety
- Use `NgZone.run` or Signals to synchronize with UI when change detection is needed

## Cautions
- Prepare wrappers to control when external libraries rewrite DOM
- APIs like innerHTML or insertAdjacentHTML have high XSS risk
- DOM API behavior differs in some environments like mobile WebView

## Related Technologies
- DomSanitizer
- PLATFORM_ID
- ChangeDetectorRef
