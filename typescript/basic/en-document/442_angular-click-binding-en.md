# #442 "(click)='onClick()'"

Shikoku Metan: "Angular's (click) bindings also rely on void methods."
Zundamon: "handleClick(): void is the standard form."
Shikoku Metan: "$event gives access to MouseEvent if needed."
Zundamon: "We can pass arguments like delete(user.id) too."
Shikoku Metan: "Yes, since no value is returned, void is appropriate."
Zundamon: "Templates stay readable when handlers share this pattern."
Shikoku Metan: "Keep side-effect logic inside the component class."
Zundamon: "I'll keep my (click) handlers void!"

---

## 📺 Code for Display

```typescript
/** Example 1: Basic click handler */
@Component({
  selector: 'app-button',
  template: '<button (click)="handleClick()">Click</button>'
})
export class ButtonComponent {
  handleClick(): void {
    console.log('Clicked');
  }
}

/** Example 2: Receiving $event */
@Component({
  template: '<button (click)="onClick($event)">Click</button>'
})
export class Component {
  onClick(event: MouseEvent): void {
    console.log('Position:', event.clientX, event.clientY);
  }
}

/** Example 3: Passing arguments */
@Component({
  template: '<button (click)="delete(user.id)">Delete</button>'
})
export class UserListComponent {
  delete(id: number): void {
    console.log('Deleting user:', id);
  }
}
```
