# #446 "Dynamic Positioning"

## Overview
To dynamically adjust Tooltip position, obtain the BoundingClientRect of the host element and calculate the position considering the placement option and viewport boundaries.

## Learning Objectives
- Understand the basics of Tooltip position calculation
- Learn coordinate calculation according to placement options
- Grasp techniques to correct position to stay within viewport

## Technical Points
- Get coordinates with `getBoundingClientRect()`
- Get Tooltip size with `clientWidth/Height`
- Invert or adjust offset when exceeding viewport

## 📺 On-Screen Code (for video)
```typescript
const host = this.el.nativeElement.getBoundingClientRect();
const tooltip = this.tooltip!.getBoundingClientRect();
```

## 💻 Detailed Implementation Example (for learning)
```typescript
private setPosition(placement: 'top' | 'bottom' | 'left' | 'right', offset: number): void {
  if (!this.tooltip) return;
  const host = this.el.nativeElement.getBoundingClientRect();
  const tip = this.tooltip.getBoundingClientRect();
  const viewportWidth = window.innerWidth;
  const viewportHeight = window.innerHeight;
  let top = 0;
  let left = 0;
  switch (placement) {
    case 'bottom':
      top = host.bottom + offset;
      left = host.left + host.width / 2 - tip.width / 2;
      break;
    case 'left':
      top = host.top + host.height / 2 - tip.height / 2;
      left = host.left - tip.width - offset;
      break;
    case 'right':
      top = host.top + host.height / 2 - tip.height / 2;
      left = host.right + offset;
      break;
    default:
      top = host.top - tip.height - offset;
      left = host.left + host.width / 2 - tip.width / 2;
  }
  top = Math.max(0, Math.min(top, viewportHeight - tip.height));
  left = Math.max(0, Math.min(left, viewportWidth - tip.width));
  this.renderer.setStyle(this.tooltip, 'top', `${top}px`);
  this.renderer.setStyle(this.tooltip, 'left', `${left}px`);
}
```

## Best Practices
- Accept placement option and offset via Input for flexibility
- Invert/correct at viewport boundaries to prevent display from being cut off
- Consider recalculation on scroll and responsive support

## Considerations
- Use `position: fixed` as position shifts with page scrolling
- For elements within scroll containers, use `position: absolute` + calculate based on parent element
- High-frequency recalculation affects performance, so optimize

## Related Technologies
- IntersectionObserver
- ResizeObserver
- Tooltip library placement logic
