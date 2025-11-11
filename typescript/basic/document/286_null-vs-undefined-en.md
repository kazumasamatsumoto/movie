# #286 "Differences between null and undefined"

四国めたん「Today let's learn about the differences between null and undefined!」
ずんだもん「Both represent the absence of a value, but their meanings differ.」
四国めたん「null is an explicit empty value, undefined is an uninitialized state.」
ずんだもん「The typeof operator also gives different results for each.」
四国めたん「Understanding when to use optional properties versus null is important.」
ずんだもん「With the Nullish Coalescing operator, both are treated the same!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Basic differences */
let a: null = null;          // Explicit empty
let b: undefined = undefined; // Uninitialized
typeof null;      // "object"
typeof undefined; // "undefined"
```

```typescript
/** Example 2: Optional vs null usage */
interface User {
  name?: string;        // string | undefined
  email: string | null; // Explicit null
}
```

```typescript
/** Example 3: Nullish Coalescing */
const value1 = null ?? "default";      // "default"
const value2 = undefined ?? "default"; // "default"
```
