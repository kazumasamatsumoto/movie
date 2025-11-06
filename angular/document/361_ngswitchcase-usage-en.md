# #361 "*ngSwitchCase - Case Branching"

## Overview
`*ngSwitchCase` is a structural directive that displays templates when matching the value specified by `[ngSwitch]`, allowing organized case-specific UI.

## Learning Objectives
- Understand the function and placement of `*ngSwitchCase`
- Learn techniques to share common templates across multiple cases
- Grasp case value types and comparison rules

## Technical Points
- `*ngSwitchCase` uses strict comparison for matching
- Use template references to share common templates across multiple cases
- Case order doesn't matter; the first matching case is displayed

## 📺 Screen Display Code (For Video)
```html
<p *ngSwitchCase="'success'">Succeeded</p>
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
type PaymentStatus = 'pending' | 'succeeded' | 'failed';

@Component({
  selector: 'app-switchcase-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <section [ngSwitch]="status">
      <p *ngSwitchCase="'pending'">Payment processing.</p>
      <p *ngSwitchCase="'succeeded'">Payment completed.</p>
      <p *ngSwitchCase="'failed'">Payment failed.</p>
      <p *ngSwitchDefault>Unknown status.</p>
    </section>
  `
})
export class SwitchCaseDemoComponent {
  protected status: PaymentStatus = 'pending';
}
```

## Best Practices
- Manage case values with constants or enums to prevent typos
- Use `ng-template` to share common UI across multiple cases
- Detect exception states in default case and enhance quality with logging

## Cautions
- Passing objects or arrays as case values won't match as references change each time
- String comparison is case-sensitive, so maintain consistency
- With SSR, state changes may cause cases not to match, displaying default

## Related Technologies
- Union Types
- Template Reference Variables
- SSR/Hydration
