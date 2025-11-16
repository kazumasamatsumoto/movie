# #512 "Type Narrowing"

Shikoku Metan: "Let's tame unions via type narrowing."
Zundamon: "handle() inspected Response.status for 200/404/500."
Shikoku Metan: "Writing const check: never = res; proves the union is fully narrowed."
Zundamon: "process() used typeof to branch across string, number, and boolean."
Shikoku Metan: "Sequential conditions let the compiler infer what remains."
Zundamon: "An `in` guard lets us peel object unions step by step too."
Shikoku Metan: "narrowLog() split on data vs. error keys cleanly."
Zundamon: "Careful narrowing reinforces exhaustive checks."

---

## 📺 Code for Display

```typescript
/** Example 1: Narrow HTTP responses */
type Response =
  | { status: 200; data: string }
  | { status: 404; error: string }
  | { status: 500; error: string };

function handle(res: Response) {
  if (res.status === 200) {
    console.log(res.data);
  } else if (res.status === 404) {
    console.log(res.error);
  } else if (res.status === 500) {
    console.log(res.error);
  }
  const check: never = res;
  return check;
}

/** Example 2: Stepwise typeof */
function process(value: string | number | boolean) {
  if (typeof value === "string") {
    return value.toUpperCase();
  } else if (typeof value === "number") {
    return value * 2;
  }
  return !value;
}

/** Example 3: Using the in operator */
type ApiResult =
  | { ok: true; data: string }
  | { ok: false; error: string };

function narrowLog(result: ApiResult) {
  if ("data" in result) {
    console.log(result.data);
  } else if ("error" in result) {
    console.error(result.error);
  } else {
    const check: never = result;
    throw new Error(`Unhandled: ${check}`);
  }
}
```
