# #498 "Start/End Specification"

## Overview
In Range directive, receive start value (from) and end value (to) as Input to determine loop conditions. Flexible range iteration becomes possible when specifying step as well.

## Learning Objectives
- Understand Input design necessary for range specification
- Grasp relationship between from/to/step
- Learn input value validation methods

## Technical Points
- `@Input('appRangeFrom')`, `@Input('appRangeTo')`, `@Input('appRangeStep')`
- Invert step sign when from > to
- Throw error or apply default value when step is 0

## 📺 On-Screen Code (for video)
```typescript
const increasing = this.to >= this.from;
const step = increasing ? Math.abs(this.step) : -Math.abs(this.step);
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appRange]',
  standalone: true
})
export class RangeDirective implements OnChanges {
  @Input('appRangeFrom') from = 0;
  @Input('appRangeTo') to = 0;
  @Input('appRangeStep') step = 1;

  // ...(Same implementation as 497)
}
```

## Best Practices
- Set default values for Inputs to work safely even when undefined
- Issue error or warning when from/to/step combination is invalid
- Alert user when range is wide

## Considerations
- Possibility of infinite loop if not adjusting step sign
- Perform type check when values other than Number are passed
- Be mindful of floating-point errors when handling decimal steps

## Related Technologies
- RangeDirective
- TemplateRef / ViewContainerRef
- Structural Directive Input design
