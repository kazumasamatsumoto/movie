# #368 "Control Flow Syntax (v17+)"

## Overview
The Control Flow syntax introduced in Angular v17+ provides more intuitive and optimized rendering with new template notation like `@if`/`@for`/`@switch`.

## Learning Objectives
- Understand overview and benefits of Control Flow syntax
- Grasp differences from traditional `*` syntax
- Learn migration considerations

## Technical Points
- Written in `@if (condition) { ... } @else { ... }` format
- `@for (item of items; track item.id)` standardizes track clause
- `@switch` has syntax close to TypeScript switch statements

## 📺 Screen Display Code (For Video)
```html
@if (user()) {
  <p>{{ user()!.name }}</p>
} @else {
  <p>Not logged in</p>
}
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
@Component({
  selector: 'app-control-flow-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    @if (items().length === 0) {
      <p>No items.</p>
    } @else {
      @for (item of items(); track item.id) {
        <p>{{ item.label }}</p>
      }
    }
  `
})
export class ControlFlowDemoComponent {
  private readonly itemsSignal = signal([{ id: 1, label: 'New Syntax' }]);
  protected items = this.itemsSignal.asReadonly();
}
```

## Best Practices
- New syntax is opt-in, so establish project-wide adoption plan
- Always specify track clause to receive optimization benefits
- Verify behavior with tests while gradually replacing during refactoring

## Cautions
- Only available in v17+, can't build in older versions
- Verify support status of ESLint and template analysis tools
- Mixing new and traditional syntax reduces readability, so set rules

## Related Technologies
- Angular v17+
- Template Control Flow
- track clause (`track item.id`)
