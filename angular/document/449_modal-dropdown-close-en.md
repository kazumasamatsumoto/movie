# #449 "Modal/Dropdown Close Processing"

## Overview
Using the ClickOutside directive allows for concise implementation of close processing when clicking outside modals or dropdowns. The close logic is handled externally, while the directive focuses on detection.

## Learning Objectives
- Understand how to make modal/dropdown close processing respond to outside clicks
- Learn the flow of detecting events with directive and changing state in component
- Grasp combinations with focus and Escape key

## Technical Points
- Notify `close` or `outside` with Output event
- Control state in modal component
- Combine with focus control and Esc key support

## 📺 On-Screen Code (for video)
```html
<div class="dropdown" appClickOutside (appClickOutside)="close()">...</div>
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Component({
  selector: 'app-dropdown',
  standalone: true,
  imports: [CommonModule, ClickOutsideDirective],
  template: `
    <div class="dropdown" appClickOutside (appClickOutside)="close()">
      <ul>
        <li><button (click)="select('Profile')">Profile</button></li>
        <li><button (click)="select('Settings')">Settings</button></li>
      </ul>
    </div>
  `
})
export class DropdownComponent {
  protected close(): void {
    console.log('close dropdown');
  }

  protected select(value: string): void {
    console.log('selected', value);
    this.close();
  }
}
```

## Best Practices
- Control close processing on component side based on state, directive focuses only on detection
- Use in combination with other close triggers like Esc key or focus out
- Pass close conditions via Input to enable detailed control

## Considerations
- Use `stopPropagation` appropriately if events propagate inside modal and close it
- Events may not be captured in iFrames or Shadow DOM
- Consider z-index and event order when multiple modals overlap

## Related Technologies
- ClickOutsideDirective
- Keyboard shortcuts (Esc)
- FocusTrap
