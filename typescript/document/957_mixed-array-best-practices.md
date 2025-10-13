# #957 「ベストプラクティス」

四国めたん「混合型配列を使うときのベストプラクティスを整理しましょう。」
ずんだもん「Unionを明示する、型ガードを用意する、filterやmapで型を絞る、だったね。」
四国めたん「はい、頻出の判定ロジックは関数に切り出して再利用します。」
ずんだもん「用途によってはタプルやオブジェクト配列に置き換える選択肢もあるよ。」
四国めたん「混在に伴うリスクを理解しつつ可読性を保ちましょう。」
ずんだもん「ベストプラクティスで安全な混合配列を！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 型エイリアス */
type Token = string | number;
const tokens: Token[] = [];

/** Example 2: 型ガード */
const isStringToken = (value: Token): value is string => typeof value === "string";

/** Example 3: ユーティリティ */
function partitionTokens(values: Token[]) {
  return {
    strings: values.filter(isStringToken),
    numbers: values.filter((value): value is number => typeof value === "number"),
  };
}
```
