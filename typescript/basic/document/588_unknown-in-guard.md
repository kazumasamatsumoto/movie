# #588 「in型ガード」

四国めたん「in型ガードはunknownが特定のプロパティを持つか確認します」
ずんだもん「"id" in value みたいに書けるやつだね」
四国めたん「はい。オブジェクトの形を部分的に保障するのに便利です」
ずんだもん「optionalプロパティもチェックできるのが嬉しいよ」
四国めたん「プロパティ存在を証明してからアサーションで取り出しましょう」
ずんだもん「外部データを安全に扱う鉄板テクニックだね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: in演算子 */
function hasId(value: unknown): value is { id: number } {
  return typeof value === "object" && value !== null && "id" in value;
}

/** Example 2: optionalプロパティ */
function hasTitle(value: unknown): value is { title?: string } {
  return typeof value === "object" && value !== null && "title" in value;
}

/** Example 3: 使用例 */
const payload: unknown = { id: 1, title: "TS" };
if (hasId(payload)) console.log(payload.id);
```
