# #338 "*ngIf=\"condition; else template\""

## Overview
`*ngIf="expr; else tpl"` can specify a template to display when the condition is false, organizing waiting states and error displays.

## Learning Objectives
- Learn how to specify else templates
- Understand the scope of template reference variables
- Design reusable fallback templates

## Technical Points
- What's specified in `else` is a reference to `<ng-template #name>`
- Can utilize `let-` syntax to receive context within templates
- Can develop into then/else syntax for many conditional branches

## 📺 On-Screen Code (for video)
```html
<section *ngIf="data; else loading">Data display</section>
<ng-template #loading><p>Loading...</p></ng-template>
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Component({
  selector: 'app-ngif-else-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <section *ngIf="user(); else fallback">
      <h3>{{ user()!.name }}</h3>
      <p>{{ user()!.email }}</p>
    </section>
    <ng-template #fallback>
      <p>Could not retrieve user information.</p>
      <button type="button" (click)="retry()">Retry</button>
    </ng-template>
  `
})
export class NgIfElseDemoComponent {
  private readonly store = signal<{ name: string; email: string } | null>(null);
  protected user = this.store.asReadonly();

  protected retry(): void {
    setTimeout(() => {
      this.store.set({ name: 'Retry User', email: 'retry@example.com' });
    }, 500);
  }
}
```

## Best Practices
- Consolidate fallback templates into separate files or reusable templates
- Design to pass context variables like `let-error` to display details
- Consider focus and accessibility in the else part as well

## Considerations
- Else templates can only be described within `ng-template` and cannot be used with other elements
- Be aware that DOM state is reset when the `if` side is destroyed
- When using the same template reference in multiple places, check for unintended sharing

## Related Technologies
- Template Reference Variables
- Angular Signals
- Retry pattern
