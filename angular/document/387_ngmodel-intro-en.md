# #387 "ngModel - Two-Way Binding"

## Overview
`ngModel` is a directive that provides two-way binding in template-driven forms, synchronizing form elements with component properties.

## Learning Objectives
- Understand the role of ngModel and its position in forms
- Grasp the mechanism of two-way binding
- Explain the differences and use cases between Reactive Forms and template-driven forms

## Technical Points
- Two-way synchronization with `[(ngModel)]` syntax
- Used by importing `FormsModule`
- Fine control of value access with `ngModelOptions`

## 📺 Display Code (for video)
```html
<input [(ngModel)]="username" placeholder="Username" />
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Component({
  selector: 'app-ngmodel-demo',
  standalone: true,
  imports: [CommonModule, FormsModule],
  template: `
    <label>
      Username
      <input [(ngModel)]="username" />
    </label>
    <p>Input value: {{ username }}</p>
  `
})
export class NgModelDemoComponent {
  protected username = '';
}
```

## Best Practices
- Use ngModel for small, simple forms and consider Reactive Forms for complex cases
- Minimize side effects of two-way binding by adding only necessary processing with `ngModelChange`
- Extract shared form logic into components or services

## Considerations
- Don't forget to import `FormsModule` when using with standalone components
- Don't use `ngModel` and Reactive Forms' `formControlName` on the same element
- Synchronization occurs every time change detection runs, so debounce heavy processing with `ngModelChange`

## Related Technologies
- FormsModule
- Reactive Forms
- ngModelChange
