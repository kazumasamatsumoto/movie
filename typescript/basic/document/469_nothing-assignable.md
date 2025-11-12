# #469 「何も代入できない」

四国めたん「neverには何も代入できないことを確認しましょう。」
ずんだもん「value: never には0もundefinedも入れられなかった!」
四国めたん「ただしneverを返す関数の結果だけは代入できます。」
ずんだもん「fail()の戻り値をconst result: neverに入れる例があったね。」
四国めたん「exhaustiveチェックではnever変数で到達不可能を表します。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 代入不可 */
let value: never;

/** Example 2: never関数から代入 */
function fail(): never {
  throw new Error("Failed");
}
const result: never = fail();

/** Example 3: 型の絞り込み */
function check(value: string | number): string {
  if (typeof value === "string") {
    return value;
  } else if (typeof value === "number") {
    return value.toString();
  }
  const exhaustive: never = value;
  return exhaustive;
}
```
