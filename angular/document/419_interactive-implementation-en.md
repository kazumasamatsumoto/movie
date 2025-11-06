# #419 "Interactive Implementation"

## Overview
By combining event monitoring and state reflection, interactive UI such as hover, toggle, and focus highlights can be reused as directives.

## Learning Objectives
- Understand representative interactive patterns
- Learn design for state management and DOM reflection
- Understand considerations for incorporating into design systems

## Technical Points
- Get events with HostListener, update styles/classes with HostBinding
- Receive configuration values with Input to support multiple scenarios
- Notify interaction results externally with Output

## 📺 On-Screen Code (for video)
```typescript
@HostListener('focus') onFocus(): void { this.focused = true; }
@HostBinding('class.is-focus') focused = false;
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appInteractiveCard]',
  standalone: true
})
export class InteractiveCardDirective {
  @HostBinding('class.is-active') active = false;

  @HostListener('click')
  onClick(): void {
    this.active = !this.active;
  }

  @HostListener('keyup.enter')
  onEnter(): void {
    this.active = !this.active;
  }
}
```

## Best Practices
- Support both mouse and keyboard operations to ensure accessibility
- Synchronize state externally with Input/Output for easier control
- Clearly document usage examples and constraints in design system

## Considerations
- Be careful of duplicate event processing and consider if stop control is needed within handlers
- Update ARIA attributes to convey information, not just visual changes
- Clarify reset timing when holding state internally

## Related Technologies
- HostListener/HostBinding
- EventEmitter
- Accessibility
