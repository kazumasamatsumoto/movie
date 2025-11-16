# #294 "Null Patterns"

Shikoku Metan「Let's learn about design patterns using null!」
Zundamon「What patterns are there?」
Shikoku Metan「Yes. There are Repository, Option type, and Null Object patterns.」
Zundamon「Repository pattern returns null from find methods!」
Shikoku Metan「Exactly. It returns null when not found.」
Zundamon「Option type increases safety with T | null?」
Shikoku Metan「Yes. By explicitly handling null, we prevent errors.」
Zundamon「Null Object pattern uses ?? to set default values!」

---

## 📺 Code for Display

```typescript
/** Example 1: Repository pattern */
class UserRepository {
  findById(id: number): User | null {
    return this.users.find(u => u.id === id) ?? null;
  }
}

/** Example 2: Option type pattern */
type Option<T> = T | null;
function safeDivide(a: number, b: number): Option<number> {
  return b !== 0 ? a / b : null;
}

/** Example 3: Null Object pattern */
const user = findUser(id) ?? createGuestUser();
if (user !== null) {
  console.log(user.name);
}
```
