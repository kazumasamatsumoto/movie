# #414 "Compile Output"

Shikoku Metan: "TypeScript's void/undefined annotations vanish at compile time."
Zundamon: "f1(): void turns into plain function f1() in JavaScript."
Shikoku Metan: "Yes, all type metadata is removed."
Zundamon: "f2(): undefined just keeps return undefined;?"
Shikoku Metan: "Exactly—the runtime follows JavaScript semantics."
Zundamon: "Even the comments illustrated that transformation."
Shikoku Metan: "Understanding the emitted code simplifies debugging."
Zundamon: "I'll treat types as design info only!"

---

## 📺 Code for Display

```typescript
/** Example 1: TypeScript */
function f1(): void {
  console.log("void");
}
function f2(): undefined {
  return undefined;
}

/** Example 2: JavaScript */
function f1() {
  console.log("void");
}
function f2() {
  return undefined;
}

/** Example 3: Types are erased */
// TypeScript: function log(msg: string): void
// JavaScript: function log(msg)
```
