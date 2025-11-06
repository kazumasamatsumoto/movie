# #327 "SSR-Compatible DOM Manipulation"

## Overview
In SSR environments, the DOM doesn't exist, so directives need to guard execution to browser-only and avoid differences during Hydration.

## Learning Objectives
- Understand the constraints of DOM manipulation faced in SSR
- Learn implementation patterns that branch between SSR and browser
- Minimize side effects in combination with Hydration

## Technical Points
- Browser detection with `isPlatformBrowser`
- Data sharing between SSR and browser using `APP_ID` or `TransferState`
- Align side effects between initial rendering and browser initialization

## 📺 On-Screen Code (for video)
```typescript
@Directive({ selector: '[appHydrateSafe]', standalone: true })
export class HydrateSafeDirective implements OnInit {
  private readonly platformId = inject(PLATFORM_ID);
  constructor(private readonly el: ElementRef<HTMLElement>, private readonly r: Renderer2) {}
  ngOnInit(): void {
    if (!isPlatformBrowser(this.platformId)) return;
    this.r.addClass(this.el.nativeElement, 'hydrated');
  }
}
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Injectable({ providedIn: 'root' })
export class HydrationStateService {
  private readonly key = makeStateKey<boolean>('hydrated-flag');
  constructor(private readonly state: TransferState) {}
  hasHydrated(): boolean {
    return this.state.get(this.key, false);
  }
  markHydrated(): void {
    this.state.set(this.key, true);
  }
}

@Directive({
  selector: '[appHydrateSafe]',
  standalone: true
})
export class HydrateSafeDirective implements OnInit {
  private readonly platformId = inject(PLATFORM_ID);

  constructor(
    private readonly el: ElementRef<HTMLElement>,
    private readonly renderer: Renderer2,
    private readonly hydrationState: HydrationStateService
  ) {}

  ngOnInit(): void {
    if (!isPlatformBrowser(this.platformId)) return;
    if (!this.hydrationState.hasHydrated()) {
      this.renderer.addClass(this.el.nativeElement, 'hydrated');
      this.hydrationState.markHydrated();
    }
  }
}
```

## Best Practices
- Don't produce side effects during SSR, only make minimal changes during browser initialization
- To avoid Hydration errors, match HTML structure and attributes with SSR time
- When state sharing is needed, pass data with `TransferState`

## Considerations
- Calling `requestAnimationFrame` or `window` during SSR will cause exceptions
- Modifying the DOM before hydration creates differences and causes flash
- Consider fallbacks when lazy-loaded directives only work on the client side

## Related Technologies
- Angular Universal
- TransferState
- Hydration
