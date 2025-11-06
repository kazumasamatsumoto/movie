# #379 "Conditional Class Application"

## Overview
Conditional classes use `ngClass` to apply state-based classes, achieving visual feedback and accessibility improvements.

## Learning Objectives
- Understand considerations when designing conditional classes
- Learn method to manage state on component side and simplify templates
- Be able to apply in diverse scenarios like forms and lists

## Technical Points
- Prepare table mapping states to classes
- Returning class sets with computed or getters makes testing easier
- Use together with accessibility attributes (`aria-*`)

## 📺 Screen Display Code (For Video)
```html
<input [ngClass]="{ 'is-invalid': control.invalid && control.touched }" />
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
@Component({
  selector: 'app-conditional-class-demo',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  template: `
    <form [formGroup]="form">
      <label>
        Email
        <input formControlName="email" [ngClass]="classMap('email')" />
      </label>
      <p *ngIf="form.controls.email.invalid && form.controls.email.touched" class="error">
        Please enter a valid email address
      </p>
    </form>
  `,
  styles: [`
    input { border: 1px solid #94a3b8; border-radius: 0.5rem; padding: 0.5rem; width: 100%; }
    .is-invalid { border-color: #f97316; background: #fff7ed; }
    .error { color: #f97316; font-size: 0.875rem; }
  `]
})
export class ConditionalClassDemoComponent {
  protected form = new FormGroup({
    email: new FormControl('', { nonNullable: true, validators: [Validators.email, Validators.required] })
  });

  protected classMap(controlName: string): Record<string, boolean> {
    const control = this.form.controls[controlName];
    return { 'is-invalid': control.invalid && control.touched };
  }
}
```

## Best Practices
- Switch classes based on form state or API responses to give users clear feedback
- Also set accessibility attributes like `aria-invalid` alongside class application
- Organize priority to avoid multiple conditions conflicting and document

## Cautions
- Guard null when referencing classes while control doesn't exist or error occurs
- When switching display with classes, also set `role` or `aria-live` if needed
- Move logic to component methods or services when conditions become complex

## Related Technologies
- Reactive Forms
- Accessibility Attributes
- Angular Signals
