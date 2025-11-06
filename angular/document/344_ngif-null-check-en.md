# #344 "Null Check with *ngIf"

## Overview
`*ngIf` works well with `null` checks, allowing non-null variables to be safely handled within templates using the `as` syntax.

## Learning Objectives
- Understand how to use `*ngIf` as a `null` guard
- Learn techniques to narrow types with the `as` syntax
- Design conditional expressions that distinguish between null and undefined

## Technical Points
- With `*ngIf="value as v"`, `v` can be treated as non-null
- Template type checking works effectively in `strictNullChecks` environment
- Prepare else template to handle unfetched state

## 📺 Screen Display Code (For Video)
```html
<div *ngIf="user; as u">
  <span>{{ u.name }}</span>
</div>
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
interface Detail {
  title: string;
  description: string;
}

@Component({
  selector: 'app-null-check-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <section *ngIf="detail(); as d; else placeholder">
      <h2>{{ d.title }}</h2>
      <p>{{ d.description }}</p>
    </section>
    <ng-template #placeholder>
      <p>No data available yet.</p>
    </ng-template>
  `
})
export class NullCheckDemoComponent {
  private readonly detailSignal = signal<Detail | null>(null);
  protected detail = this.detailSignal.asReadonly();

  protected load(): void {
    this.detailSignal.set({ title: 'Angular Null Check', description: 'Safe handling of null' });
  }
}
```

## Best Practices
- Explicitly branching with `*ngIf` makes template intent clearer than using the `??` operator
- When async processing results are `null`, log the reason to make debugging easier
- Use meaningful template reference names like `detail` to improve readability

## Cautions
- `0` or empty string are not null, so they need to be handled with separate conditions
- Missed null checks causing template errors can be detected with `strictTemplates`
- Also provide guidance on the else template side to avoid hurting UX

## Related Technologies
- strictNullChecks
- Angular Signals
- Template Type Checking
