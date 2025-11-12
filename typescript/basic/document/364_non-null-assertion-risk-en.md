# #364 "Risks of the ! Operator"

Shikoku Metan: "Overusing ! easily causes runtime errors."
Zundamon: "document.getElementById('app')! would crash if it returned null…"
Shikoku Metan: "Right—touching innerHTML on a missing DOM node will blow up."
Zundamon: "Is users.find(...)! risky for array lookups too?"
Shikoku Metan: "Yes, if the element is missing you'll read properties on undefined."
Zundamon: "So we should guard the value when we want safety?"
Shikoku Metan: "Exactly; checks like if (element !== null) { ... } prevent the exception."
Zundamon: "I'll remember that every ! comes with hidden risk!"

---

## 📺 Code for Display

```typescript
/** Example 1: Dangerous DOM access */
const element = document.getElementById("app")!;
element.innerHTML = "Hello";  // Throws if element is null

/** Example 2: Runtime error example */
const user = users.find(u => u.id === 999)!;
console.log(user.name);  // Errors when undefined

/** Example 3: Safer alternative */
const element = document.getElementById("app");
if (element !== null) {
  element.innerHTML = "Hello";  // Safe
}
```
