# #389 "Integration with Form Elements"

## Overview
`ngModel` integrates with form elements such as input, select, and textarea, synchronizing user input with components. Option settings for each element are also possible.

## Learning Objectives
- Understand points for using ngModel with each form element
- Learn how to set name, updateOn, etc. with `ngModelOptions`
- Grasp the distinction between standalone forms and template-driven forms

## Technical Points
- For select elements, handle selected values with `[ngModel]` and `(ngModelChange)`
- Set `standalone`, `name`, `updateOn` with `ngModelOptions`
- `[(ngModel)]` depends on the `NgModel` directive from `FormsModule`

## 📺 Display Code (for video)
```html
<select [(ngModel)]="selected" name="plan">
  <option value="basic">Basic</option>
  <option value="pro">Pro</option>
</select>
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Component({
  selector: 'app-ngmodel-form-elements-demo',
  standalone: true,
  imports: [CommonModule, FormsModule],
  template: `
    <form>
      <label>
        Plan
        <select [(ngModel)]="plan" name="plan">
          <option value="basic">Basic</option>
          <option value="pro">Pro</option>
          <option value="enterprise">Enterprise</option>
        </select>
      </label>
      <label>
        Memo
        <textarea [(ngModel)]="memo" name="memo"></textarea>
      </label>
    </form>
    <pre>{{ { plan, memo } | json }}</pre>
  `
})
export class NgModelFormElementsDemoComponent {
  protected plan = 'basic';
  protected memo = '';
}
```

## Best Practices
- For select elements, use Union types to clarify choice constraints
- Change update timing with `updateOn: 'blur'` to suppress changes during input
- For textarea, implement character counting by combining with `ngModelChange`

## Considerations
- When bundling radio buttons, need to align `name` attributes
- Not setting `standalone: true` may affect parent form validation
- Use `[ngValue]` when handling objects with `select`

## Related Technologies
- ngModelOptions
- Template-driven Forms
- Reactive Forms
