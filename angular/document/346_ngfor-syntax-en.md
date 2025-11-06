# #346 "Basic *ngFor Syntax"

## Overview
The basic syntax of `*ngFor` is `*ngFor="let item of items"`, which expands collection elements within the template.

## Learning Objectives
- Understand the meaning of `let` declaration and `of` keyword
- Grasp syntax for declaring additional variables inline
- Learn patterns for handling Iterables other than arrays

## Technical Points
- Provides syntactic sugar like `let item of items; let i = index`
- `items` can be arrays, `ReadonlyArray`, `Iterable`, `Signal` results, etc.
- Set identifier with `; trackBy: fn` to promote reuse

## 📺 Screen Display Code (For Video)
```html
<div *ngFor="let user of users; let i = index">
  {{ i + 1 }}. {{ user }}
</div>
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
@Component({
  selector: 'app-ngfor-syntax-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <ul>
      <li *ngFor="let user of users; let i = index">
        {{ i + 1 }}: {{ user }}
      </li>
    </ul>
  `
})
export class NgForSyntaxDemoComponent {
  protected users = ['Alice', 'Bob', 'Carol'];
}
```

## Best Practices
- Keep collections Readonly to avoid side effects
- Use context variables to simplify template logic
- Suppress DOM regeneration by using trackBy together

## Cautions
- Syntax after `;` depends on order, so arrange for readability
- Avoid method calls in `items` as they're evaluated each time
- When passing Signals directly to `items`, call with `items()`

## Related Technologies
- Angular Signals
- trackBy
- Structural Directive syntactic sugar
