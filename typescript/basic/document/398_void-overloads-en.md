# #398 "Overloads"

Shikoku Metan: "Overloads can assign different return types per signature."
Zundamon: "process returns string for strings and void for numbers."
Shikoku Metan: "Right, the implementation returns string | void."
Zundamon: "log shows multiple parameter patterns that all return void?"
Shikoku Metan: "Yes, when we only print messages that's enough."
Zundamon: "The forEach overload example merely toggles the start argument."
Shikoku Metan: "Both overloads still return void, keeping usage simple."
Zundamon: "I'll design overloads with void strategically!"

---

## 📺 Code for Display

```typescript
/** Example 1: Overload returning void */
function process(data: string): string;
function process(data: number): void;
function process(data: string | number): string | void {
  if (typeof data === "string") return data.toUpperCase();
  console.log(data);
}

/** Example 2: Practical example */
function log(message: string): void;
function log(level: string, message: string): void;
function log(levelOrMsg: string, message?: string): void {
  if (message) {
    console.log(`[${levelOrMsg}] ${message}`);
  } else {
    console.log(levelOrMsg);
  }
}

/** Example 3: Callback overload */
function forEach(callback: (item: number) => void): void;
function forEach(start: number, callback: (item: number) => void): void;
function forEach(startOrCb: any, callback?: any): void {
  // Implementation
}
```
