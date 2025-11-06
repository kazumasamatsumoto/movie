# #495 "Fixed Count Repeat Display"

## Overview
Fixed count repeat display generates views for the number received via Input value, enabling concise description of simple iterative processing in template.

## Learning Objectives
- Understand view generation logic according to count value
- Learn validation and cleansing methods for input values
- Grasp processing flow during re-rendering

## Technical Points
- Normalize with `Math.max(0, Math.floor(count))`
- Loop createEmbeddedView after clearing ViewContainerRef
- Provide index and other information in Context

## 📺 On-Screen Code (for video)
```typescript
const times = Math.max(0, Math.floor(this.count));
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appRepeat]',
  standalone: true
})
export class RepeatDirective implements OnChanges {
  @Input('appRepeat') count = 0;

  constructor(
    private readonly template: TemplateRef<{ $implicit: number; index: number }>,
    private readonly viewContainer: ViewContainerRef
  ) {}

  ngOnChanges(): void {
    this.viewContainer.clear();
    const times = Math.max(0, Math.floor(this.count));
    for (let i = 0; i < times; i++) {
      this.viewContainer.createEmbeddedView(this.template, { $implicit: i, index: i });
    }
  }
}
```

## Best Practices
- Implement fallback when count is negative or non-numeric
- Convenient to also provide flags like `first`/`last`/`even` in Context
- Optimize as needed as many views update when count changes

## Considerations
- Be mindful of balance with server-side rendering as DOM becomes enormous when count is large
- Also consider optimization by manually remove/insert when change difference becomes large
- Understand rule that other Structural Directives cannot be attached to same element

## Related Technologies
- ViewContainerRef
- Context object
- Structural Directive basics
