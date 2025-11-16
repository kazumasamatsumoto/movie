# #507 "Unreachable Code Detection"

Shikoku Metan: "The never type also reveals unreachable code."
Zundamon: "In process(), the final else should never run once string and number are handled."
Shikoku Metan: "Referencing value there turns it into never and surfaces a warning."
Zundamon: "handle() only accepts success or error, so console.log(status) becomes unreachable."
Shikoku Metan: "Editors even gray that branch out for us."
Zundamon: "neverReturn() that always throws is treated the same way."
Shikoku Metan: "Any console.log('unreachable') after it triggers an error."
Zundamon: "Lean on never to prune dead code early."

---

## 📺 Code for Display

```typescript
/** Example 1: Else after type guards */
function process(value: string | number) {
  if (typeof value === "string") return value.toUpperCase();
  else if (typeof value === "number") return value * 2;
  else {
    value; // never
    return 0; // unreachable
  }
}

/** Example 2: Remaining union states */
type Status = "success" | "error";

function handle(status: Status) {
  if (status === "success") return "OK";
  if (status === "error") return "NG";
  console.log(status); // unreachable
}

/** Example 3: Functions that never return */
function neverReturn(): never {
  throw new Error("Error");
}

function example() {
  neverReturn();
  console.log("Unreachable");
}
```
