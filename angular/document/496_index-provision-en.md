# #496 "Index Provision"

## Overview
To provide index in structural directive, set `index` property in context object and use as `let i = index` in template.

## Learning Objectives
- Understand index provision method through context
- Learn procedure using `let` syntax in template
- Grasp how to pass additional flags like `first`/`last`

## Technical Points
- Pass `{ $implicit: value, index: i }` as second argument of `createEmbeddedView`
- Set arbitrary keys like `context.index`
- Extract using `let` on template side

## 📺 On-Screen Code (for video)
```typescript
this.viewContainer.createEmbeddedView(this.template, { $implicit: item, index: i });
```

## 💻 Detailed Implementation Example (for learning)
```typescript
interface RepeatContext<T> {
  $implicit: T;
  index: number;
  even: boolean;
}

@Directive({
  selector: '[appRepeatOf]',
  standalone: true
})
export class RepeatOfDirective<T> implements OnChanges {
  @Input('appRepeatOf') items: T[] = [];

  constructor(
    private readonly template: TemplateRef<RepeatContext<T>>,
    private readonly viewContainer: ViewContainerRef
  ) {}

  ngOnChanges(): void {
    this.viewContainer.clear();
    this.items.forEach((item, i) => {
      this.viewContainer.createEmbeddedView(this.template, {
        $implicit: item,
        index: i,
        even: i % 2 === 0
      });
    });
  }
}
```

## Best Practices
- Define Context type for type-safe handling on template side
- Provide necessary metadata like `even`, `odd`, `first`, `last`
- Document to use explicitly like `let item; let i = index`

## Considerations
- `$implicit` is implicit main value, so avoid confusion with other properties
- Be mindful of duplicate generation with large data, consider differential updates
- Structural Directive can only be applied one per element

## Related Technologies
- Context object
- TemplateRef
- `*ngFor` context
