# #345 "*ngFor - Repeating Display"

## Overview
`*ngFor` is a structural directive that iterates over collections to generate elements, providing the foundation for list rendering.

## Learning Objectives
- Understand the basic role of *ngFor
- Grasp context variables available within templates
- Be aware of trackBy for performance

## Technical Points
- Use `let item of items` syntax to expand arrays or Iterables
- Variables like `index`, `first`, `last`, `even`, `odd`, `count` are available
- `trackBy` promotes DOM reuse

## 📺 Screen Display Code (For Video)
```html
<li *ngFor="let task of tasks">{{ task.title }}</li>
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
interface Task {
  id: number;
  title: string;
}

@Component({
  selector: 'app-ngfor-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <ul>
      <li *ngFor="let task of tasks; trackBy: trackById">
        {{ task.title }}
      </li>
    </ul>
  `
})
export class NgForDemoComponent {
  protected tasks: Task[] = [
    { id: 1, title: 'Learning Directives' },
    { id: 2, title: 'Component Decomposition' }
  ];

  protected trackById(_: number, task: Task): number {
    return task.id;
  }
}
```

## Best Practices
- Treat data as immutable objects and generate new arrays when making changes
- Implement trackBy to minimize re-rendering
- Perform sorting and filtering on the component side to keep templates simple

## Cautions
- Consider optimizations like virtual scrolling for long lists
- Using `index` as a key will regenerate DOM when order changes
- For async data, ensure unsubscription with `AsyncPipe`

## Related Technologies
- trackBy
- Angular CDK Virtual Scroll
- AsyncPipe
