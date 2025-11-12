# #441 "Angular Event Handlers"

Shikoku Metan: "Angular event handlers are classic void functions."
Zundamon: "onClick(): void handled button clicks."
Shikoku Metan: "Form submissions and input events follow the same pattern."
Zundamon: "We bind (click) in the template to those methods, right?"
Shikoku Metan: "Exactly; since no value is returned, void fits perfectly."
Zundamon: "All logic stays inside the component class."
Shikoku Metan: "Side effects simply update the UI."
Zundamon: "I'll keep Angular handlers void and tidy!"

---

## 📺 Code for Display

```typescript
/** Example 1: Angular component */
@Component({
  selector: 'app-user',
  template: '<button (click)="onClick()">Click</button>'
})
export class UserComponent {
  onClick(): void {
    console.log('Button clicked');
  }
}

/** Example 2: Form submission */
@Component({
  selector: 'app-form',
  template: '<form (submit)="onSubmit()">...</form>'
})
export class FormComponent {
  onSubmit(): void {
    console.log('Form submitted');
  }
}

/** Example 3: Input event */
onInput(event: Event): void {
  const value = (event.target as HTMLInputElement).value;
  console.log('Input:', value);
}
```
