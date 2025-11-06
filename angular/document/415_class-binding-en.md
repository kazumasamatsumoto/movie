# #415 "class Binding"

## Overview
Using `@HostBinding('class.class-name')` allows adding/removing classes to the host element, reflecting directive internal state to CSS styles.

## Learning Objectives
- Understand class binding syntax
- Learn how to coordinate state management with style application
- Understand patterns for managing multiple classes

## Technical Points
- Control addition/removal with boolean properties
- Evaluate complex conditions with getters
- Update state from HostListener to reflect classes

## 📺 On-Screen Code (for video)
```typescript
@HostBinding('class.is-active') active = false;
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appToggleClass]',
  standalone: true
})
export class ToggleClassDirective {
  @HostBinding('class.is-active') active = false;

  @HostListener('click')
  onClick(): void {
    this.active = !this.active;
  }
}
```

## Best Practices
- Follow BEM or project conventions for class names to avoid conflicts
- Manage with separate HostBindings when switching multiple classes
- Coordinate HostBinding with stylesheets and centralize display rules on the CSS side

## Considerations
- Overusing classes can lead to style conflicts, requiring design
- Reliably test logic that triggers state changes
- Verify that initial state classes are displayed correctly with SSR

## Related Technologies
- HostListener
- CSS BEM
- Renderer2.addClass/removeClass
