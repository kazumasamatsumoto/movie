# #289 "Nullish coalescing operator - ??"

四国めたん「Today let's learn about the nullish coalescing operator!」
ずんだもん「The ?? operator returns the default value only when null or undefined.」
四国めたん「Unlike the || operator, 0 and empty strings are treated as valid values.」
ずんだもん「The key difference is how falsy values are handled.」
四国めたん「The ??= assignment operator is also useful.」
ずんだもん「Combine it with optional chaining to write safe code!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Nullish Coalescing */
const name = userName ?? "Guest";
const port = config.port ?? 3000;
```

```typescript
/** Example 2: Difference from || operator */
const count1 = 0 || 10;  // 10 (0 is falsy)
const count2 = 0 ?? 10;  // 0  (0 is not null)
```

```typescript
/** Example 3: ??= assignment operator and optional chaining */
config.timeout ??= 5000;
const zip = user?.address?.zipCode ?? "N/A";
```
