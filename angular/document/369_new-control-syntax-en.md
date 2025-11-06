# #369 "@if / @for / @switch New Syntax"

## Overview
The new `@if`/`@for`/`@switch` syntax uses TypeScript-like block notation, balancing template readability with compile-time optimization.

## Learning Objectives
- Understand basic notation and characteristics of each syntax
- Learn track clause in `@for` and case specification in `@switch`
- Grasp practical template application examples

## Technical Points
- `@if` can nest `@else if` and `@else`
- Get additional info like `@for (item of items; track item.id; let i = $index)`
- `@switch` branches with `@case` and `@default`

## 📺 Screen Display Code (For Video)
```html
@for (task of tasks; track task.id) {
  <li>{{ task.title }}</li>
}
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
@Component({
  selector: 'app-new-syntax-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    @switch (status()) {
      @case ('loading') { <p>Loading...</p> }
      @case ('success') { <p>Success!</p> }
      @default { <p>Unknown state</p> }
    }
  `
})
export class NewSyntaxDemoComponent {
  private readonly statusSignal = signal<'loading' | 'success' | 'unknown'>('loading');
  protected status = this.statusSignal.asReadonly();
}
```

## Best Practices
- Properly write track clause to maximize `@for` performance
- Align indentation of HTML inside blocks to improve readability
- Share new syntax usage rules across team for consistent templates

## Cautions
- Template lint rule updates needed after introducing new syntax
- Be careful with scope when defining template references inside `@if`
- Verify no confusion in reviews when mixing with old syntax

## Related Technologies
- Angular v17 Template Syntax
- ESLint Template Plugins
- track clause and meta variables like $index
