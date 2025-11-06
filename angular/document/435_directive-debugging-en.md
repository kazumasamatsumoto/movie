# #435 "Directive Debugging"

## Overview
Directive debugging combines log output, Angular DevTools, and test reproduction to identify application omissions and event non-firing.

## Learning Objectives
- Understand debugging method options
- Learn lightweight verification techniques using `ngDevMode` and `console`
- Understand how to check directive state with DevTools

## Technical Points
- `if (ngDevMode) console.debug(...)`
- Check Directive tab in Angular DevTools
- Prepare reproduction scenarios in tests to prevent regressions

## 📺 On-Screen Code (for video)
```typescript
if (ngDevMode) console.debug('active', this.isActive);
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appDebug]',
  standalone: true
})
export class DebugDirective {
  @HostBinding('class.is-debug') debug = false;

  @HostListener('click')
  onClick(): void {
    this.debug = !this.debug;
    if (ngDevMode) {
      console.debug('[appDebug] toggled', this.debug);
    }
  }
}
```

## Best Practices
- Wrap debug logs with `ngDevMode` to exclude from production bundle
- During development, check directive application status in Angular DevTools Elements tab
- Incorporate debugging perspective into tests to ensure long-term reproducibility

## Considerations
- Excessive logging leads to performance degradation and information leaks, keep to minimum
- Guard as console may not exist in SSR environments
- Remove debug classes and attributes before shipping

## Related Technologies
- Angular DevTools
- Testing Library
- ngDevMode
