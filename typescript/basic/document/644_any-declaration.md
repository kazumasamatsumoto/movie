# #644 「any型の宣言方法」

四国めたん「any型は型注釈や型推論で宣言できます」
ずんだもん「let value: anyとか、型を省略してnoImplicitAnyが切れてる場合だね」
四国めたん「はい。ただし明示的にanyと書くときは用途をコメントで残しましょう」
ずんだもん「関数の引数や戻り値に使うと影響範囲が広がるよ」
四国めたん「宣言時点でリスクを意識し、後で置き換える前提を持つことが重要です」
ずんだもん「宣言の瞬間から型負債が始まるって覚えておこう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 明示的宣言 */
let temp: any; // TODO: replace with SpecificType

/** Example 2: 引数any */
function legacyHandler(event: any) {
  return event.payload;
}

/** Example 3: 暗黙的any（noImplicitAnyがfalseの場合） */
function sum(a, b) {
  return a + b; // a,bが暗黙any
}
```
