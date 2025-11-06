# #447 "ClickOutside Directive - Outside Click Detection"

## Overview
The ClickOutside directive detects clicks or touches that occur outside the host element and can centralize logic for closing modals and dropdowns.

## Learning Objectives
- Understand the basic pattern for outside click detection
- Learn how to monitor document events with HostListener
- Grasp the design of notifying externally with EventEmitter

## Technical Points
- `@HostListener('document:click', ['$event'])`
- Determine if `event.target` is within the host element
- Notify close event with Output

## 📺 On-Screen Code (for video)
```typescript
@HostListener('document:click', ['$event']) handleClick(event: MouseEvent) { if (!this.el.nativeElement.contains(event.target)) this.clickedOutside.emit(); }
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appClickOutside]',
  standalone: true
})
export class ClickOutsideDirective {
  @Output() appClickOutside = new EventEmitter<void>();

  constructor(private readonly el: ElementRef<HTMLElement>) {}

  @HostListener('document:click', ['$event'])
  onDocumentClick(event: MouseEvent): void {
    if (!this.el.nativeElement.contains(event.target as Node)) {
      this.appClickOutside.emit();
    }
  }

  @HostListener('document:touchstart', ['$event'])
  onDocumentTouch(event: TouchEvent): void {
    if (!this.el.nativeElement.contains(event.target as Node)) {
      this.appClickOutside.emit();
    }
  }
}
```

## Best Practices
- When using document events, exclude internal clicks with `contains`
- Support both touch events and click events
- Delegate close processing externally with Output to increase reusability

## Considerations
- Guard is necessary because document does not exist in SSR
- Be mindful of event order when multiple directives exist on the same page
- Set `stopPropagation` appropriately if clicks are needed within modal

## Related Technologies
- HostListener
- EventEmitter
- Overlay/Modal components
