# #1035 「NonNullable型」

四国めたん「NonNullable型を使うとnull/undefined除去が明確になります。」
ずんだもん「NonNullable<T>でTからnullとundefinedを取り除けるんだね。」
四国めたん「はい、filterの型述語と組み合わせると型がきれいに絞り込まれます。」
ずんだもん「ユーティリティ型を覚えておくと便利だよ。」
四国めたん「NonNullableの使い方を確認しましょう。」
ずんだもん「コードの意図が明確になるね！」

---

## 📺 画面表示用コード

```typescript
const values = [1, undefined, 3, null];

type NonNullNumber = NonNullable<typeof values[number]>; // number

/** Example 1: 型述語 */
const nonNull = values.filter((value): value is NonNullNumber => value != null);

/** Example 2: ユーティリティ関数 */
const isNonNullable = <T>(value: T): value is NonNullable<T> => value != null;
const filtered = values.filter(isNonNullable);

/** Example 3: mapとの組み合わせ */
const squared = values.filter(isNonNullable).map((value) => value * value);
```
