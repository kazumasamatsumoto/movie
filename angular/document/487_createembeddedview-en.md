# #487 "createEmbeddedView() Method"

## Overview
`createEmbeddedView()` is a method that generates view from TemplateRef and inserts it into ViewContainerRef, allowing value supply to template by passing context.

## Learning Objectives
- Understand createEmbeddedView arguments and return value
- Learn how to pass context object
- Grasp cases of holding and reusing generated view

## Technical Points
- `createEmbeddedView(template, context?, index?)`
- Return value is `EmbeddedViewRef`
- Provide `$implicit` and other properties with context

## 📺 On-Screen Code (for video)
```typescript
const view = this.viewContainer.createEmbeddedView(this.template, { $implicit: item });
```

## 💻 Detailed Implementation Example (for learning)
```typescript
interface RepeatContext<T> {
  $implicit: T;
  index: number;
}

@Directive({
  selector: '[appRepeat]',
  standalone: true
})
export class RepeatDirective<T> implements OnChanges {
  @Input('appRepeat') count = 0;
  @Input('appRepeatOf') value!: T;

  constructor(private readonly template: TemplateRef<RepeatContext<T>>, private readonly viewContainer: ViewContainerRef) {}

  ngOnChanges(): void {
    this.viewContainer.clear();
    for (let i = 0; i < this.count; i++) {
      this.viewContainer.createEmbeddedView(this.template, {
        $implicit: this.value,
        index: i
      });
    }
  }
}
```

## Best Practices
- Explicitly define context to ensure template-side type safety
- Hold generated `EmbeddedViewRef` in array as needed
- Can finely control insertion position using index argument

## Considerations
- Avoid unnecessary clear when generating multiple views from same template
- Memory leak if not destroying with `remove`/`clear` when view becomes unnecessary after generation
- Match context property names with template `let` declarations

## Related Technologies
- TemplateRef
- ViewContainerRef
- EmbeddedViewRef
