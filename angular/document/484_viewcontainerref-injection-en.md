# #484 "ViewContainerRef Injection"

## Overview
ViewContainerRef is a container for inserting and removing views generated from templates, serving as the core for Structural Directive to control DOM structure.

## Learning Objectives
- Understand role of ViewContainerRef
- Learn operations like createEmbeddedView/clear/insert/remove
- Grasp how to use in Structural Directive lifecycle

## Technical Points
- `constructor(private vc: ViewContainerRef)`
- `vc.createEmbeddedView(template, context?)`
- Destroy view with `vc.clear()`

## 📺 On-Screen Code (for video)
```typescript
constructor(private viewContainer: ViewContainerRef) {}
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appViewContainerSample]',
  standalone: true
})
export class ViewContainerSampleDirective {
  constructor(
    private readonly template: TemplateRef<{ $implicit: string }>,
    private readonly viewContainer: ViewContainerRef
  ) {}

  render(message: string): void {
    this.viewContainer.clear();
    this.viewContainer.createEmbeddedView(this.template, { $implicit: message });
  }
}
```

## Best Practices
- Delegate view generation/destruction to ViewContainerRef, manage state with flags
- Manage index with `insert`, `remove` when handling multiple views
- Can hold generated `EmbeddedViewRef` for reuse

## Considerations
- Forgetting clear leaves view and leads to memory leak
- ViewContainerRef operations are performed synchronously, so be mindful of asynchronous processing timing
- Heavy use outside Structural Directive degrades template readability

## Related Technologies
- TemplateRef
- EmbeddedViewRef
- Structural Directive lifecycle
