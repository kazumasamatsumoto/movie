# #1040 「filterまとめ」

四国めたん「filterのポイントをまとめましょう。」
ずんだもん「真偽値か型述語で絞り込み、戻り値の型はT[]、型述語ならU[]になるんだったね。」
四国めたん「null除去やUnion配列の分割に大活躍でした。」
ずんだもん「ベストプラクティスを守れば安全な絞り込みができるよ。」
四国めたん「次はreduceを詳しく見ていきます。」
ずんだもん「filterを使いこなしてデータを整えよう！」

---

## 📺 画面表示用コード

```typescript
const tokens: (string | number | undefined)[] = ["ok", 200, undefined];

/** Example 1: 真偽値 */
const truthy = tokens.filter(Boolean);

/** Example 2: 型述語 */
const strings = tokens.filter((token): token is string => typeof token === "string");

/** Example 3: チェーン */
const normalized = tokens
  .filter((token): token is number => typeof token === "number")
  .map((token) => token * 2);
```
