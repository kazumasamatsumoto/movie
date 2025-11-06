# #413 "HostBinding - Property Binding"

## Overview
`HostBinding` is a mechanism that binds directive properties to host element properties, attributes, classes, and styles, allowing state synchronization without using Renderer2.

## Learning Objectives
- Understand the basic concept of HostBinding
- Learn the specifiable property formats (class/style/attr, etc.)
- Understand state update methods coordinated with lifecycle

## Technical Points
- `@HostBinding('class.active') isActive = false;`
- `@HostBinding('style.opacity') opacity = '1';`
- Automatically reflected to DOM when property value is updated

## 📺 On-Screen Code (for video)
```typescript
@HostBinding('class.is-open') isOpen = false;
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appAccordionToggle]',
  standalone: true
})
export class AccordionToggleDirective {
  @HostBinding('class.is-open') isOpen = false;

  toggle(): void {
    this.isOpen = !this.isOpen;
  }
}
```

## Best Practices
- Declare classes and attributes representing host element state declaratively with HostBinding
- Define multiple properties together for readability when managing them
- Prioritize HostBinding over direct manipulation with Renderer2 to reduce code

## Considerations
- Returning NULL with HostBinding removes the property, so use intentionally
- Frequently updated properties may affect performance
- Properties that cannot be reflected to DOM (methods, etc.) cannot be bound

## Related Technologies
- HostListener
- Renderer2
- Angular Lifecycle Hooks
