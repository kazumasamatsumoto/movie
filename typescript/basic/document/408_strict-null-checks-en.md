# #408 "strictNullChecks"

Shikoku Metan: "strictNullChecks changes how void and undefined behave."
Zundamon: "When it's true, voidValue can't receive null."
Shikoku Metan: "Correct—only undefined is accepted."
Zundamon: "With strictNullChecks: false, null sneaks in?"
Shikoku Metan: "It does, though it's discouraged."
Zundamon: "I should also recall the difference between f1(): void and f2(): undefined."
Shikoku Metan: "void ignores returns, undefined signifies that value."
Zundamon: "I'll keep the setting-specific behavior in mind!"

---

## 📺 Code for Display

```typescript
/** Example 1: strictNullChecks: true */
let voidValue: void;
voidValue = undefined;
let undefValue: undefined;
undefValue = undefined;

/** Example 2: strictNullChecks: false */
let value: void;
value = undefined;
value = null;

/** Example 3: Function signatures */
function f1(): void {}
function f2(): undefined {
  return undefined;
}
```
