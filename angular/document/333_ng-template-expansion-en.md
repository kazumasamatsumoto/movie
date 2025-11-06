# #333 "Expansion to <ng-template>"

## Overview
Structural directives are expanded to `<ng-template>` at compile time, controlling DOM structure through a mechanism that lazily generates templates.

## Learning Objectives
- Understand the role and generation timing of `<ng-template>`
- Grasp the mechanism of EmbeddedViewRef
- Apply template expansion in custom directive implementation

## Technical Points
- `<ng-template>` is not directly output to the DOM during rendering
- ViewContainerRef instantiates templates with `createEmbeddedView`
- Pass values to templates through context objects

## 📺 On-Screen Code (for video)
```html
<ng-template #emptyState>
  <p>No data available.</p>
</ng-template>
```

## 💻 Detailed Implementation Example (for learning)
```typescript
interface EmptyContext {
  $implicit: number;
}

@Directive({
  selector: '[appEmptyState]',
  standalone: true
})
export class EmptyStateDirective implements OnChanges {
  @Input({ alias: 'appEmptyState', required: true }) count!: number;
  @Input() appEmptyStateTemplate?: TemplateRef<EmptyContext>;

  constructor(private readonly view: ViewContainerRef, private readonly defaultTpl: TemplateRef<EmptyContext>) {}

  ngOnChanges(): void {
    this.view.clear();
    if (this.count === 0) {
      const tpl = this.appEmptyStateTemplate ?? this.defaultTpl;
      this.view.createEmbeddedView(tpl, { $implicit: this.count });
    }
  }
}

@Component({
  selector: 'app-empty-demo',
  standalone: true,
  imports: [CommonModule, EmptyStateDirective],
  template: `
    <ul *appEmptyState="items.length; template: emptyTpl">
      <li *ngFor="let item of items">{{ item }}</li>
    </ul>
    <ng-template #emptyTpl let-count>
      <p>0 items ({{ count }})</p>
    </ng-template>
  `
})
export class EmptyDemoComponent {
  protected items: string[] = [];
}
```

## Best Practices
- Pass context values to templates using `let-` syntax to enhance reusability
- Provide an API that can switch between default and custom templates
- Avoid complex logic within templates and focus on presentation logic

## Considerations
- `<ng-template>` is not directly visible in the browser, so use Angular DevTools for debugging
- Leaving EmbeddedViews generated can lead to memory leaks
- Specify types when passing template references to leverage IDE completion

## Related Technologies
- EmbeddedViewRef
- TemplateRef
- Angular DevTools
