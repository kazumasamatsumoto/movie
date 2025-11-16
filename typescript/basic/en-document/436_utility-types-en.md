# #436 "Utility Types"

Shikoku Metan: "Utility types can help when working with void."
Zundamon: "ReturnType<typeof log> evaluated to void."
Shikoku Metan: "Combine it with Parameters to define variadic void functions."
Zundamon: "We also built an EventMap using Record<string, () => void>."
Shikoku Metan: "Utility types automate these conversions nicely."
Zundamon: "I'll memorize these void-centric utilities!"

---

## 📺 Code for Display

```typescript
/** Example 1: ReturnType extracting void */

function log(msg: string): void {
  console.log(msg);
}
type LogReturn = ReturnType<typeof log>;

/** Example 2: Parameters combo */

type VoidFunction<T extends any[]> = (...args: T) => void;
type Handler = VoidFunction<[string, number]>;

/** Example 3: Record */

type EventMap = Record<string, () => void>;
const events: EventMap = {
  click: () => console.log("Click"),
  hover: () => console.log("Hover"),
};
```
