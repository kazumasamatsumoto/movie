# #418 "HostListener + HostBinding"

## Overview
The combination of monitoring events with HostListener and reflecting state to DOM with HostBinding is the basic pattern for implementing interactive directives.

## Learning Objectives
- Understand the coordination flow between HostListener and HostBinding
- Learn best practices for updating state
- Understand how to test reflection to UI

## Technical Points
- State update with HostListener → DOM reflection with HostBinding
- Hold state with properties or signals
- Separate responsibilities for events and display

## 📺 On-Screen Code (for video)
```typescript
@HostBinding('class.is-active') active = false;
@HostListener('click') toggle(): void { this.active = !this.active; }
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appHoverToggle]',
  standalone: true
})
export class HoverToggleDirective {
  @HostBinding('class.is-hover') hover = false;

  @HostListener('mouseenter')
  onEnter(): void {
    this.hover = true;
  }

  @HostListener('mouseleave')
  onLeave(): void {
    this.hover = false;
  }
}
```

## Best Practices
- Perform state updates synchronously when possible, manage explicitly when async processing is needed
- Make HostBinding values read-only properties and express with immutable data
- Verify event firing → DOM change coordination in tests

## Considerations
- Delegate to services or Signals when state becomes complex
- Be careful with order when multiple directives process the same event
- Match initial display state as events don't fire with SSR

## Related Technologies
- Angular Signals
- EventEmitter
- Testing Library
