# #462 "Drag Directive - Dragging"

## Overview
The Drag directive makes elements draggable, allowing position changes through mouse or touch operations. Using pointer events supports both PC and mobile.

## Learning Objectives
- Understand the basic flow of drag operations
- Learn implementation using pointerdown/move/up events
- Grasp the mechanism for notifying drag state externally

## Technical Points
- Start drag with `pointerdown`, update position with `pointermove`, end with `pointerup`
- Update transform with HostBinding
- Notify drag position with Output

## 📺 On-Screen Code (for video)
```typescript
@HostListener('pointerdown', ['$event']) startDrag(event: PointerEvent) { ... }
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appDrag]',
  standalone: true
})
export class DragDirective implements OnDestroy {
  @HostBinding('style.userSelect') userSelect = 'none';
  @HostBinding('style.touchAction') touchAction = 'none';
  @HostBinding('style.transform') transform = 'translate(0px, 0px)';
  @Output() dragged = new EventEmitter<{ x: number; y: number }>();

  private dragging = false;
  private startX = 0;
  private startY = 0;
  private currentX = 0;
  private currentY = 0;

  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2) {}

  @HostListener('pointerdown', ['$event'])
  onPointerDown(event: PointerEvent): void {
    event.preventDefault();
    this.dragging = true;
    this.startX = event.clientX - this.currentX;
    this.startY = event.clientY - this.currentY;
    this.renderer.listen('document', 'pointermove', this.onPointerMove);
    this.renderer.listen('document', 'pointerup', this.onPointerUp);
  }

  private onPointerMove = (event: PointerEvent): void => {
    if (!this.dragging) return;
    this.currentX = event.clientX - this.startX;
    this.currentY = event.clientY - this.startY;
    this.transform = `translate(${this.currentX}px, ${this.currentY}px)`;
    this.dragged.emit({ x: this.currentX, y: this.currentY });
  };

  private onPointerUp = (): void => {
    this.dragging = false;
  };

  ngOnDestroy(): void {
    this.dragging = false;
  }
}
```

## Best Practices
- Unify mouse/touch support using Pointer Events
- Use transform to prevent layout destruction
- Suppress text selection with `user-select: none` during drag

## Considerations
- Reliably remove drag state listeners to prevent leaks
- Set `touchAction` so scroll and drag don't conflict
- Implement boundary checks if drag area restriction is needed

## Related Technologies
- Pointer Events API
- Drag & Drop libraries
- Renderer2
