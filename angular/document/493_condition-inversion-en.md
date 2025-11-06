# #493 "Condition Inversion Implementation"

## Overview
In condition inversion implementation, negate truthy value received via Input and generate template only when false. Handling special values like null/undefined is important.

## Learning Objectives
- Understand condition inversion implementation techniques
- Learn handling of truthy/falsy
- Grasp pattern of processing Input with setter

## Technical Points
- Booleanize then invert (like `!coerceBooleanProperty(value)`)
- Treat `null` and `undefined` as false
- `SimpleChanges` for change detection also an option

## 📺 On-Screen Code (for video)
```typescript
set appUnless(value: unknown) { const condition = coerceBooleanProperty(value); ... }
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appUnless]',
  standalone: true
})
export class UnlessDirective {
  private hasView = false;

  constructor(
    private readonly template: TemplateRef<unknown>,
    private readonly viewContainer: ViewContainerRef
  ) {}

  @Input('appUnless')
  set condition(value: unknown) {
    const shouldHide = coerceBooleanProperty(value);
    if (!shouldHide && !this.hasView) {
      this.viewContainer.createEmbeddedView(this.template);
      this.hasView = true;
    } else if (shouldHide && this.hasView) {
      this.viewContainer.clear();
      this.hasView = false;
    }
  }
}
```

## Best Practices
- Unify boolean judgment using `coerceBooleanProperty` from `@angular/cdk/coercion`
- Store inversion result in clear variable for readability
- Perform view operation only when condition changes

## Considerations
- Document to handle strings and numbers as expected for truthy/falsy
- Design according to requirements whether to treat `null` as false or error
- Limit Input type to boolean if possible to maintain type safety

## Related Technologies
- coerceBooleanProperty
- TemplateRef/ViewContainerRef
- Structural Directive Input handling
