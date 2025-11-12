# #484 "Stack Trace"

Shikoku Metan: "Use stack traces inside never functions."
Zundamon: "fail logged error.stack."
Shikoku Metan: "Custom errors can call captureStackTrace."
Zundamon: "We printed the stack inside a catch block too."
Shikoku Metan: "Leaving breadcrumbs speeds up debugging."

---

## 📺 Code for Display

```typescript
/** Example 1: Print stack */
function fail(message: string): never {
  const error = new Error(message);
  console.error(error.stack);
  throw error;
}

/** Example 2: Custom AppError */
class AppError extends Error {
  constructor(message: string) {
    super(message);
    this.name = "AppError";
    Error.captureStackTrace(this, AppError);
  }
}
function throwAppError(): never {
  throw new AppError("Application error");
}

/** Example 3: Use stack trace */
try {
  fail("Something went wrong");
} catch (error) {
  if (error instanceof Error) {
    console.error("Stack trace:", error.stack);
  }
}
```
