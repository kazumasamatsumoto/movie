# #309 "@Directive Decorator"

## Overview
The `@Directive` decorator provides Angular with directive metadata, declaring configuration information such as selector, dependent services, and host settings.

## Learning Objectives
- Understand main properties that can be specified in the `@Directive` decorator
- Learn how to configure host metadata and providers
- Understand configuration required for Standalone directives

## Technical Points
- Define application target with `selector`
- Adjust behavior with `standalone`, `host`, `providers`, `exportAs`, etc.
- Decorator is analyzed at compile time as TypeScript metadata

## 📺 Display Code (For Video)
```typescript
@Directive({
  selector: '[appTooltip]',
  standalone: true,
  host: { '(mouseenter)': 'show()', '(mouseleave)': 'hide()', '[attr.aria-hidden]': '!visible' }
})
export class TooltipDirective {
  visible = false;
  show(): void { this.visible = true; }
  hide(): void { this.visible = false; }
}
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
export const TOOLTIP_REF = new InjectionToken<TooltipDirective>('TOOLTIP_REF');

@Directive({
  selector: '[appTooltip]',
  standalone: true,
  exportAs: 'appTooltip',
  host: { '(focus)': 'show()', '(blur)': 'hide()', '[class.tooltip-open]': 'visible' },
  providers: [{ provide: TOOLTIP_REF, useExisting: TooltipDirective }]
})
export class TooltipDirective {
  visible = false;

  constructor(private readonly overlay: TooltipOverlayService) {}

  show(): void {
    if (this.visible) return;
    this.visible = true;
    this.overlay.open(this);
  }

  hide(): void {
    if (!this.visible) return;
    this.visible = false;
    this.overlay.close(this);
  }
}

@Component({
  selector: 'app-tooltip-demo',
  standalone: true,
  imports: [CommonModule, TooltipDirective],
  template: `
    <button appTooltip #tooltip="appTooltip">Show on focus</button>
    <p>Status: {{ tooltip.visible }}</p>
  `
})
export class TooltipDemoComponent {}
```

## Best Practices
- Consolidate HostBinding/HostListener equivalent settings in one place with `host` property
- Use `providers` to expose tokens for coordination between multiple Directives
- Provide template references with `exportAs` without leaking logic externally

## Cautions
- When using `useExisting` in `providers`, be careful of circular references
- Keep methods called in `host` property lightweight to ensure performance
- After metadata changes, verify in tests that there are no breaking changes to selector or export names

## Related Technologies
- InjectionToken
- HostBinding / HostListener
- Standalone Directives
