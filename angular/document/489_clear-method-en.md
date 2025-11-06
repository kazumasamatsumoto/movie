# #489 "clear() Method"

## Overview
`ViewContainerRef.clear()` destroys all EmbeddedViews within container, enabling collective deletion of unnecessary views when structural directive conditions change.

## Learning Objectives
- Understand usage and behavior of clear method
- Learn state management methods after clearing
- Grasp view reset procedure combined with createEmbeddedView

## Technical Points
- `viewContainer.clear()`
- Check if empty with `viewContainer.length === 0`
- Also destroy reference if holding ViewRef

## 📺 On-Screen Code (for video)
```typescript
this.viewContainer.clear();
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appResettable]',
  standalone: true
})
export class ResettableDirective {
  constructor(private readonly viewContainer: ViewContainerRef) {}

  reset(): void {
    this.viewContainer.clear();
  }
}
```

## Best Practices
- Delete existing views with clear before conditions change and generate new state
- Initialize references and flags after clear to maintain consistency
- ViewRef is destroyed when calling `clear`, so consider detach if reuse is needed

## Considerations
- All views are deleted with clear, so use `remove(index)` for partial deletion
- Grasp cost of clear when many views are generated
- Avoid accessing held references after clear

## Related Technologies
- ViewContainerRef.remove
- EmbeddedViewRef
- Structural Directive control
