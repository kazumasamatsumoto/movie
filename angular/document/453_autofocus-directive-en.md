# #453 "AutoFocus Directive - Auto Focus"

## Overview
The AutoFocus directive provides functionality to automatically focus on an element when it is displayed, improving usability of forms and modals.

## Learning Objectives
- Understand the basics of auto focus processing
- Learn lifecycle hooks to focus immediately after display
- Grasp how to execute focus limited to browser environment

## Technical Points
- `nativeElement.focus()` in `ngAfterViewInit` or `ngOnInit`
- Do not execute focus in SSR
- Can set delay time or conditions via Input

## 📺 On-Screen Code (for video)
```typescript
ngAfterViewInit(): void { queueMicrotask(() => this.el.nativeElement.focus()); }
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appAutoFocus]',
  standalone: true
})
export class AutoFocusDirective implements AfterViewInit {
  @Input() appAutoFocus = true;
  @Input() focusDelay = 0;

  constructor(
    private readonly el: ElementRef<HTMLElement>,
    @Inject(PLATFORM_ID) private readonly platformId: Object
  ) {}

  ngAfterViewInit(): void {
    if (!this.appAutoFocus || !isPlatformBrowser(this.platformId)) return;
    window.setTimeout(() => this.el.nativeElement.focus(), this.focusDelay);
  }
}
```

## Best Practices
- Control focus presence and delay time via Input for flexibility
- Limit to browser environment with `isPlatformBrowser`
- Provide appropriate delay for asynchronous rendering like modal display

## Considerations
- Forced focus takes control from user, so limit to necessary situations
- Focus may not work on iOS input elements
- Always perform environment check as DOM does not exist in SSR

## Related Technologies
- AfterViewInit
- PLATFORM_ID / isPlatformBrowser
- FocusTrap
