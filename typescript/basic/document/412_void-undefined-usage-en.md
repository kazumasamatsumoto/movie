# #412 "Choosing Between void and undefined"

Shikoku Metan: "Let's revisit when to use void versus undefined."
Zundamon: "saveData only performs side effects, so it returns void."
Shikoku Metan: "Right—it signals that callers shouldn't expect data."
Zundamon: "loadData returns Data | undefined to show lookup results?"
Shikoku Metan: "Exactly; undefined tells us nothing was found."
Zundamon: "UserService separates getUser and deleteUser the same way!"
Shikoku Metan: "Fetch methods use undefined, mutating ones use void for clarity."
Zundamon: "I'll choose types based on each responsibility!"

---

## 📺 Code for Display

```typescript
/** Example 1: void: side effects */
function saveData(data: Data): void {
  database.save(data);
}

/** Example 2: undefined: may return data */
function loadData(id: number): Data | undefined {
  return database.find(id);
}

/** Example 3: Practical interface split */
interface UserService {
  getUser(id: number): User | undefined;
  deleteUser(id: number): void;
  saveUser(user: User): void;
}
```
