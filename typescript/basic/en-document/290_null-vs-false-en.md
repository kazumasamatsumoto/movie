# #290 "Differences between null and false"

四国めたん「Today let's learn about the differences between null and false!」
ずんだもん「null is null type, false is boolean type - they're completely different types.」
四国めたん「When compared with the strict equality operator, the result is always false.」
ずんだもん「They're also handled differently in Nullish Coalescing.」
四国めたん「null represents an empty value, while false represents logical falsity.」
ずんだもん「Understand the type system and use them correctly!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Type differences */
let a: null = null;     // null type
let b: boolean = false; // boolean type
null === false;  // false
```

```typescript
/** Example 2: Nullish Coalescing behavior */
const v1 = null ?? "default";  // "default"
const v2 = false ?? "default"; // false
```

```typescript
/** Example 3: Type safety */
let flag: boolean = null;  // Error
let flag: boolean | null = null;  // OK
```
