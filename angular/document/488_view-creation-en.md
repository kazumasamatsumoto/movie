# #488 "View Creation"

## Overview
View creation is a process of calling `createEmbeddedView` according to conditions to generate DOM tree from template, enabling reuse and state management by holding generated view.

## Learning Objectives
- Understand timing and logic of view creation
- Learn management methods for generated EmbeddedViewRef
- Grasp structure to switch views according to conditions

## Technical Points
- Organize existing views with `clear` before view creation
- Hold EmbeddedViewRef with property
- Also consider using `detach`/`attach` for reuse

## 📺 On-Screen Code (for video)
```typescript
if (!this.viewRef) this.viewRef = this.viewContainer.createEmbeddedView(this.template);
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appDefer]',
  standalone: true
})
export class DeferDirective implements OnChanges {
  @Input('appDefer') condition = false;
  private viewRef?: EmbeddedViewRef<unknown>;

  constructor(
    private readonly template: TemplateRef<unknown>,
    private readonly viewContainer: ViewContainerRef
  ) {}

  ngOnChanges(): void {
    if (this.condition) {
      if (!this.viewRef) {
        this.viewRef = this.viewContainer.createEmbeddedView(this.template);
      }
    } else {
      this.viewContainer.clear();
      this.viewRef = undefined;
    }
  }
}
```

## Best Practices
- Hold view creation state with flag or property to avoid duplicate creation
- Hold ViewRef for reuse, use `clear` and `create` appropriately as needed
- Utilize `ViewContainerRef` index when switching multiple templates

## Considerations
- Consider cache if condition changes frequently as creation/destruction cost is high
- Be careful of forgetting destruction when holding ViewRef to prevent memory leak
- Carefully manage state to prevent conflicts when creating asynchronously like Defer

## Related Technologies
- EmbeddedViewRef
- ViewContainerRef
- Structural Directive patterns
