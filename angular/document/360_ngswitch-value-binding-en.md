# #360 "Value Specification with [ngSwitch]"

## Overview
`[ngSwitch]` can specify arbitrary expressions, achieving rich branching by passing type-safe enum values, Signals, or Observable results.

## Learning Objectives
- Understand types of values that can be passed to `[ngSwitch]`
- Learn branching using Signal or Computed values
- Organize value specification from testing perspective

## Technical Points
- Evaluates arbitrary expressions and strictly compares with case values
- Using Union types or enums enables IDE completion
- For Observables, resolve with `AsyncPipe` before passing

## 📺 Screen Display Code (For Video)
```html
<section [ngSwitch]="state()">
  <p *ngSwitchCase="'idle'">Idle</p>
  <p *ngSwitchCase="'running'">Running</p>
</section>
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
type JobState = 'idle' | 'running' | 'failed';

@Component({
  selector: 'app-switch-value-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <section [ngSwitch]="state()">
      <p *ngSwitchCase="'idle'">Job is waiting.</p>
      <p *ngSwitchCase="'running'">Job is executing.</p>
      <p *ngSwitchCase="'failed'">Job failed.</p>
      <p *ngSwitchDefault>Unknown state.</p>
    </section>
  `
})
export class SwitchValueDemoComponent {
  private readonly stateSignal = signal<JobState>('idle');
  protected state = this.stateSignal.asReadonly();
}
```

## Best Practices
- Define values with Union types and maintain literal types with `const assertions`
- Using Signals or Computed makes it easier to synchronize state management and branching
- Verify display for each case in tests to prevent state transition bugs

## Cautions
- Follow with default when `null` or `undefined` may be passed
- Pre-calculate complex expressions in components as direct specification becomes hard to read
- Be careful as case value type mismatches won't match

## Related Technologies
- Angular Signals
- Enums / Literal Types
- AsyncPipe
