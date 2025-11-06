# #427 "Publishing Custom Events"

## Overview
Directives can publish internal state and operation results as custom events, which the consumer side can receive with `(appSomething)` and incorporate into application logic.

## Learning Objectives
- Understand custom event design methods
- Clarify event name and payload naming conventions
- Learn to organize firing conditions and lifecycle

## Technical Points
- `@Output() appDragMoved = new EventEmitter<Point>();`
- Pass payload as object to ensure extensibility
- Document firing timing in event documentation

## 📺 On-Screen Code (for video)
```typescript
@Output() appDragMoved = new EventEmitter<{ x: number; y: number }>();
```

## 💻 Detailed Implementation Example (for learning)
```typescript
interface DragPosition {
  x: number;
  y: number;
}

@Directive({
  selector: '[appDragTracker]',
  standalone: true
})
export class DragTrackerDirective {
  @Output() appDragMoved = new EventEmitter<DragPosition>();

  @HostListener('document:mousemove', ['$event'])
  onMove(event: MouseEvent): void {
    if (event.buttons === 1) {
      this.appDragMoved.emit({ x: event.clientX, y: event.clientY });
    }
  }
}
```

## Best Practices
- Define event payloads in object format that's resistant to changes
- Use `appAction` format for event names to clarify meaning
- Document firing timing and guarantee with tests

## Considerations
- Don't forget to remove listeners when using document-level listeners
- Too many output events complicate consumer-side processing, keep to necessary minimum
- Be aware of event firing order and maintain consistency in dependent processing

## Related Technologies
- HostListener (for document/window)
- RxJS Subject
- Event naming guidelines
