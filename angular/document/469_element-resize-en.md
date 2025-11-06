# #469 "Element Resizing"

## Overview
In element resizing, calculate drag distance to update width/height and restrict to satisfy boundary conditions (min/max). Also need to consider `box-sizing` to prevent layout collapse.

## Learning Objectives
- Understand how to calculate size from drag distance
- Learn how to apply min/max constraints
- Grasp implementation considering influence of `box-sizing` and padding

## Technical Points
- Record width and pointer coordinates at drag start
- Add movement amount to set width/height within constraint range
- Simplify calculation by utilizing `box-sizing: border-box`

## 📺 On-Screen Code (for video)
```typescript
this.width = Math.min(this.maxWidth, Math.max(this.minWidth, this.startWidth + deltaX));
```

## 💻 Detailed Implementation Example (for learning)
```typescript
private updateSize(deltaX: number, deltaY: number): void {
  const newWidth = this.startWidth + deltaX;
  const newHeight = this.startHeight + deltaY;
  this.width = Math.min(this.maxWidth, Math.max(this.minWidth, newWidth));
  this.height = Math.min(this.maxHeight, Math.max(this.minHeight, newHeight));
}
```

## Best Practices
- Calculate including padding and border with `box-sizing: border-box`
- Fire size change event with Output if two-way binding is needed
- Provide visual feedback with transform or outline during change

## Considerations
- CSS Grid or Flexbox elements have resize constraints, so check layout
- Define behavior clearly when falling below minimum size (fix, snap, etc.)
- Set `user-select: none` to prevent text selection during resize

## Related Technologies
- ResizableDirective
- CSS box-sizing
- Drag event processing
