# #590 「Array.isArray()ガード」

四国めたん「Array.isArray()でunknownが配列かどうかを判定できます」
ずんだもん「typeofだとオブジェクト扱いになるから必須だね」
四国めたん「はい。要素の型チェックと組み合わせれば完全に絞れます」
ずんだもん「配列だったらmapやfilterが安心して使えるよ」
四国めたん「配列境界はArray.isArray()から始めましょう」
ずんだもん「データ整形の安全性が跳ね上がるね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 配列確認 */
function normalizeList(value: unknown) {
  if (Array.isArray(value)) {
    return value.length;
  }
  return 0;
}

/** Example 2: 要素チェック */
const isStringArray = (value: unknown): value is string[] =>
  Array.isArray(value) && value.every((item) => typeof item === "string");

/** Example 3: 使用例 */
const data: unknown = ["a", "b"];
if (isStringArray(data)) console.log(data.map((v) => v.toUpperCase()));
```
