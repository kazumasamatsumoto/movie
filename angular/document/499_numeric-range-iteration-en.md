# #499 "Numeric Range Iteration"

## Overview
In numeric range iteration, generate numbers according to specified from/to/step and pass to template for repeated display. Important to control loop condition according to range direction.

## Learning Objectives
- Understand numeric range loop logic
- Learn determination method for step direction and termination condition
- Provide boolean flags (first/last etc.) with Context object

## Technical Points
- Determine if increasing or decreasing direction
- `value += effectiveStep` in for loop
- Calculate last/first flags and add to Context

## 📺 On-Screen Code (for video)
```typescript
for (let value = from, index = 0; increasing ? value <= to : value >= to; value += step, index++) { ... }
```

## 💻 Detailed Implementation Example (for learning)
```typescript
interface RangeContext {
  $implicit: number;
  index: number;
  first: boolean;
  last: boolean;
}

@Directive({
  selector: '[appRange]',
  standalone: true
})
export class RangeDirective implements OnChanges {
  @Input('appRangeFrom') from = 0;
  @Input('appRangeTo') to = 0;
  @Input('appRangeStep') step = 1;

  constructor(
    private readonly template: TemplateRef<RangeContext>,
    private readonly viewContainer: ViewContainerRef
  ) {}

  ngOnChanges(): void {
    this.viewContainer.clear();
    if (this.step === 0) {
      throw new Error('step must not be 0');
    }
    const increasing = this.to >= this.from;
    const step = increasing ? Math.abs(this.step) : -Math.abs(this.step);
    const values: number[] = [];
    for (let value = this.from; increasing ? value <= this.to : value >= this.to; value += step) {
      values.push(value);
    }
    values.forEach((value, index) => {
      this.viewContainer.createEmbeddedView(this.template, {
        $implicit: value,
        index,
        first: index === 0,
        last: index === values.length - 1
      });
    });
  }
}
```

## Best Practices
- Provide supplementary information like index/first/last in context
- Be mindful of performance even when range is large, consider virtual scroll if needed
- Alert as loop count increases when step absolute value is small

## Considerations
- Consider rounding process as terminal may not match with floating-point steps
- Infinite loop if step sign is wrong in reverse direction loop
- Don't forget destruction if holding ViewRef reference after loop

## Related Technologies
- TemplateRef/Context
- ViewContainerRef
- RangeDirective
