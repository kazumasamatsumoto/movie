# #271 "Boolean in Angular Templates"

Shikoku Metan: "Let's use boolean in Angular templates!"
Zundamon: "We can utilize component properties in the template!"
Shikoku Metan: "That's right. The *ngIf directive allows conditional display."
Zundamon: "We can also disable buttons with the [disabled] attribute, right?"
Shikoku Metan: "Exactly. UI control is possible based on boolean state."
Zundamon: "Property binding enables dynamic control, so convenient!"
Shikoku Metan: "The key point is that TypeScript type definitions work together with Angular templates."
Zundamon: "It's an essential feature for creating reactive UIs!"

---

## 📺 Code for Display

```typescript
// Boolean in Angular templates

// Component
@Component({
  selector: 'app-user',
  template: `
    <div *ngIf="isLoggedIn">Logged in</div>
    <button [disabled]="!isValid">Submit</button>
  `
})
export class UserComponent {
  isLoggedIn: boolean = true;
  isValid: boolean = false;

  checkStatus(): void {
    if (this.isLoggedIn && this.isValid) {
      console.log('OK');
    }
  }
}
```
