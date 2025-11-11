# #288 "Null checking"

四国めたん「Today let's learn about null checking methods!」
ずんだもん「You can safely check with the strict equality operator.」
四国めたん「Using type guards, TypeScript will narrow the type for you.」
ずんだもん「Optional chaining lets you safely access deep properties.」
四国めたん「The Nullish Coalescing operator can set default values.」
ずんだもん「Combine these techniques to write robust code!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Strict equality operator and type guard */
if (user === null) {
  console.log("User is null");
}
function isNotNull<T>(value: T | null): value is T {
  return value !== null;
}
```

```typescript
/** Example 2: Optional chaining */
const name = user?.name;
const zip = user?.address?.zipCode;
```

```typescript
/** Example 3: Nullish Coalescing */
const displayName = user ?? "Guest";
const port = config.port ?? 3000;
```
