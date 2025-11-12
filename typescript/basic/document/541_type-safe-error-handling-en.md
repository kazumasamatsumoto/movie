# #541 "Type-Safe Error Handling"

Shikoku Metan: "Use Result or Either to keep errors type-safe."
Zundamon: "Result<T, E> splits success and failure with an ok flag."
Shikoku Metan: "divide() returns { ok: false } on zero division, otherwise the value."
Zundamon: "handleResult() checks result.ok twice and falls back to const check: never."
Shikoku Metan: "Either<L, R> labels JSON parsing results as left/right."
Zundamon: "parseJson() returns right on success or left with an Error."
Shikoku Metan: "AppError's handleError() covered validation, network, and business cases."
Zundamon: "Unknown errors hit the never guard immediately."

---

## 📺 Code for Display

```typescript
/** Example 1: Result-based divide */
type Result<T, E> =
  | { ok: true; value: T }
  | { ok: false; error: E };

function divide(a: number, b: number): Result<number, string> {
  if (b === 0) return { ok: false, error: "Division by zero" };
  return { ok: true, value: a / b };
}

function handleResult(result: Result<number, string>): number {
  if (result.ok) return result.value;
  if (!result.ok) throw new Error(result.error);
  const check: never = result;
  return check;
}
```

```typescript
/** Example 2: Either type */
type Either<L, R> =
  | { type: "left"; value: L }
  | { type: "right"; value: R };

function parseJson<T>(json: string): Either<Error, T> {
  try {
    return { type: "right", value: JSON.parse(json) };
  } catch (e) {
    return { type: "left", value: e as Error };
  }
}
```

```typescript
/** Example 3: AppError handling */
type AppError =
  | { type: "validation"; field: string }
  | { type: "network"; code: number }
  | { type: "business"; message: string };

function handleError(error: AppError): string {
  if (error.type === "validation") return `Invalid: ${error.field}`;
  if (error.type === "network") return `HTTP ${error.code}`;
  if (error.type === "business") return error.message;
  const check: never = error;
  return "Unknown error";
}
```
