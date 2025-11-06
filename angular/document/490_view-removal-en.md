# #490 "View Removal"

## Overview
`ViewContainerRef.remove` deletes EmbeddedView at specified index, enabling partial view deletion in structural directive managing multiple views.

## Learning Objectives
- Understand usage of remove method
- Grasp importance of index management
- Learn flow of holding and deleting EmbeddedViewRef

## Technical Points
- Delete view with `viewContainer.remove(index)`
- Get view count with `viewContainer.length`
- Get index with `indexOf(viewRef)`

## 📺 On-Screen Code (for video)
```typescript
const idx = this.viewContainer.indexOf(viewRef);
if (idx !== -1) this.viewContainer.remove(idx);
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appDynamicList]',
  standalone: true
})
export class DynamicListDirective {
  private viewRefs: EmbeddedViewRef<unknown>[] = [];

  constructor(
    private readonly template: TemplateRef<unknown>,
    private readonly viewContainer: ViewContainerRef
  ) {}

  add(): void {
    const view = this.viewContainer.createEmbeddedView(this.template);
    this.viewRefs.push(view);
  }

  remove(index: number): void {
    const view = this.viewRefs[index];
    if (!view) return;
    const containerIndex = this.viewContainer.indexOf(view);
    if (containerIndex !== -1) {
      this.viewContainer.remove(containerIndex);
    }
    this.viewRefs.splice(index, 1);
  }
}
```

## Best Practices
- Hold array of EmbeddedViewRef to simplify index calculation during remove
- Save in data structure if view state (context) is needed
- Be mindful that remaining view indexes change after deletion

## Considerations
- Cannot reuse ViewRef after remove, so regenerate if needed
- Calling remove when viewContainer is empty causes exception, so implement defensively
- Consider `detach`/`insert` for complex operations to reduce load

## Related Technologies
- ViewContainerRef.detach
- EmbeddedViewRef
- Structural Directive operations
