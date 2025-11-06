# #463 "Draggable Element Implementation"

## Overview
Draggable elements update position with transform during dragging and maintain start/end positions to achieve smooth movement. Initial position and limits can be set via Input.

## Learning Objectives
- Understand techniques for position updating using transform
- Learn how to accept initial position and limits via Input
- Grasp techniques for displaying drag state with animation

## Technical Points
- Update position with `translate(x, y)`
- Restrict movement range with `@Input() bounds`
- Change shadow and cursor during drag with CSS

## 📺 On-Screen Code (for video)
```typescript
@HostBinding('style.transform') transform = `translate(${this.x}px, ${this.y}px)`;
```

## 💻 Detailed Implementation Example (for learning)
```typescript
interface Bounds {
  minX: number;
  maxX: number;
  minY: number;
  maxY: number;
}

@Directive({
  selector: '[appDraggable]',
  standalone: true
})
export class DraggableDirective {
  @Input() bounds?: Bounds;
  @HostBinding('class.is-dragging') dragging = false;
  @HostBinding('style.transform') transform = 'translate(0px, 0px)';

  private startX = 0;
  private startY = 0;
  private positionX = 0;
  private positionY = 0;

  @HostListener('pointerdown', ['$event'])
  onPointerDown(event: PointerEvent): void {
    event.preventDefault();
    this.dragging = true;
    this.startX = event.clientX - this.positionX;
    this.startY = event.clientY - this.positionY;
    document.addEventListener('pointermove', this.onPointerMove);
    document.addEventListener('pointerup', this.onPointerUp);
  }

  private onPointerMove = (event: PointerEvent): void => {
    if (!this.dragging) return;
    let x = event.clientX - this.startX;
    let y = event.clientY - this.startY;
    if (this.bounds) {
      x = Math.max(this.bounds.minX, Math.min(x, this.bounds.maxX));
      y = Math.max(this.bounds.minY, Math.min(y, this.bounds.maxY));
    }
    this.positionX = x;
    this.positionY = y;
    this.transform = `translate(${this.positionX}px, ${this.positionY}px)`;
  };

  private onPointerUp = (): void => {
    this.dragging = false;
    document.removeEventListener('pointermove', this.onPointerMove);
    document.removeEventListener('pointerup', this.onPointerUp);
  };
}
```

## Best Practices
- Control movement range via Input to make user operations predictable
- Use transform to balance performance and layout maintenance
- Set `cursor: grab`/`grabbing` in CSS to enhance operability

## Considerations
- Be mindful of `pointer-events` and `user-select` during drag to prevent unintended behavior
- Set `touch-action` appropriately on mobile devices as it conflicts with scrolling
- Always remove listeners on drag end to prevent leaks

## Related Technologies
- DragDirective
- CSS transform
- Pointer Events
