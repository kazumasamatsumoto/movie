# #410 "Keyboard Event Monitoring"

## Overview
Monitoring keyboard events enables shortcuts and accessibility improvements, and allows common handling of `keydown`/`keyup` processing for focused elements with Directive.

## Learning Objectives
- Understand the difference between `keydown`, `keyup`, and `keypress`
- Learn how to obtain key information with HostListener
- Learn accessibility improvement techniques involving keyboard operations

## Technical Points
- `@HostListener('keydown', ['$event'])`
- Check modifier keys with `event.key`, `event.code`, `event.ctrlKey`, etc.
- Suppress default action with `event.preventDefault()` for shortcut registration

## 📺 On-Screen Code (for video)
```typescript
@HostListener('keydown', ['$event.key'])
handleKey(key: string): void { if (key === 'Enter') this.trigger(); }
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appShortcut]',
  standalone: true
})
export class ShortcutDirective {
  @Output() shortcut = new EventEmitter<void>();

  @HostListener('keydown', ['$event'])
  onKeydown(event: KeyboardEvent): void {
    if (event.key === 'Enter' || (event.key === ' ' && event.target instanceof HTMLElement)) {
      event.preventDefault();
      this.shortcut.emit();
    }
  }
}
```

## Best Practices
- Choose key determination using `event.key` (locale-aware) or `event.code` (physical key) depending on the situation
- Handle both Space/Enter simultaneously for accessibility improvement
- Document the shortcut list and make it explicit to users

## Considerations
- Keyboard events only reach focused elements, so manage focus
- Consider OS differences when combining modifier key determination
- Be careful not to override browser reserved shortcuts

## Related Technologies
- EventEmitter
- Accessibility (ARIA role/button/checkbox)
- KeyboardEvent API
