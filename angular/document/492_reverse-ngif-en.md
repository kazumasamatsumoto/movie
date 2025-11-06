# #492 "Reverse Operation of *ngIf"

## Overview
The Unless directive providing reverse operation of `*ngIf` displays view only when condition is false. Can express negation conditions understandably in template.

## Learning Objectives
- Understand logic implementing reverse operation of `*ngIf`
- Learn technique of monitoring condition changes with Input setter
- Grasp pattern of view generation and destruction

## Technical Points
- Clear if true, create if false with `set condition(value: boolean)`
- Booleanize value with `coerceBooleanProperty` etc.
- Use `hasView` flag to avoid regeneration

## 📺 On-Screen Code (for video)
```html
<div *appUnless="form.valid">Please fill in the form</div>
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
  set appUnless(condition: boolean) {
    if (!condition && !this.hasView) {
      this.viewContainer.createEmbeddedView(this.template);
      this.hasView = true;
    } else if (condition && this.hasView) {
      this.viewContainer.clear();
      this.hasView = false;
    }
  }
}
```

## Best Practices
- Maintain performance by preventing view duplication with `hasView`
- Improves readability as don't need to write negated conditions in template
- Align binding names in template with Input alias

## Considerations
- Avoid unnecessary changes as view operation runs each time condition changes
- Unify handling of `null` and `undefined` and document it
- Consider if supporting syntax like `*appUnless; else` yourself

## Related Technologies
- `*ngIf`
- TemplateRef / ViewContainerRef
- Structural Directive Input setter
