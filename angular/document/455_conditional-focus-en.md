# #455 "Conditional Focus"

## Overview
Conditional focus applies focus only when the condition received via Input is true, enabling scenarios like focus guidance during validation errors.

## Learning Objectives
- Understand the mechanism of conditional focus
- Learn implementation combining Input and lifecycle
- Grasp focus guidance patterns linked with validation

## Technical Points
- `@Input() appAutoFocusIf = false;`
- Evaluate condition and focus in `ngOnChanges`
- Avoid unnecessary refocus when already focused

## 📺 On-Screen Code (for video)
```typescript
@Input() appAutoFocusIf = false;
ngOnChanges(): void { if (this.appAutoFocusIf) this.focus(); }
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appAutoFocusIf]',
  standalone: true
})
export class AutoFocusIfDirective implements OnChanges {
  @Input() appAutoFocusIf = false;
  @Input() focusDelay = 0;
  private focused = false;

  constructor(
    private readonly el: ElementRef<HTMLElement>,
    @Inject(PLATFORM_ID) private readonly platformId: Object
  ) {}

  ngOnChanges(): void {
    if (!isPlatformBrowser(this.platformId)) return;
    if (this.appAutoFocusIf && !this.focused) {
      setTimeout(() => {
        this.el.nativeElement.focus();
        this.focused = true;
      }, this.focusDelay);
    } else if (!this.appAutoFocusIf) {
      this.focused = false;
    }
  }
}
```

## Best Practices
- Record whether already focused to avoid unnecessary refocus
- Set delay time and conditions via Input for flexibility
- Improve UX by guiding focus during validation errors

## Considerations
- UX degrades when focus/blur repeats if state changes frequently, so scrutinize conditions
- Browser check needed as it errors in SSR
- Handle focus control carefully so as not to interfere with user operations

## Related Technologies
- OnChanges
- Angular Forms validation
- Accessibility (focus management)
