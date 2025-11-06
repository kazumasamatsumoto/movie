# #464 "Drag Event Handling"

## Overview
In drag event handling, monitor pointer events, calculate movement amount and reflect to host element, while notifying drag information externally with EventEmitter.

## Learning Objectives
- Understand drag processing flow using pointer events
- Learn movement amount calculation and State updates
- Grasp how to notify drag state externally with EventEmitter

## Technical Points
- Record initial position with pointerdown
- Calculate movement amount and update transform with pointermove
- End drag and cleanup with pointerup

## 📺 On-Screen Code (for video)
```typescript
@Output() dragMove = new EventEmitter<{ x: number; y: number }>();
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appDragHandle]',
  standalone: true
})
export class DragHandleDirective implements OnDestroy {
  @Output() dragMove = new EventEmitter<{ x: number; y: number }>();
  @Output() dragEnd = new EventEmitter<void>();

  private startX = 0;
  private startY = 0;
  private boundMove = this.onPointerMove.bind(this);
  private boundUp = this.onPointerUp.bind(this);

  @HostListener('pointerdown', ['$event'])
  onPointerDown(event: PointerEvent): void {
    event.preventDefault();
    this.startX = event.clientX;
    this.startY = event.clientY;
    document.addEventListener('pointermove', this.boundMove);
    document.addEventListener('pointerup', this.boundUp);
  }

  private onPointerMove(event: PointerEvent): void {
    const deltaX = event.clientX - this.startX;
    const deltaY = event.clientY - this.startY;
    this.dragMove.emit({ x: deltaX, y: deltaY });
  }

  private onPointerUp(): void {
    document.removeEventListener('pointermove', this.boundMove);
    document.removeEventListener('pointerup', this.boundUp);
    this.dragEnd.emit();
  }

  ngOnDestroy(): void {
    document.removeEventListener('pointermove', this.boundMove);
    document.removeEventListener('pointerup', this.boundUp);
  }
}
```

## Best Practices
- Notify movement amount externally with EventEmitter, control position application on user side
- Hold listeners in bound functions for reliable removal later
- Provide events to execute post-processing (snap, save) on drag end

## Considerations
- Pointer events are not supported in all browsers, so check support status
- Prevent text selection with `preventDefault` during drag
- Be mindful of side effects like context menu from long press

## Related Technologies
- EventEmitter
- Pointer Events API
- Drag & Drop implementation patterns
