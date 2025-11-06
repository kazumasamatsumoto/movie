# #430 "Configurable Implementation"

## Overview
Configurable directives receive option objects and merge with default settings to have flexibility to support diverse use cases.

## Learning Objectives
- Understand configurable implementation patterns
- Learn how to merge with default settings
- Understand validation and error handling on configuration changes

## Technical Points
- `@Input() options?: Partial<Settings>;`
- `const config = { ...DEFAULT, ...options };`
- Validate with `ngOnChanges` and throw logs or exceptions if necessary

## 📺 On-Screen Code (for video)
```typescript
@Input() appTooltipOptions?: Partial<TooltipOptions>;
```

## 💻 Detailed Implementation Example (for learning)
```typescript
interface RippleOptions {
  color: string;
  duration: number;
}

const DEFAULT_RIPPLE: RippleOptions = { color: '#38bdf8', duration: 250 };

@Directive({
  selector: '[appRipple]',
  standalone: true
})
export class RippleDirective implements OnChanges {
  @Input() appRipple?: Partial<RippleOptions>;
  private options = DEFAULT_RIPPLE;

  ngOnChanges(): void {
    this.options = { ...DEFAULT_RIPPLE, ...this.appRipple };
    if (this.options.duration < 0) {
      console.warn('[appRipple] duration must be >= 0');
      this.options = { ...this.options, duration: 0 };
    }
  }
}
```

## Best Practices
- Group configuration values in objects and constrain with types
- Decide handling for invalid values (revert to default, throw exception)
- Present configuration API clearly in documentation and Storybook

## Considerations
- Too many optional settings confuse users, keep to necessary minimum
- Update documentation with each change and avoid breaking changes
- Don't directly mutate configuration objects, treat immutably

## Related Technologies
- Partial type
- Storybook Controls
- OnChanges lifecycle
