# #389 "Explicit return"

Shikoku Metan: "Sometimes we still write explicit return; in void functions."
Zundamon: "processData returns early after a null check."
Shikoku Metan: "Yes, it prevents unnecessary work."
Zundamon: "notify exits when notifications are disabled, too."
Shikoku Metan: "Right, it short-circuits based on conditions."
Zundamon: "I must remember that return 'value'; causes an error in invalid."
Shikoku Metan: "Never return a value from a void function."
Zundamon: "I'll choose the correct return style!"

---

## 📺 Code for Display

```typescript
/** Example 1: Early return */
function processData(data: string | null): void {
  if (data === null) return;
  console.log(data.toUpperCase());
}

/** Example 2: Conditional return */
function notify(user: User): void {
  if (!user.notifications) return;
  sendEmail(user.email);
  logNotification(user.id);
}

/** Example 3: Erroneous return */
function invalid(): void {
  return "value";  // Error
}
```
