# #312 "Behavior When Disabled"

Shikoku Metan「Let's learn about the behavior when strictNullChecks is disabled!」
Zundamon「What happens when it's disabled?」
Shikoku Metan「Yes. All types implicitly include null and undefined, allowing dangerous code to be written.」
Zundamon「Assigning null to a string type and calling toUpperCase() causes a runtime error!」
Shikoku Metan「Exactly. Since it doesn't result in a compile error, bugs are hard to notice.」
Zundamon「Passing null as a function argument doesn't cause an error either?」
Shikoku Metan「Yes. Calls like greet(null) are possible, with the risk of crashing at runtime.」
Zundamon「Type checking is insufficient, so you should enable strictNullChecks!」

---

## 📺 Code for Display

```typescript
/** Example 1: Risk of runtime errors */
// strictNullChecks: false
let name: string = null; // OK
name.toUpperCase(); // Runtime error!

/** Example 2: All types include null/undefined */
function greet(name: string) {
  // name might be null
  return name.toUpperCase(); // Dangerous
}
greet(null); // No error

/** Example 3: Insufficient type checking */
interface User {
  name: string;
}
const user: User = { name: null }; // OK
```
