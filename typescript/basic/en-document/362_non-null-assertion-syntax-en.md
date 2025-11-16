# #362 "Syntax of the ! Operator"

Shikoku Metan: "Let's review the syntax patterns of the ! operator."
Zundamon: "It starts with expressions like value!.length, right?"
Shikoku Metan: "Yes, if the type is string | null, the ! narrows it to string."
Zundamon: "Can we attach it to properties too?"
Shikoku Metan: "Sure, but only when we're sure user.name exists, such as user.name!.toUpperCase()."
Zundamon: "What about functions or chained calls?"
Shikoku Metan: "The same syntax applies to document.getElementById("app")! or array.find(... )!."
Zundamon: "I'll remember the syntax and the safety implications together!"

---

## 📺 Code for Display

```typescript
/** Example 1: Applying it to a variable */
let value: string | null = getValue();
const length = value!.length;

/** Example 2: Property access */
const user: { name?: string } = getUser();
const name = user.name!.toUpperCase();

/** Example 3: Function and method calls */
const element = document.getElementById("app")!;
const firstChild = element.firstChild!;
const data = array.find(x => x.id === 1)!;
```
