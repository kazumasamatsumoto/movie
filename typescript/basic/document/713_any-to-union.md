# #713 「Union型への置き換え」

四国めたん「値が複数パターンに限定されるならUnion型でanyを排除します」
ずんだもん「string | number | null みたいに列挙できるんだね」
四国めたん「はい。判別ユニオンを使えば安全な分岐が可能です」
ずんだもん「ユースケースを洗い出して具体的なUnionを定義しよう」
四国めたん「Union化は補完と型チェックの両方を改善します」
ずんだもん「anyから精度の高いUnionにアップグレードしよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Union化 */
type Payload = string | number | null;

/** Example 2: 判別ユニオン */
type Result =
  | { status: "success"; data: string }
  | { status: "error"; message: string };

/** Example 3: 分岐 */
function handle(result: Result) {
  if (result.status === "success") return result.data.toUpperCase();
  return `Error: ${result.message}`;
}
```
