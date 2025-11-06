# #424 "Event Firing with Output"

## Overview
Defining EventEmitter with `@Output()` allows directives to notify events to the consumer side, enabling synchronization of UI state with external systems.

## Learning Objectives
- Understand Output declaration and emit method
- Learn design guidelines for custom events
- Understand bidirectional patterns through coordination of Output and Input

## Technical Points
- `@Output() toggled = new EventEmitter<boolean>();`
- Notify with `this.toggled.emit(true)`
- Design is also possible to publish `EventEmitter` as Observable

## 📺 On-Screen Code (for video)
```typescript
@Output() appToggle = new EventEmitter<boolean>();
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appToggle]',
  standalone: true
})
export class ToggleDirective {
  @Output() appToggle = new EventEmitter<boolean>();
  private state = false;

  @HostListener('click')
  onClick(): void {
    this.state = !this.state;
    this.appToggle.emit(this.state);
  }
}
```

## Best Practices
- Use event names like `appSomething` or `somethingChange` to clearly show contract
- Share event payload types in type files to enhance consumer-side safety
- Adopt `@Output() valueChange` pattern if bidirectional binding is needed

## Considerations
- Be careful as `new EventEmitter(true)` makes it fire synchronously
- Control with `auditTime`, etc. when events occur frequently
- Document cases where Output doesn't fire (disabled state, etc.)

## Related Technologies
- EventEmitter
- Signals and Output
- Bidirectional binding
