# #406 "HostListener - Event Monitoring"

## Overview
`HostListener` is a decorator that allows directives to concisely monitor host element events, enabling safe event handling implementation without writing `addEventListener`.

## Learning Objectives
- Understand the basic role of HostListener
- Learn how to specify event names and arguments
- Know the importance of event management along the lifecycle

## Technical Points
- `@HostListener('eventName', ['arg'])`
- Bind events without requiring DI
- Methods decorated are automatically unbound when Directive is destroyed

## 📺 On-Screen Code (for video)
```typescript
@HostListener('click') handleClick(): void { console.log('clicked'); }
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appLogClick]',
  standalone: true
})
export class LogClickDirective {
  @HostListener('click', ['$event'])
  handleClick(event: MouseEvent): void {
    console.log('[appLogClick]', event.target);
  }
}
```

## Best Practices
- Event names should be lowercase in compliance with DOM events
- Receive only necessary arguments like `['$event']` to keep functions lightweight
- When monitoring multiple events, separate methods to clarify responsibilities

## Considerations
- Putting heavy logic in event handlers delays UI, so delegate to services
- Be careful with names when handling custom events triggered outside Angular
- HostListener only applies to the host element, child element events require separate handling

## Related Technologies
- HostBinding
- Renderer2.listen
- Angular Lifecycle Hooks
