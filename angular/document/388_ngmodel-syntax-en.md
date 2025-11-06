# #388 "Using [(ngModel)]"

## Overview
The `[(ngModel)]` syntax is syntactic sugar that combines property binding and event binding, synchronizing values between templates and components.

## Learning Objectives
- Understand the structure of `[(ngModel)]` and the actual processing that occurs
- Grasp how to use it with standalone components
- Learn coordination with form controls

## Technical Points
- `[(ngModel)]="value"` is syntactic sugar for `[ngModel]="value"` + `(ngModelChange)="value = $event"`
- Without a `name` attribute, it won't be automatically registered in template-driven forms
- Setting `standalone: true` in `ngModelOptions` allows usage outside the parent form

## 📺 Display Code (for video)
```html
<input [(ngModel)]="email" name="email" />
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Component({
  selector: 'app-ngmodel-syntax-demo',
  standalone: true,
  imports: [CommonModule, FormsModule],
  template: `
    <form>
      <label>
        Email
        <input [(ngModel)]="email" name="email" />
      </label>
      <label>
        Nickname
        <input [(ngModel)]="nickname" name="nickname" />
      </label>
    </form>
    <pre>{{ { email, nickname } | json }}</pre>
  `
})
export class NgModelSyntaxDemoComponent {
  protected email = '';
  protected nickname = '';
}
```

## Best Practices
- Add name attributes to ensure form controls are properly managed
- Don't overuse two-way binding; consider `[value]` + `(input)` when one-way is sufficient
- Handle with `ngModelChange` when change monitoring is needed

## Considerations
- If you want to change `value` directly from outside the component, reference with `@ViewChild(NgModel)`
- If you forget to set `standalone: true`, it may be unintentionally registered in the parent form
- Two-way binding can complicate tests, so assess necessity

## Related Technologies
- ngModelChange
- Template-driven Forms
- Migration to Reactive Forms
