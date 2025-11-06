# #422 "Directive Customization"

## Overview
Parameterizing Directives with Input/Output to allow external behavior configuration greatly improves reusability.

## Learning Objectives
- Understand basic strategy for Directive customization
- Learn design patterns for configuration objects
- Understand the importance of documenting customization points

## Technical Points
- Receive options with Input and merge with defaults
- Notify events with Output for consumer-side control
- Define configuration values with types to improve readability

## 📺 On-Screen Code (for video)
```typescript
@Input() appTooltip = { placement: 'top', delay: 200 };
```

## 💻 Detailed Implementation Example (for learning)
```typescript
export interface TooltipOptions {
  placement: 'top' | 'bottom' | 'left' | 'right';
  delay: number;
}

const DEFAULT_OPTIONS: TooltipOptions = { placement: 'top', delay: 150 };

@Directive({
  selector: '[appTooltip]',
  standalone: true
})
export class TooltipDirective implements OnChanges {
  @Input() appTooltip?: Partial<TooltipOptions>;
  private options: TooltipOptions = DEFAULT_OPTIONS;

  ngOnChanges(): void {
    this.options = { ...DEFAULT_OPTIONS, ...this.appTooltip };
  }
}
```

## Best Practices
- Receive configuration objects as `Partial` and merge with defaults
- Export Options type and default values so consumer side can also reference
- Update documentation and Storybook in response to changes

## Considerations
- Scrutinize requirements as unlimited options lead to excessive responsibilities
- Process differences with `ngOnChanges` if immediate reflection is needed on configuration changes
- Add validation for options to prevent invalid values

## Related Technologies
- Partial type
- Storybook Controls
- Directive API design
