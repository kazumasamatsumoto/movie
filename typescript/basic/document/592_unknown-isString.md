# #592 「isString型ガード」

四国めたん「isStringのような型ガード関数でunknownを文字列に絞れます」
ずんだもん「戻り値にx is stringって書くやつだね」
四国めたん「はい。条件式で再利用すれば読みやすさも向上します」
ずんだもん「配列フィルタでも活躍するよ」
四国めたん「小さなガードを積み上げて安全なドメインを作りましょう」
ずんだもん「文字列処理がグッと扱いやすくなるね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: isString定義 */
function isString(value: unknown): value is string {
  return typeof value === "string";
}

/** Example 2: 条件分岐 */
function shout(value: unknown) {
  if (isString(value)) {
    console.log(value.toUpperCase());
  }
}

/** Example 3: フィルタ */
const values: unknown[] = ["a", 1, "b"];
const onlyStrings = values.filter(isString);
```
