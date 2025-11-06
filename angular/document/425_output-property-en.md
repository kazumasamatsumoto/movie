# #425 "@Output() Property"

## Overview
Properties declared with `@Output()` can be published to the consumer side as event emitters, propagating events within the directive outward.

## Learning Objectives
- Understand Output property declaration method
- Learn event types and type-safe `emit` calls
- Understand design patterns for publishing as Observable

## Technical Points
- `@Output() change = new EventEmitter<MyEvent>();`
- Read-only publication with `change.asObservable()`
- Specify event name alias with `@Output('appChange')`

## 📺 On-Screen Code (for video)
```typescript
@Output('appToggle') toggled = new EventEmitter<boolean>();
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appPress]',
  standalone: true
})
export class PressDirective {
  @Output() appPress = new EventEmitter<{ x: number; y: number }>();

  @HostListener('click', ['$event'])
  onClick(event: MouseEvent): void {
    this.appPress.emit({ x: event.clientX, y: event.clientY });
  }
}
```

## Best Practices
- Define event payload types in separate files so consumer side can also reference
- Provide `readonly` accessor when publishing as Observable
- As Output fires asynchronously by default, document reasons if synchronous firing is needed

## Considerations
- Understand that EventEmitter is Angular-specific and differs from RxJS Subject
- Be careful with naming to avoid conflicts between Output and Input names
- Don't subscribe to Output internally (self-subscription causes leaks)

## Related Technologies
- EventEmitter vs Subject
- @Output alias
- Angular template binding
