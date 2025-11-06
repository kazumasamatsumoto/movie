# #486 "View Container Operations"

## Overview
Using ViewContainerRef enables operations like generating, inserting, deleting, and clearing EmbeddedView, allowing flexible control of template display in structural directive.

## Learning Objectives
- Understand main methods of ViewContainerRef
- Learn view insertion position and deletion procedures
- Grasp how to hold and reuse EmbeddedViewRef

## Technical Points
- `createEmbeddedView(template, context?, index?)`
- `insert(viewRef, index)`/`move`/`remove(index)`
- Destroy all views with `clear()`

## 📺 On-Screen Code (for video)
```typescript
const view = this.viewContainer.createEmbeddedView(this.template);
this.viewContainer.insert(view, 0);
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appViewOperations]',
  standalone: true
})
export class ViewOperationsDirective {
  private viewRefs: EmbeddedViewRef<unknown>[] = [];

  constructor(
    private readonly template: TemplateRef<unknown>,
    private readonly viewContainer: ViewContainerRef
  ) {}

  addView(): void {
    const viewRef = this.viewContainer.createEmbeddedView(this.template);
    this.viewRefs.push(viewRef);
  }

  removeLast(): void {
    if (this.viewRefs.length === 0) return;
    const viewRef = this.viewRefs.pop()!;
    const index = this.viewContainer.indexOf(viewRef);
    if (index !== -1) {
      this.viewContainer.remove(index);
    }
  }

  clearAll(): void {
    this.viewContainer.clear();
    this.viewRefs = [];
  }
}
```

## Best Practices
- Managing generated EmbeddedViewRef in array makes insertion/deletion easy
- Utilize `insert` index or `move` when maintaining order
- Convenient for state reset as `clear()` can destroy all at once

## Considerations
- Need to recalculate index during remove if not holding ViewRef
- Affects performance if generating views indiscriminately, so generate only needed number
- Continuing to hold reference after view destruction leads to memory leak

## Related Technologies
- EmbeddedViewRef
- TemplateRef
- Structural Directive control
