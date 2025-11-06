# #454 "Auto Focus on Display"

## Overview
To auto focus on display, call `focus()` when the view is initialized to put the user in a state where they can immediately input.

## Learning Objectives
- Understand lifecycle for setting focus at display timing
- Learn guard methods to avoid errors in SSR environment
- Grasp techniques to ensure focus is applied with delayed execution

## Technical Points
- Execute `focus()` in `ngAfterViewInit`
- Delay with `requestAnimationFrame` or `setTimeout`
- Browser check with `isPlatformBrowser`

## 📺 On-Screen Code (for video)
```typescript
ngAfterViewInit(): void { requestAnimationFrame(() => this.el.nativeElement.focus()); }
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appAutoFocusOnInit]',
  standalone: true
})
export class AutoFocusOnInitDirective implements AfterViewInit {
  constructor(
    private readonly el: ElementRef<HTMLElement>,
    @Inject(PLATFORM_ID) private readonly platformId: Object
  ) {}

  ngAfterViewInit(): void {
    if (!isPlatformBrowser(this.platformId)) return;
    requestAnimationFrame(() => this.el.nativeElement.focus());
  }
}
```

## Best Practices
- Apply focus after DOM update with `requestAnimationFrame`
- Perform browser detection to avoid exceptions in SSR
- Specify delay time separately via Input for asynchronous displays like modals

## Considerations
- Limit to situations where focus is needed so as not to interfere with Tab key operations
- Consider UX as keyboard opens on focus in mobile browsers
- Conflicts occur when many focus directives exist on the same screen

## Related Technologies
- AfterViewInit
- PLATFORM_ID detection
- Modal focus management
