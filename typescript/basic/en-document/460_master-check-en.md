# #460 "Master Check"

Shikoku Metan: "Let's finish with a master check of void patterns."
Zundamon: "Remember fundamentals like log or save."
Shikoku Metan: "Recall generics such as Callback<T> and the Angular/Nest examples."
Zundamon: "So we review every void scenario we've covered."
Shikoku Metan: "Side effects, generics, and frameworks all get a final check."

---

## 📺 Code for Display

```typescript
/** Example 1: Basic usage */
function log(msg: string): void {
  console.log(msg);
}
async function save(data: Data): Promise<void> {
  await database.save(data);
}

/** Example 2: With generics */
type Callback<T> = (data: T) => void;
const handler: Callback<User> = (user) => {
  console.log(user.name);
};

/** Example 3: Angular/Nest usage */
@Component({...})
class UserComponent {
  onClick(): void {
    this.service.save(this.user);
  }
}
```
