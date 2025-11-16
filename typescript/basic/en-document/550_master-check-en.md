# #550 "Master Check"

Shikoku Metan: "Time for the never master check."
Zundamon: "Laws 1-4 review union/intersection plus Exclude/Extract basics."
Shikoku Metan: "neverReturn() can only assign to a never variable."
Zundamon: "handle() on Status covers pending/success/error before calling exhaustiveCheck."
Shikoku Metan: "Result<T, E> and ApiResponse<T> unions drive safe error handling."
Zundamon: "unwrap() and handleResponse() end with const check: never = result;."
Shikoku Metan: "Master these patterns and never design gets easy."
Zundamon: "Even spec changes stay under control."

---

## 📺 Code for Display

```typescript
/** Example 1: Recap core laws */
type Law1 = string | never;              // string
type Law2 = string & never;              // never
type Law3 = Exclude<string, never>;      // string
type Law4 = Extract<never, string>;      // never

function neverReturn(): never {
  throw new Error();
}

const unreachable: never = neverReturn();
```

```typescript
/** Example 2: Exhaustive check */
type Status = "pending" | "success" | "error";

function exhaustiveCheck(value: never): never {
  throw new Error(`Unhandled: ${value}`);
}

function handle(status: Status): string {
  if (status === "pending") return "Processing";
  if (status === "success") return "Done";
  if (status === "error") return "Failed";
  return exhaustiveCheck(status);
}
```

```typescript
/** Example 3: Type-safe patterns */
type Result<T, E> =
  | { ok: true; value: T }
  | { ok: false; error: E };

type ApiResponse<T> =
  | { status: "success"; data: T }
  | { status: "error"; error: string };

function unwrap<T, E>(result: Result<T, E>): T {
  if (result.ok) return result.value;
  if (!result.ok) throw result.error;
  const check: never = result;
  return check;
}
```
