# #403 "undefined Means 'An Undefined Value'"

Shikoku Metan: "undefined signals that the function may return the undefined value itself."
Zundamon: "findUser becomes undefined when it can't locate anything."
Shikoku Metan: "Right, callers check whether the result is undefined."
Zundamon: "Optional properties like Config.timeout can be undefined too?"
Shikoku Metan: "Exactly; missing properties resolve to undefined."
Zundamon: "Unlike void, we still treat it as data."
Shikoku Metan: "Making undefined explicit keeps edge cases safe."
Zundamon: "I'll pick the undefined type whenever a value might be absent!"

---

## 📺 Code for Display

```typescript
/** Example 1: undefined: a missing value */
function findUser(id: number): User | undefined {
  return users.find((u) => u.id === id);
}

/** Example 2: Check before use */
const user = findUser(1);
if (user !== undefined) {
  console.log(user.name);
}

/** Example 3: Optional property */
interface Config {
  timeout?: number;
}
const config: Config = {};
console.log(config.timeout);  // undefined
```
