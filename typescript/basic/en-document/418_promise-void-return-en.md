# #418 "No return in Promise<void>"

Shikoku Metan: "Promise<void> functions can omit return statements."
Zundamon: "saveUser finished without returning anything."
Shikoku Metan: "Right, even early exits just use return;."
Zundamon: "Is returning undefined allowed like in log?"
Shikoku Metan: "It is, though omitting it is cleaner."
Zundamon: "So the standard void rules still apply to async code."
Shikoku Metan: "Promise<void> doesn't require special return handling."
Zundamon: "I'll pick the right return style every time!"

---

## 📺 Code for Display

```typescript
/** Example 1: No return */
async function saveUser(user: User): Promise<void> {
  await database.save(user);
  console.log("User saved");
}

/** Example 2: Early return */
async function validate(data: Data): Promise<void> {
  if (!data) return;
  await processData(data);
}

/** Example 3: return undefined */
async function log(msg: string): Promise<void> {
  console.log(msg);
  return undefined;
}
```
