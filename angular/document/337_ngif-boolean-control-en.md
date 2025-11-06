# #337 "Display Control with Boolean Values"

## Overview
Display control with boolean values using `*ngIf` is the most basic pattern, defining state flags to switch the UI.

## Learning Objectives
- Design display control using boolean flags
- Understand how to convert Signal/Observable values to boolean
- Prevent common bugs when handling falsy values

## Technical Points
- Explicitly convert to boolean with `!!value`
- Resolve Observables with `AsyncPipe` and perform truthy/falsy judgment
- High readability by consolidating state with `signal` or `computed`

## 📺 On-Screen Code (for video)
```html
<button (click)="toggle()">Toggle</button>
<div *ngIf="isVisible">Currently visible</div>
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Component({
  selector: 'app-boolean-control-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <label>
      <input type="checkbox" [checked]="visible()" (change)="toggle()" />
      Show description
    </label>
    <section *ngIf="visible()">Section controlled by boolean value</section>
  `
})
export class BooleanControlDemoComponent {
  private readonly flag = signal(true);
  protected visible = this.flag.asReadonly();
  protected toggle(): void {
    this.flag.update(value => !value);
  }
}
```

## Best Practices
- Name boolean flags in a way that makes the state clear, like `isLoading`, `hasError`
- When using `AsyncPipe`, set default values to avoid returning null
- Utilize Signals to keep state updates and template updates simple

## Considerations
- When judging falsy values like `0` or `''`, perform explicit comparison
- Passing non-boolean types as conditions can lead to unintended displays
- When multiple flags are involved, consolidate them into a state object

## Related Technologies
- Angular Signals
- AsyncPipe
- Reactive Forms (used in state management examples)
