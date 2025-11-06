# #408 "Click Event Monitoring"

## Overview
Monitoring click events with HostListener and performing processing or state updates in response to host element clicks is the most basic directive pattern.

## Learning Objectives
- Understand how to handle `click` events with HostListener
- Learn the procedure to obtain DOM information from `$event`
- Learn behavior control through combination with preventDefault

## Technical Points
- `@HostListener('click', ['$event'])`
- Stop default action with `$event.preventDefault()`
- Use `Event.target` to determine click source

## 📺 On-Screen Code (for video)
```typescript
@HostListener('click') handleClick(): void { this.toggle = !this.toggle; }
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appToggleOnClick]',
  standalone: true
})
export class ToggleOnClickDirective {
  @HostBinding('class.is-active') active = false;

  @HostListener('click', ['$event'])
  onClick(event: MouseEvent): void {
    event.preventDefault();
    this.active = !this.active;
  }
}
```

@Component({
  selector: 'app-click-demo',
  standalone: true,
  imports: [CommonModule, ToggleOnClickDirective],
  template: `
    <button type="button" appToggleOnClick>Click to toggle</button>
  `
})
export class ClickDemoComponent {}

## Best Practices
- Keep click side effects lightweight, delegate complex logic to services
- Use `preventDefault()` and `stopPropagation()` only when necessary
- Synchronize display state with HostBinding to improve template readability

## Considerations
- When applying clicks to elements other than buttons or links, handle accessibility
- Consider compatibility with touch events and test behavior on mobile
- Check if event duplication (double-clicks, etc.) is not a problem

## Related Technologies
- HostBinding
- EventEmitter
- Accessibility (role/button, etc.)
