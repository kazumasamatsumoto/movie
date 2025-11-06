# #349 "index - Getting Index"

## Overview
In `*ngFor`, you can get a 0-based index with `let i = index`, which can be used for displaying numbers or conditional style branching.

## Learning Objectives
- Understand usage and scope of the `index` variable
- Utilize for display numbers and style control
- Learn advanced usage examples combined with `count`

## Technical Points
- `index` starts from 0 and is updated for each iteration
- Get total count with `count` to calculate reverse index
- Get multiple variables with `*ngFor="let item of items; let i = index; let count = count"`

## 📺 Screen Display Code (For Video)
```html
<li *ngFor="let city of cities; let i = index">
  {{ i + 1 }}. {{ city }}
</li>
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
@Component({
  selector: 'app-ngfor-index-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <ol>
      <li *ngFor="let city of cities; let i = index; let count = count">
        {{ i + 1 }} / {{ count }}: {{ city }}
      </li>
    </ol>
  `
})
export class NgForIndexDemoComponent {
  protected cities = ['Sapporo', 'Sendai', 'Tokyo', 'Fukuoka'];
}
```

## Best Practices
- Adjust display numbers like `i + 1` in templates
- Use expressions like `[class.is-odd]="i % 2 === 1"` for conditional styles
- Precalculate complex logic like reverse display in components

## Cautions
- Using `index` as trackBy return value regenerates DOM when reordering
- Avoid confusion by changing variable names in nested *ngFor
- `index` is read-only and cannot be reassigned

## Related Technologies
- trackBy
- CSS Class Binding
- Computed Signals
