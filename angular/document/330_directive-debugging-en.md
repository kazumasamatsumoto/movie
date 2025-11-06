# #330 "Directive Debugging Methods"

## Overview
Directive debugging leverages conditional logging with `ngDevMode`, Angular DevTools, and test Spies to visualize lifecycle and host element state.

## Learning Objectives
- Understand effective tools and techniques for debugging
- Learn methods to verify lifecycle hooks and HostBinding
- Know debugging techniques in SSR and Hydration environments

## Technical Points
- Conditional logging with `ngDevMode` guard doesn't affect production builds
- Utilize Angular DevTools' Directive inspection tab
- Spy on HostBinding/Listener in unit tests

## 📺 On-Screen Code (for video)
```typescript
@Directive({ selector: '[appDebug]', standalone: true })
export class DebugDirective implements OnInit {
  ngOnInit(): void {
    if (ngDevMode) console.debug('DebugDirective init', this);
  }
}
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appDebug]',
  standalone: true
})
export class DebugDirective implements OnInit, OnDestroy {
  @Input() label = 'debug';
  private remove?: () => void;

  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2, private readonly zone: NgZone) {}

  ngOnInit(): void {
    if (ngDevMode) {
      console.debug(`[${this.label}] init`, this.el.nativeElement);
    }
    this.remove = this.renderer.listen(this.el.nativeElement, 'click', () => {
      if (ngDevMode) console.debug(`[${this.label}] click`, performance.now());
    });
  }

  ngOnDestroy(): void {
    this.remove?.();
    if (ngDevMode) {
      console.debug(`[${this.label}] destroy`);
    }
  }
}
```

## Best Practices
- Control logging with `ngDevMode` or environment variables, eliminating it in production
- Select host elements in Angular DevTools to verify Input/Output value changes
- In tests, verify event registration status using `spyOn(renderer, 'listen')`

## Considerations
- Excessive logging degrades performance, so output conditionally
- In SSR environments, `console` may be mocked, so provide error handling
- Don't leave debug attributes when shipping; check with build pipelines

## Related Technologies
- Angular DevTools
- ngDevMode
- Jasmine / Jest
