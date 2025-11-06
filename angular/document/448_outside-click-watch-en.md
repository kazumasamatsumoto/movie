# #448 "Outside Click Monitoring"

## Overview
To monitor outside clicks and suppress operations, monitor `document` level events and determine if the click target is within the host element.

## Learning Objectives
- Understand outside click determination using the `contains` method
- Learn expansion methods for focus and touch events
- Grasp implementation conscious of behavior across devices

## Technical Points
- `this.el.nativeElement.contains(event.target)`
- Monitor both document click and document touch
- Notify results with Output event

## 📺 On-Screen Code (for video)
```typescript
if (!this.el.nativeElement.contains(event.target as Node)) this.clickedOutside.emit();
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appOutsideWatcher]',
  standalone: true
})
export class OutsideWatcherDirective {
  @Output() outside = new EventEmitter<Event>();

  constructor(private readonly el: ElementRef<HTMLElement>) {}

  @HostListener('document:click', ['$event'])
  onDocumentClick(event: MouseEvent): void {
    if (!this.el.nativeElement.contains(event.target as Node)) {
      this.outside.emit(event);
    }
  }

  @HostListener('document:focusin', ['$event'])
  onDocumentFocus(event: FocusEvent): void {
    if (!this.el.nativeElement.contains(event.target as Node)) {
      this.outside.emit(event);
    }
  }
}
```

## Best Practices
- Properly perform `contains` check so clicking inside dropdown doesn't close it
- Support focus movement as well to cover scenarios where closing occurs with keyboard operations
- Pass event information externally with EventEmitter, letting the user side decide processing

## Considerations
- Forgetting to remove document events can cause memory leaks (Angular auto-removes, but be aware)
- For elements within Shadow DOM, need to check `composedPath`
- Manage state to avoid conflicts when closing asynchronously

## Related Technologies
- EventEmitter
- Overlay/Modal design
- Shadow DOM
