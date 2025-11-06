# #341 "Specifying both then/else"

## Overview
By specifying both then/else templates in `*ngIf`, you can clearly separate the display for each condition while reducing template duplication.

## Learning Objectives
- Understand the placement and naming of then/else templates
- Extract common parts to avoid template duplication
- Learn structuring techniques to organize complex branching

## Technical Points
- Specify separate template references with `then` and `else`
- Extract common parts using `ng-container` or child components
- Context variables can pass data to templates

## 📺 Screen Display Code (For Video)
```html
<div *ngIf="status === 'success'; then successTpl; else failTpl"></div>
<ng-template #successTpl><p>Processing successful</p></ng-template>
<ng-template #failTpl><p>Failed</p></ng-template>
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
type LoadState = 'loading' | 'success' | 'error';

@Component({
  selector: 'app-then-else-both-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <ng-container *ngIf="state() === 'success'; then successTpl; else pendingTpl"></ng-container>
    <ng-template #successTpl>
      <h2>Dashboard</h2>
      <p>Displaying the latest data.</p>
    </ng-template>
    <ng-template #pendingTpl>
      <section *ngIf="state() === 'loading'; else errorTpl">
        <p>Loading...</p>
      </section>
    </ng-template>
    <ng-template #errorTpl>
      <p>Failed to load.</p>
      <button type="button" (click)="retry()">Retry</button>
    </ng-template>
  `
})
export class ThenElseBothDemoComponent {
  private readonly stateSignal = signal<LoadState>('loading');
  protected state = this.stateSignal.asReadonly();

  protected retry(): void {
    this.stateSignal.set('loading');
    setTimeout(() => this.stateSignal.set('success'), 600);
  }
}
```

## Best Practices
- Clarify template references with names like `successTpl`, `errorTpl` to indicate their role
- Group common parts with `ng-container`, leaving only the differences in each template block
- Test that each state switches correctly to prevent regressions

## Cautions
- As templates increase, scope becomes complex, so adhere to naming conventions
- When branching many states, consider `*ngSwitch` or the new `@switch` syntax
- With SSR, if states differ, Hydration may fail, so ensure initial values match

## Related Technologies
- ng-container
- Angular Signals
- Template Composition
