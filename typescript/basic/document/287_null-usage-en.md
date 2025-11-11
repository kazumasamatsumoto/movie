# #287 "When to use null"

四国めたん「Today let's learn about when to use null!」
ずんだもん「null is used to express an explicit empty value.」
四国めたん「It's useful in function return values to indicate "not found".」
ずんだもん「On the other hand, undefined is used for optional values.」
四国めたん「The difference in JSON compatibility is also an important point.」
ずんだもん「Use them appropriately to make your intentions clear!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: null - Explicit empty value */
let currentUser: User | null = null;
function findById(id: number): User | null {
  return null;
}
```

```typescript
/** Example 2: undefined - Optional */
interface Config {
  timeout?: number;  // number | undefined
}
function process(data?: string) {}
```

```typescript
/** Example 3: JSON compatibility differences */
JSON.stringify({ value: null });      // {"value":null}
JSON.stringify({ value: undefined }); // {}
```
