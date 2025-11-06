# #340 "*ngIf=\"condition; then/else\""

## Overview
`*ngIf="condition; then tplA; else tplB"` is syntax that specifies both true and false templates at once, improving visibility of conditional branching.

## Learning Objectives
- Understand the notation of then/else syntax
- Learn naming and placement of template references
- Acquire design patterns that organize conditional branching

## Technical Points
- `then` template is displayed when the condition is true, `else` when false
- Templates are defined with `<ng-template #name>` and referenced within the same scope
- Expressiveness increases when combined with `as` syntax to pass values

## 📺 On-Screen Code (for video)
```html
<section *ngIf="ready; then success; else loading"></section>
<ng-template #success><p>Complete!</p></ng-template>
<ng-template #loading><p>Processing...</p></ng-template>
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Component({
  selector: 'app-then-else-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <ng-container *ngIf="state(); then doneTpl; else pendingTpl"></ng-container>
    <ng-template #doneTpl>
      <h2>Completed</h2>
      <p>{{ detail }}</p>
    </ng-template>
    <ng-template #pendingTpl>
      <p>Processing is in progress. Please wait.</p>
    </ng-template>
    <button type="button" (click)="toggle()">Toggle state</button>
  `
})
export class ThenElseDemoComponent {
  private readonly status = signal(false);
  protected state = this.status.asReadonly();
  protected detail = 'Last updated: just now';

  protected toggle(): void {
    this.status.update(v => !v);
  }
}
```

## Best Practices
- Name template references in ways that clarify their role, like `successTpl`
- When using the same template in multiple places, consolidate into a common component
- Aggregate conditional logic with then/else syntax to reduce nesting

## Considerations
- Templates for then/else must be defined within the same component scope
- When display content is large, files become long, so split into separate components
- Align server and client initial values so conditions don't change during Hydration

## Related Technologies
- Angular Signals
- Template Reference Variables
- Component Composition
