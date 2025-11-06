# #328 "Directive Best Practices"

## Overview
Directives improve reusability and safety by keeping responsibilities small, abstracting DOM operations, and managing clean lifecycles.

## Learning Objectives
- Systematically understand principles to emphasize in Directive design
- Learn implementation of clean lifecycle management
- Know techniques for maintaining quality through testing and documentation

## Technical Points
- Side-effect management with Renderer2 and DestroyRef
- Define clear contracts with Input/Output
- Ensure safety with platform detection and sanitization

## 📺 On-Screen Code (for video)
```typescript
@Directive({ selector: '[appBestDirective]', standalone: true })
export class BestDirective {
  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2, destroyRef: DestroyRef) {
    const off = this.renderer.listen(this.el.nativeElement, 'focus', () => {});
    destroyRef.onDestroy(off);
  }
}
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appAccessibleTooltip]',
  standalone: true
})
export class AccessibleTooltipDirective implements OnInit {
  @Input({ alias: 'appAccessibleTooltip', required: true }) message!: string;
  @Input() placement: 'top' | 'bottom' = 'top';
  private readonly platformId = inject(PLATFORM_ID);
  private cleanup: VoidFunction[] = [];

  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2, destroyRef: DestroyRef) {
    destroyRef.onDestroy(() => this.cleanup.forEach(fn => fn()));
  }

  ngOnInit(): void {
    if (!isPlatformBrowser(this.platformId)) return;
    const host = this.el.nativeElement;
    this.renderer.setAttribute(host, 'role', 'tooltip');
    this.renderer.setAttribute(host, 'data-placement', this.placement);
    this.cleanup.push(this.renderer.listen(host, 'focus', () => this.renderer.addClass(host, 'is-active')));
    this.cleanup.push(this.renderer.listen(host, 'blur', () => this.renderer.removeClass(host, 'is-active')));
  }
}
```

## Best Practices
- Limit responsibilities to UI behavior and delegate business logic to services or Signals
- Leverage DestroyRef and removal functions to reliably clean up side effects
- Give inputs types and defaults, and document the API contract
- Eliminate environment-dependent code with Renderer2 and platform detection

## Considerations
- If a Directive becomes bloated, consider component separation or service extraction
- Forgetting to remove event listeners or timers leads directly to memory leaks
- Without sharing usage rules, other teams may misuse them, so communicate with sample code or Storybook

## Related Technologies
- DestroyRef
- Angular Style Guide
- Storybook / Documentation maintenance
