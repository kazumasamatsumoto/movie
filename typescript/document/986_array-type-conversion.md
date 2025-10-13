# #986 「型変換」

四国めたん「mapやfilterを使うと配列の型変換が行えます。」
ずんだもん「string[]をnumber[]にしたり、Union配列を絞り込んだりできるんだね。」
四国めたん「はい、型安全に変換するためには戻り値型を正しく設定しましょう。」
ずんだもん「状況によってはreduceで別のデータ構造に変換することもあるよ。」
四国めたん「型変換を意識して配列操作を設計してください。」
ずんだもん「変換処理の基本を押さえてね！」

---

## 📺 画面表示用コード

```typescript
const tags = ["1", "2", "3"];

/** Example 1: map */
const numbers = tags.map(Number); // number[]

/** Example 2: filterで絞り込み */
const mixed: (string | number)[] = ["ok", 200];
const onlyStrings = mixed.filter((item): item is string => typeof item === "string");

/** Example 3: reduce */
const lookup = mixed.reduce<Record<string, number>>((acc, item) => {
  if (typeof item === "string") acc[item] = item.length;
  return acc;
}, {});
```
