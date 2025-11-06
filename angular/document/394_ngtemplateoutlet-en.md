# #394 "ngTemplateOutlet - Template Insertion"

## Overview
`ngTemplateOutlet` is a directive that injects template references from outside and renders them with a specified context, useful for layout customization.

## Learning Objectives
- Understand how to use `ngTemplateOutlet` and pass context
- Learn component design that performs template replacement
- Grasp the structure of `ngTemplateOutletContext`

## Technical Points
- Specify template reference with `[ngTemplateOutlet]="tpl"`
- Pass values with `[ngTemplateOutletContext]="{ $implicit: value }"`
- Can pass with arbitrary keys besides `$implicit`

## 📺 Display Code (for video)
```html
<ng-container [ngTemplateOutlet]="itemTpl" [ngTemplateOutletContext]="{ $implicit: item }"></ng-container>
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Component({
  selector: 'app-template-outlet-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <ng-container *ngFor="let task of tasks" [ngTemplateOutlet]="taskTpl" [ngTemplateOutletContext]="{ $implicit: task }"></ng-container>
    <ng-template #taskTpl let-task>
      <p class="task">{{ task }}</p>
    </ng-template>
  `
})
export class TemplateOutletDemoComponent {
  protected tasks = ['Review', 'Implementation', 'Release'];
}
```

## Best Practices
- Utilize component's `@Input() template?: TemplateRef` to allow users to replace layouts
- Document context keys so template side doesn't get confused
- Prepare default templates to create robust APIs that work even when unspecified

## Considerations
- Pay attention to the lifecycle of passed templates and perform null checks
- When injecting complex templates, readability decreases, so consider file separation
- Verify that template switching renders correctly in SSR

## Related Technologies
- TemplateRef
- ViewContainerRef
- Content Projection
