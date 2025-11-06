# #497 "Range Directive - Range Specification"

## Overview
The Range directive is a structural directive that iterates numeric range by specifying start and end values, providing values within range to template.

## Learning Objectives
- Understand design of structural directive handling numeric ranges
- Learn Input design like `from`/`to`/`step`
- Grasp how to sequentially generate values within range with ViewContainerRef

## Technical Points
- `@Input() appRangeFrom`, `@Input() appRangeTo`, `@Input() appRangeStep`
- Call `createEmbeddedView` in loop to pass values
- Consider step sign and termination condition

## 📺 On-Screen Code (for video)
```html
<li *appRange="let n from 1 to 5">{{ n }}</li>
```

## 💻 Detailed Implementation Example (for learning)
```typescript
interface RangeContext {
  $implicit: number;
  index: number;
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
      throw new Error('appRangeStep must not be 0');
    }
    const increasing = this.to >= this.from;
    const effectiveStep = increasing ? Math.abs(this.step) : -Math.abs(this.step);
    let index = 0;
    for (let value = this.from; increasing ? value <= this.to : value >= this.to; value += effectiveStep) {
      this.viewContainer.createEmbeddedView(this.template, { $implicit: value, index });
      index++;
    }
  }
}
```

## Best Practices
- Error when step is 0 and communicate clearly to user
- Automatically adjust step sign when range is reversed (from > to)
- Can also provide index and `first`/`last` in Context

## Considerations
- Document upper limit as DOM becomes bloated when generating large range
- Implement synchronously to get same result in SSR
- Always clear previous views when Input updates

## Related Technologies
- TemplateRef
- ViewContainerRef
- Context object
