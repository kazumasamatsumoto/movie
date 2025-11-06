# #412 "Using preventDefault()"

## Overview
`preventDefault()` is a method that suppresses the default action of an event, allowing control of link navigation and form submission by calling it within HostListener.

## Learning Objectives
- Understand the role of `preventDefault()`
- Learn usage examples within HostListener
- Understand the difference from `stopPropagation()`

## Technical Points
- Disable default action with `event.preventDefault()`
- Stop bubbling with `event.stopPropagation()`
- Use appropriately with consideration for user experience in input control

## 📺 On-Screen Code (for video)
```typescript
@HostListener('click', ['$event']) onClick(event: MouseEvent) { event.preventDefault(); }
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appPreventSubmit]',
  standalone: true
})
export class PreventSubmitDirective {
  @HostListener('submit', ['$event'])
  onSubmit(event: Event): void {
    event.preventDefault();
    console.log('submit prevented');
  }
}
```

## Best Practices
- Clearly document the reason for preventDefault in comments or documentation
- Verify that focus movement and accessibility are not affected
- Reliably provide alternative actions (custom submission processing, etc.)

## Considerations
- When using with links, also verify keyboard operation behavior
- Suppressing form submission requires manual validation and error handling
- Be careful not to block features that depend on browser default actions (print dialog, etc.)

## Related Technologies
- Event.stopPropagation
- Angular Forms
- Accessibility guidelines
