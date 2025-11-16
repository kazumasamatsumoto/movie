# #506 "If-Else Exhaustiveness"

Shikoku Metan: "Exhaustiveness works in if-else chains too."
Zundamon: "We defined the Status union and an exhaustiveCheck() helper first."
Shikoku Metan: "handleStatus() walks pending, success, and error with if statements."
Zundamon: "The final else returns exhaustiveCheck(status) to accept never."
Shikoku Metan: "Missing any condition drops into that branch and fails compilation."
Zundamon: "The extended Status with 'timeout' immediately triggered an error."
Shikoku Metan: "Even pure if chains can detect new union members."
Zundamon: "Every union bump turns exhaustiveCheck into a safety net."

---

## 📺 Code for Display

```typescript
/** Example 1: never-returning helper */
type Status = "pending" | "success" | "error";

function exhaustiveCheck(value: never): never {
  throw new Error(`Unhandled: ${value}`);
}

/** Example 2: Exhaustive if-else */
function handleStatus(status: Status): string {
  if (status === "pending") return "Processing";
  else if (status === "success") return "Done";
  else if (status === "error") return "Failed";
  else return exhaustiveCheck(status);
}

/** Example 3: Detecting new cases */
type StatusWithTimeout = "pending" | "success" | "error" | "timeout";

function handle(status: StatusWithTimeout): string {
  if (status === "pending") return "Processing";
  // Skipping the other branches makes exhaustiveCheck complain
  return exhaustiveCheck(status);
}
```
