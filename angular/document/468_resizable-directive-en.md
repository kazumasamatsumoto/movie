# #468 "Resizable Directive - Resizing"

## Overview
The Resizable directive adds resize handles to elements, allowing width and height changes through drag operations. Minimum/maximum sizes and direction restrictions can be set via Input.

## Learning Objectives
- Understand the structure of resize directive
- Learn how to generate handles and change size with drag
- Grasp design of constraints (min/max) and direction options

## Technical Points
- Add handle element with Renderer2
- Update size with pointer events
- Update width/height with HostBinding or style manipulation

## 📺 On-Screen Code (for video)
```typescript
@HostBinding('style.width.px') width = 300;
@HostBinding('style.height.px') height = 200;
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appResizable]',
  standalone: true
})
export class ResizableDirective implements OnInit, OnDestroy {
  @Input() minWidth = 150;
  @Input() minHeight = 100;
  @Input() maxWidth = Infinity;
  @Input() maxHeight = Infinity;

  @HostBinding('style.position') position = 'relative';
  @HostBinding('style.width.px') width = 300;
  @HostBinding('style.height.px') height = 200;

  private handle!: HTMLElement;
  private startX = 0;
  private startY = 0;
  private startWidth = 0;
  private startHeight = 0;

  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2) {}

  ngOnInit(): void {
    this.handle = this.renderer.createElement('span');
    this.renderer.addClass(this.handle, 'resize-handle');
    this.renderer.setStyle(this.handle, 'position', 'absolute');
    this.renderer.setStyle(this.handle, 'right', '0');
    this.renderer.setStyle(this.handle, 'bottom', '0');
    this.renderer.setStyle(this.handle, 'width', '12px');
    this.renderer.setStyle(this.handle, 'height', '12px');
    this.renderer.setStyle(this.handle, 'cursor', 'nwse-resize');
    this.renderer.appendChild(this.el.nativeElement, this.handle);
    this.handle.addEventListener('pointerdown', this.onPointerDown);
  }

  private onPointerDown = (event: PointerEvent): void => {
    event.preventDefault();
    this.startX = event.clientX;
    this.startY = event.clientY;
    this.startWidth = this.width;
    this.startHeight = this.height;
    document.addEventListener('pointermove', this.onPointerMove);
    document.addEventListener('pointerup', this.onPointerUp);
  };

  private onPointerMove = (event: PointerEvent): void => {
    const deltaX = event.clientX - this.startX;
    const deltaY = event.clientY - this.startY;
    this.width = Math.min(this.maxWidth, Math.max(this.minWidth, this.startWidth + deltaX));
    this.height = Math.min(this.maxHeight, Math.max(this.minHeight, this.startHeight + deltaY));
  };

  private onPointerUp = (): void => {
    document.removeEventListener('pointermove', this.onPointerMove);
    document.removeEventListener('pointerup', this.onPointerUp);
  };

  ngOnDestroy(): void {
    this.handle.removeEventListener('pointerdown', this.onPointerDown);
    document.removeEventListener('pointermove', this.onPointerMove);
    document.removeEventListener('pointerup', this.onPointerUp);
  }
}
```

## Best Practices
- Generate handle with Renderer2 without polluting component template
- Set minimum/maximum sizes via Input to restrict unexpected sizes
- Set handle appearance and animation with CSS to improve UX

## Considerations
- Set `pointer-events` and `touch-action` so resize and scroll don't interfere
- Provide device-specific UI as resize operations are difficult on mobile
- Be mindful of layout changes from handle addition, set position to relative etc.

## Related Technologies
- Renderer2
- Pointer Events
- Drag & Resize libraries
