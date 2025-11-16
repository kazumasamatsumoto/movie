# #311 "What is strictNullChecks"

Shikoku Metan「Let's learn about strictNullChecks!」
Zundamon「Is it an option that strictly checks null and undefined?」
Shikoku Metan「Yes. When disabled, all types include null and undefined, but when enabled, you need to specify them explicitly.」
Zundamon「With strictNullChecks: false, you can assign null to string type!」
Shikoku Metan「Exactly. But that's dangerous code that can cause runtime errors.」
Zundamon「When enabled, you need to write explicitly like string | null?」
Shikoku Metan「Yes. It can be configured in tsconfig.json and is included in strict: true.」
Zundamon「It's recommended to enable it to prevent null pointer exceptions!」

---

## 📺 Code for Display

```typescript
/** Example 1: strictNullChecks: false (disabled) */
let name: string = null; // OK (no error)
let age: number = undefined; // OK

/** Example 2: strictNullChecks: true (enabled) */
let name: string = null; // Error
let name: string | null = null; // OK

/** Example 3: Configure in tsconfig.json */
{
  "compilerOptions": {
    "strictNullChecks": true
  }
}
```
