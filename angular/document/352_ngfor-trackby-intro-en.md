# #352 "trackBy - Performance Optimization"

## Overview
`trackBy` is a mechanism that returns an item identifier in `*ngFor`, allowing Angular to reuse existing DOM nodes and improve rendering performance.

## Learning Objectives
- Understand the role and effect of trackBy
- Learn the signature and return value of trackBy functions
- Grasp best practices for performance improvement

## Technical Points
- Function signature is `trackBy(index, item)` returning an identifier
- Default is item reference comparison, but trackBy uses custom keys
- Effective for reducing re-rendering in large lists or when resorting

## 📺 Screen Display Code (For Video)
```html
<li *ngFor="let todo of todos; trackBy: trackById">
  {{ todo.title }}
</li>
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
interface Todo {
  id: string;
  title: string;
}

@Component({
  selector: 'app-trackby-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <ul>
      <li *ngFor="let todo of todos; trackBy: trackById">{{ todo.title }}</li>
    </ul>
  `
})
export class TrackByDemoComponent {
  protected todos: Todo[] = [
    { id: 't1', title: 'Signal Support' },
    { id: 't2', title: 'Structural Directive' }
  ];

  protected trackById(_: number, todo: Todo): string {
    return todo.id;
  }
}
```

## Best Practices
- Return unique keys (like IDs) to enable reuse even when order changes
- Make trackBy functions pure functions without state or side effects
- Extract to service for testability if complex logic is needed

## Cautions
- Returning the same value prevents Angular from distinguishing elements
- Be careful with naming when defining multiple trackBy functions in a widget
- Even with trackBy, performance issues remain if large amounts of DOM are generated

## Related Technologies
- ChangeDetectionStrategy.OnPush
- Angular Signals
- Virtual Scrolling
