# #993 「型安全性」

四国めたん「ループ処理でも型安全性を意識しましょう。」
ずんだもん「要素型を絞り込んだり、undefinedを防いだりするんだね。」
四国めたん「制御フロー解析を活用して安全に処理を書きます。」
ずんだもん「Promiseや非同期処理でも戻り値の型を意識しよう。」
四国めたん「型安全性を守ることでバグを抑制できます。」
ずんだもん「安全第一でループを書いてね！」

---

## 📺 画面表示用コード

```typescript
const payload: (string | number | undefined)[] = ["ok", undefined, 200];

/** Example 1: ガード */
for (const value of payload) {
  if (value === undefined) continue;
  console.log(value.toString());
}

/** Example 2: 型述語 */
const isString = (value: string | number | undefined): value is string => typeof value === "string";
const strings = payload.filter(isString); // string[]

/** Example 3: 非同期 */
async function processAll(items: string[]) {
  for (const item of items) {
    await fetch(`/api/${item}`);
  }
}
```
