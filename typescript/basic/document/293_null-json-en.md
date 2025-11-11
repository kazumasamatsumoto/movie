# #293 "Null in JSON"

Shikoku Metan「Let's learn about null in JSON representation!」
Zundamon「How is null handled in JSON?」
Shikoku Metan「Yes. null is supported in the JSON specification, so it can be represented as is.」
Zundamon「What's the difference from undefined?」
Shikoku Metan「It's an important difference. undefined is omitted in JSON, but null remains.」
Zundamon「We use them differently in API response type definitions!」
Shikoku Metan「Exactly. Use null when JSON compatibility is needed.」
Zundamon「It can be properly handled with JSON.stringify and JSON.parse!」

---

## 📺 Code for Display

```typescript
/** Example 1: null in JSON */
JSON.stringify({ value: null });
// → '{"value":null}'
JSON.stringify({ a: null, b: undefined });
// → '{"a":null}'

/** Example 2: API response type definition */
interface ApiResponse {
  user: User | null;  // JSON compatible
  metadata?: object;  // Optional
}

/** Example 3: JSON parsing */
const data = JSON.parse('{"name":null}');
// → { name: null }
```
