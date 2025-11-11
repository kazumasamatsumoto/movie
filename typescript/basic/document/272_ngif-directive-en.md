# #272 "*ngIf Directive"

Shikoku Metan: "Let's learn about the *ngIf directive!"
Zundamon: "We can toggle element visibility based on conditions!"
Shikoku Metan: "That's right. Elements are displayed only when the boolean value is true."
Zundamon: "With the else clause, we can also set what to display when the condition is false, right?"
Shikoku Metan: "Exactly. Combined with ng-template, it allows flexible control."
Zundamon: "Since DOM elements themselves are added or removed, it's good for performance too!"
Shikoku Metan: "Unlike CSS display:none, the important point is that elements are completely removed."
Zundamon: "There are many practical scenarios like UI switching based on login status!"

---

## 📺 Code for Display

```typescript
// *ngIf directive

@Component({
  selector: 'app-example',
  template: `
    <div *ngIf="isVisible">Will be displayed</div>

    <div *ngIf="isLoggedIn; else loginTemplate">
      Logged in
    </div>
    <ng-template #loginTemplate>
      Not logged in
    </ng-template>
  `
})
export class ExampleComponent {
  isVisible: boolean = true;
  isLoggedIn: boolean = false;
}
```
