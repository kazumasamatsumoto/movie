# #423 "Setting Default Values"

## Overview
Setting default values for Directive Input allows safe operation even when the consumer side doesn't pass values, lowering the adoption hurdle.

## Learning Objectives
- Understand default value setting patterns
- Learn how to apply fallbacks when not specified with `ngOnChanges`, etc.
- Understand the importance of explicitly documenting in documentation

## Technical Points
- Set basic values with property initialization
- Check null/undefined with Setter or `ngOnChanges`
- Utilize `??` operator and `??=`

## 📺 On-Screen Code (for video)
```typescript
@Input() appDelay = 150;
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appDelayHover]',
  standalone: true
})
export class DelayHoverDirective implements OnChanges {
  @Input() delay = 150;

  ngOnChanges(): void {
    if (this.delay < 0) {
      this.delay = 0;
    }
  }
}
```

## Best Practices
- Document default values clearly so users can understand expected behavior
- Take double safety measures with property initialization and validation
- Consider using `@Input({ transform: ... })` for value conversion

## Considerations
- `undefined` and `null` are handled differently, so distinguish clearly
- Use immutable constants when default values are complex objects
- Avoid conflicts when configuration is coordinated with external stores

## Related Technologies
- Angular Input Transform
- TypeScript nullish coalescing
- Directive API documentation
