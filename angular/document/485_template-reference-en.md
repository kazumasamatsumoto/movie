# #485 "Template Reference"

## Overview
Structural directive obtains template reference through TemplateRef and calls `createEmbeddedView` at necessary timing to generate view.

## Learning Objectives
- Understand relationship between TemplateRef and ng-template
- Learn view generation procedure utilizing template reference
- Grasp structure when handling multiple templates

## Technical Points
- TemplateRef represents template implicitly converted to ng-template
- Can access DOM element with `templateRef.elementRef`
- Generate view with `ViewContainerRef.createEmbeddedView(template, context)`

## 📺 On-Screen Code (for video)
```typescript
this.viewContainer.createEmbeddedView(this.template, context);
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appTemplateReference]',
  standalone: true
})
export class TemplateReferenceDirective {
  constructor(
    private readonly template: TemplateRef<{ $implicit: number }>,
    private readonly viewContainer: ViewContainerRef
  ) {}

  renderTimes(times: number): void {
    this.viewContainer.clear();
    for (let i = 0; i < times; i++) {
      this.viewContainer.createEmbeddedView(this.template, { $implicit: i });
    }
  }
}
```

## Best Practices
- Collectively manage data passed to template with Context object
- Clearing ViewContainerRef before regeneration prevents view duplication
- TemplateRef can be cached and reused to suppress extra DOM generation

## Considerations
- Avoid directly manipulating template to change DOM, manage via ViewContainerRef
- Consider performance impact when generating many views
- Be mindful during design that multiple Structural Directives cannot be applied simultaneously

## Related Technologies
- TemplateRef
- ViewContainerRef
- Context object
