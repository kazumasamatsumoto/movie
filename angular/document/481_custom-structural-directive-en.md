# #481 "Creating Custom Structural Directive"

## Overview
Custom Structural Directive is a mechanism that controls template creation and destruction, allowing dynamic construction of DOM tree using `TemplateRef` and `ViewContainerRef`.

## Learning Objectives
- Understand basic structure of Structural Directive
- Learn roles of TemplateRef and ViewContainerRef
- Grasp selector design to enable * syntax

## Technical Points
- `@Directive({ selector: '[appUnless]', standalone: true })`
- `constructor(private template: TemplateRef<unknown>, private view: ViewContainerRef)`
- Generate/destroy views with `createEmbeddedView`/`clear`

## 📺 On-Screen Code (for video)
```typescript
constructor(private tpl: TemplateRef<unknown>, private vc: ViewContainerRef) {}
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appUnless]',
  standalone: true
})
export class UnlessDirective implements OnChanges {
  @Input('appUnless') condition = false;
  private hasView = false;

  constructor(
    private readonly template: TemplateRef<unknown>,
    private readonly viewContainer: ViewContainerRef
  ) {}

  ngOnChanges(): void {
    if (!this.condition && !this.hasView) {
      this.viewContainer.createEmbeddedView(this.template);
      this.hasView = true;
    } else if (this.condition && this.hasView) {
      this.viewContainer.clear();
      this.hasView = false;
    }
  }
}
```

## Best Practices
- Hold view generation status with flag to avoid unnecessary regeneration
- Provide syntax like `*appUnless` with Input alias
- Pass to second argument of `createEmbeddedView` if context is needed

## Considerations
- Be aware during design that multiple Structural Directives cannot be applied to same element
- TemplateRef/ViewContainerRef can only be injected via constructor
- Make conditional branching clear to avoid view destruction leaks

## Related Technologies
- TemplateRef
- ViewContainerRef
- Structural Directive template syntax
