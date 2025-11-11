# #307 "JSON Representation of undefined"

Shikoku Metan: "Let's learn about the JSON representation of undefined!"
Zundamon: "In JSON, undefined properties are completely omitted!"
Shikoku Metan: "That's right. null remains as '{"value":null}', but undefined disappears."
Zundamon: "undefined in arrays is special - it gets converted to null, right?"
Shikoku Metan: "Exactly. In arrays, it's treated as null to preserve the position."
Zundamon: "When optional properties are omitted, they're not included in JSON either!"
Shikoku Metan: "Understanding JSON.stringify behavior helps prevent issues during data transmission."
Zundamon: "The difference between undefined and null becomes clear through JSON conversion!"

---

## 📺 Code for Display

```typescript
/** Example 1: JSON representation of undefined */
JSON.stringify({ value: undefined });
// → '{}'  (undefined is omitted)
JSON.stringify({ value: null });
// → '{"value":null}'

/** Example 2: undefined in arrays */
JSON.stringify([1, undefined, 3]);
// → '[1,null,3]'  (converted to null in arrays)

/** Example 3: Optional properties */
interface User {
  name: string;
  age?: number;  // can be undefined
}
JSON.stringify({ name: "Alice" });
// → '{"name":"Alice"}'
```
