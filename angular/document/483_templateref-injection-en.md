# #483 "TemplateRef Injection"

## Overview
TemplateRef is a reference representing the template itself to which the directive is applied, serving as the template source when generating views in structural directive.

## Learning Objectives
- Understand functionality provided by TemplateRef
- Learn injection method in constructor
- Grasp relationship with view generation having context

## Technical Points
- `constructor(private template: TemplateRef<unknown>)`
- Call `createEmbeddedView` from `ViewContainerRef`, not from `template.createEmbeddedView`
- Can specify context type with generics

## 📺 On-Screen Code (for video)
```typescript
constructor(private template: TemplateRef<unknown>) {}
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appTemplateRefSample]',
  standalone: true
})
export class TemplateRefSampleDirective {
  constructor(private readonly template: TemplateRef<{ $implicit: number }>) {}

  createView(viewContainer: ViewContainerRef, index: number): void {
    viewContainer.createEmbeddedView(this.template, { $implicit: index });
  }
}
```

## Best Practices
- Define type with generics when using context to enable template-side completion
- TemplateRef can be reused many times during view generation
- Also consider receiving TemplateRef in wrapper service to share processing

## Considerations
- TemplateRef can only be injected within structural directive
- Not recommended to call createEmbeddedView directly in component template
- Match context Keys with template `let` declarations

## Related Technologies
- ViewContainerRef
- Context object
- Structural Directive basics
