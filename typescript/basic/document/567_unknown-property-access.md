# #567 「unknownはプロパティアクセス不可」

四国めたん「unknownではプロパティアクセスがそのままでは許されません」
ずんだもん「value.idとか書くと即エラーだね」
四国めたん「はい。typeofやin演算子で安全性を確認してからアクセスします」
ずんだもん「ガードを共通関数化すると重複も減らせるよ」
四国めたん「アクセス前に安全性を証明するのが開発者の役割です」
ずんだもん「チェックを怠らない仕組みを作っておこう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 直接アクセスはエラー */
const obj: unknown = { id: 1 };
// obj.id; // ❌

/** Example 2: in演算子でチェック */
if (typeof obj === "object" && obj !== null && "id" in obj) {
  const id = (obj as { id: number }).id;
  console.log(id);
}

/** Example 3: 型ガード関数 */
function hasName(value: unknown): value is { name: string } {
  return typeof value === "object" && value !== null && "name" in value;
}
```
