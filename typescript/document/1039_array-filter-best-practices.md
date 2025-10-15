# #1039 「ベストプラクティス」

四国めたん「filterを使うときのベストプラクティスも確認しておきましょう。」
ずんだもん「型述語で絞りこむ、副作用を避ける、null除去ならNonNullableを使う、だったね。」
四国めたん「はい、チェーンでは可読性と性能バランスを意識します。」
ずんだもん「ガード済みのユーティリティを再利用すると安全だよ。」
四国めたん「ベストプラクティスを守ってfilterを活用してください。」
ずんだもん「型安全な絞り込みを楽しもう！」

---

## 📺 画面表示用コード

```typescript
const values: (string | number | undefined)[] = ["a", undefined, "b", 1];

/** Example 1: 型述語ユーティリティ */
const isString = (value: unknown): value is string => typeof value === "string";
const strings = values.filter(isString);

/** Example 2: NonNullable */
const defined = values.filter((value): value is NonNullable<typeof value> => value != null);

/** Example 3: 関数抽出 */
function onlyNumbers(values: (string | number)[]) {
  return values.filter((value): value is number => typeof value === "number");
}
```
