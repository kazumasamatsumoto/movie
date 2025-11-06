# #414 "@HostBinding Decorator"

## Overview
The `@HostBinding` decorator is syntax for binding properties within a directive to specific properties of the host element, making it easy to switch classes and styles.

## Learning Objectives
- Understand `@HostBinding` syntax
- Learn examples of class, style, and attribute binding
- Understand the flow where DOM changes through internal state updates

## Technical Points
- `@HostBinding('class.some')`
- `@HostBinding('style.backgroundColor')`
- `@HostBinding('attr.aria-expanded')`

## 📺 On-Screen Code (for video)
```typescript
@HostBinding('attr.aria-expanded') get ariaExpanded(): 'true' | 'false' { return this.open ? 'true' : 'false'; }
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appAriaToggle]',
  standalone: true
})
export class AriaToggleDirective {
  private open = false;

  @HostBinding('attr.aria-expanded')
  get ariaExpanded(): 'true' | 'false' {
    return this.open ? 'true' : 'false';
  }

  toggle(): void {
    this.open = !this.open;
  }
}
```

## Best Practices
- Return computed values with getters to synchronize state and display
- Specify binding names explicitly to improve readability
- Combine HostBinding and HostListener to implement reactive behavior

## Considerations
- Specifying a non-existent property as the binding target causes runtime errors
- When using getters, avoid side effects and purely return values
- Don't perform heavy calculations within getters for performance

## Related Technologies
- HostListener
- Accessibility attributes
- ChangeDetectionStrategy
