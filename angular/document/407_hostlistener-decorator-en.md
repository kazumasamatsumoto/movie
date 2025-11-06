# #407 "@HostListener Decorator"

## Overview
The `@HostListener` decorator is a mechanism that directly binds event monitoring configuration to method declarations, specifying the event name and arguments in array format.

## Learning Objectives
- Understand decorator syntax and parameters
- Learn how to receive `$event` and DOM properties as arguments
- Learn how to design multiple event handling using decorators

## Technical Points
- `@HostListener('keydown', ['$event.key'])`
- Arguments specify `$event.property` like template strings
- Multiple decorators can be applied to the same method

## 📺 On-Screen Code (for video)
```typescript
@HostListener('keydown', ['$event.key'])
handleKey(key: string): void { console.log(key); }
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appKeyLogger]',
  standalone: true
})
export class KeyLoggerDirective {
  @HostListener('keydown', ['$event.key'])
  onKey(key: string): void {
    console.log('keydown:', key);
  }

  @HostListener('keyup', ['$event'])
  onKeyUp(event: KeyboardEvent): void {
    console.log('keyup with ctrl?', event.ctrlKey);
  }
}
```

## Best Practices
- Pass only necessary event information as arguments to keep methods testable
- Group decorator definitions at the beginning of the class to ensure readability
- Enhance safety by converting to typed arguments instead of `$event`

## Considerations
- When using `this` in HostListener, always define as class property
- Forgetting additional arguments results in `undefined`, causing unexpected behavior
- Events outside the tree structure are not listener targets, so document/window require separate settings

## Related Technologies
- EventEmitter
- Renderer2.listen
- Angular Signals
