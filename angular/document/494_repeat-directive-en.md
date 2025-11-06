# #494 "Repeat Directive - Repetition"

## Overview
The Repeat directive generates template specified number of times, providing simple loop. Can be used like `*appRepeat="5; let i = index"`.

## Learning Objectives
- Understand structure repeating template specified number of times
- Learn how to provide index etc. with context
- Grasp view generation pattern utilizing ViewContainerRef

## Technical Points
- Receive count via Input and createEmbeddedView in `for` loop
- Set `$implicit` and `index` in Context
- Make clean state with `clear()` before generation

## 📺 On-Screen Code (for video)
```html
<li *appRepeat="5; let i = index">Item {{ i }}</li>
```

## 💻 Detailed Implementation Example (for learning)
```typescript
interface RepeatContext {
  $implicit: number;
  index: number;
}

@Directive({
  selector: '[appRepeat]',
  standalone: true
})
export class RepeatDirective implements OnChanges {
  @Input('appRepeat') count = 0;

  constructor(
    private readonly template: TemplateRef<RepeatContext>,
    private readonly viewContainer: ViewContainerRef
  ) {}

  ngOnChanges(): void {
    this.viewContainer.clear();
    for (let i = 0; i < this.count; i++) {
      this.viewContainer.createEmbeddedView(this.template, {
        $implicit: i,
        index: i
      });
    }
  }
}
```

## Best Practices
- Defensively handle cases like negative count treated as 0
- Add necessary information (index, first, last etc.) to Context to improve usability
- Focus on numeric repetition rather than data array to clarify role

## Considerations
- Be mindful of performance with large numeric repetitions
- Design so diff doesn't become large as re-renders when `count` changes
- Set initial values to work not only on client but also SSR

## Related Technologies
- TemplateRef
- ViewContainerRef
- Context object
