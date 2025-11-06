# #409 "Mouse Event Monitoring"

## Overview
Mouse events are important for realizing interactions like hover and drag, and can control UI by monitoring `mouseenter`, `mouseleave`, `mousemove`, etc. with HostListener.

## Learning Objectives
- Understand representative mouse events
- Learn how to coordinate multiple events with HostListener
- Learn the procedure to change styles by combining with Renderer2 and HostBinding

## Technical Points
- Manage hover state with `mouseenter`/`mouseleave`
- Get coordinates with `mousemove`, detect drag state with `DragEvent`
- Type event objects as `MouseEvent`/`DragEvent`

## 📺 On-Screen Code (for video)
```typescript
@HostListener('mouseenter') onEnter(): void { this.hover = true; }
@HostListener('mouseleave') onLeave(): void { this.hover = false; }
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appHoverGlow]',
  standalone: true
})
export class HoverGlowDirective {
  @HostBinding('class.is-hover') hover = false;

  @HostListener('mouseenter')
  onEnter(): void {
    this.hover = true;
  }

  @HostListener('mouseleave')
  onLeave(): void {
    this.hover = false;
  }

  @HostListener('mousemove', ['$event.clientX', '$event.clientY'])
  onMove(x: number, y: number): void {
    console.log('mouse position', x, y);
  }
}
```

## Best Practices
- Keep state management simple with booleans, etc., and make style changes with HostBinding
- Consider throttling for `mousemove` as it fires frequently
- Integrate with HTML5 Drag & Drop API or external libraries if drag operations are needed

## Considerations
- Prepare fallbacks as mouse events don't fire on mobile
- Measure performance impact of event monitoring with Chrome DevTools
- Avoid async processing in `mousemove`, use `requestAnimationFrame` if necessary

## Related Technologies
- Renderer2
- DragEvent API
- RxJS throttleTime
