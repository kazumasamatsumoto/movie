# #960 「混合型配列まとめ」

四国めたん「混合型配列のポイントをまとめましょう。」
ずんだもん「Union型で宣言、型ガードで絞り込み、filterやmapで整形、だったね。」
四国めたん「はい、タプルとの使い分けやパターン集も確認しました。」
ずんだもん「混在するデータを安全に扱うテクニックが揃ったよ。」
四国めたん「次は配列型とUnion型の違いをさらに掘り下げます。」
ずんだもん「混合型配列を味方にしよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 宣言 */
const tokens: (string | number)[] = ["ok", 200];

/** Example 2: 型ガード */
const onlyNumbers = tokens.filter((token): token is number => typeof token === "number");

/** Example 3: 正規化 */
const normalized = tokens.map(String);
```
