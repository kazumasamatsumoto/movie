# #367 "Mistake (2) - Missing Checks"

Shikoku Metan: "Writing ! too early makes us skip null checks."
Zundamon: "processUser calling findUser(id)! would crash when the ID is missing."
Shikoku Metan: "Exactly—if it returns null, property access throws immediately."
Zundamon: "So the correct flow is to test for null first?"
Shikoku Metan: "Yes, guard it with if (user === null) return; or similar early exits."
Zundamon: "Optional Chaining also fetches the name safely?"
Shikoku Metan: "user?.name ?? 'Unknown' reads it without risking a crash."
Zundamon: "I won't rely on ! to hide missing checks!"

---

## 📺 Code for Display

```typescript
/** Example 1: Example of a missed check */
function processUser(id: number) {
  const user = findUser(id)!;  // Ignores possible null
  console.log(user.name);      // May throw at runtime
}

/** Example 2: Proper check */
function processUser(id: number) {
  const user = findUser(id);
  if (user === null) {
    console.log("User not found");
    return;
  }
  console.log(user.name);  // Safe
}

/** Example 3: Handling it with Optional Chaining */
function processUser(id: number) {
  const user = findUser(id);
  const name = user?.name ?? "Unknown";
  console.log(name);
}
```
