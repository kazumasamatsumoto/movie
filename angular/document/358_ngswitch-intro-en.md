# #358 "*ngSwitch - Multi-way Branching"

## Overview
`*ngSwitch` is a structural directive that expresses value-based multi-way branching in templates, organizing conditions and providing readable structure.

## Learning Objectives
- Understand the structure and usage of `*ngSwitch`
- Learn how to combine `*ngSwitchCase`/`*ngSwitchDefault`
- Know how to organize templates with multiple branches

## Technical Points
- Specify target value with `[ngSwitch]="value"`
- Declare branches with `*ngSwitchCase="'caseValue'"`
- Display `*ngSwitchDefault` when no case matches

## 📺 Screen Display Code (For Video)
```html
<section [ngSwitch]="status">
  <p *ngSwitchCase="'loading'">Loading...</p>
  <p *ngSwitchCase="'done'">Complete!</p>
  <p *ngSwitchDefault>Unknown state</p>
</section>
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
type Status = 'loading' | 'done' | 'error';

@Component({
  selector: 'app-switch-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <section [ngSwitch]="status()">
      <p *ngSwitchCase="'loading'">Loading...</p>
      <p *ngSwitchCase="'done'">Completed.</p>
      <p *ngSwitchCase="'error'">An error occurred.</p>
      <p *ngSwitchDefault>Unknown state.</p>
    </section>
    <button (click)="cycle()">Change state</button>
  `
})
export class SwitchDemoComponent {
  private readonly statuses: Status[] = ['loading', 'done', 'error'];
  private index = 0;
  private readonly statusSignal = signal<Status>('loading');
  protected status = this.statusSignal.asReadonly();

  protected cycle(): void {
    this.index = (this.index + 1) % this.statuses.length;
    this.statusSignal.set(this.statuses[this.index]);
  }
}
```

## Best Practices
- Manage states type-safely using enums or Union types
- Componentize each case for complex UI, leaving only invocations in switch
- Always provide default case to visualize unexpected states

## Cautions
- Case values are determined by strict comparison (===), so match types and values
- Consider `@switch` syntax when templates get long with many cases
- With SSR, state mismatches may fall to default, so align initial values

## Related Technologies
- Union Types
- Angular Signals
- Control Flow Syntax
