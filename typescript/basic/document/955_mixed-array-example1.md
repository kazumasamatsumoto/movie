# #955 「実例(1)」

四国めたん「混合型配列を使ったログ解析の例を見てみましょう。」
ずんだもん「ログの内容がstring、タイムスタンプがnumberになっているケースだね。」
四国めたん「filterで文字列だけ抽出したり、numberだけ加算する処理を書いてみます。」
ずんだもん「型ガードで安全に扱えるのがポイントだよ。」
四国めたん「実例を通してUnion配列操作の感覚を掴んでください。」
ずんだもん「現場でもよくある形だよ！」

---

## 📺 画面表示用コード

```typescript
const logStream: (string | number)[] = ["start", 1680000000000, "finish", 1680000005000];

/** Example 1: 文字列のみ */
const messages = logStream.filter((entry): entry is string => typeof entry === "string");

/** Example 2: タイムスタンプ合計 */
const totalTime = logStream
  .filter((entry): entry is number => typeof entry === "number")
  .reduce((acc, cur) => acc + cur, 0);

/** Example 3: 正規化 */
const normalized = logStream.map((entry) => entry.toString());
```
