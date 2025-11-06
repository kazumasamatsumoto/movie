# #491 "Unless Directive - Inverted Condition"

## Overview
The Unless directive is a structural directive that displays template when condition is false, providing readable template syntax as inverted version of `*ngIf`.

## Learning Objectives
- Understand operation of Unless directive
- Learn how to implement condition inversion with `createEmbeddedView`/`clear`
- Set selector and Input alias to enable `*appUnless` syntax

## Technical Points
- `@Input('appUnless') set condition(value: boolean)`
- Generate view when `value === false`, `clear` when true
- Prevent double generation with `this.hasView` flag

## 📺 On-Screen Code (for video)
```html
<p *appUnless="isLoggedIn">Please log in</p>
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
  set condition(value: boolean) {
    if (!value && !this.hasView) {
      this.viewContainer.createEmbeddedView(this.template);
      this.hasView = true;
    } else if (value && this.hasView) {
      this.viewContainer.clear();
      this.hasView = false;
    }
  }
}
```

## Best Practices
- Hold flag to prevent unnecessary createEmbeddedView
- Recommend null-safe expressions like `*appUnless="items?.length"`
- Also consider coercing for values other than booleans to work correctly

## Considerations
- Clarify handling of `condition` when undefined
- Generation cost occurs if clearing every time without holding view
- Cannot use `appUnless` and `ngIf` on same element together

## Related Technologies
- TemplateRef/ViewContainerRef
- Structural Directive Input alias
- Comparison with `*ngIf`
