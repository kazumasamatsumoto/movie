# #949 「要素アクセス」

四国めたん「混合型配列の要素にアクセスするとUnion型が返ります。」
ずんだもん「tokens[0]がstring | numberになる感じだね。」
四国めたん「特定の型に絞るには型ガードが必要です。」
ずんだもん「typeofで判定すれば安全に扱えるよ。」
四国めたん「アクセスのあとにガードを入れる習慣をつけましょう。」
ずんだもん「混合型でも型安全に扱ってね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Union戻り値 */
const tokens: (string | number)[] = ["GET", 200];
const first = tokens[0]; // string | number

/** Example 2: typeofチェック */
if (typeof first === "string") {
  console.log(first.toUpperCase());
}

/** Example 3: 関数 */
function head<T>(values: T[]): T | undefined {
  return values[0];
}
```
