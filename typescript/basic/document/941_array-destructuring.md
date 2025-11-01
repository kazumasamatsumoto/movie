# #941 「分割代入」

四国めたん「配列は分割代入で要素を取り出せます。」
ずんだもん「const [first, second] = values; って書くやつだね。」
四国めたん「不要な要素はカンマでスキップすることもできます。」
ずんだもん「restパターンで残りの要素をまとめて受け取るのも便利だよ。」
四国めたん「分割代入は可読性が高く、型推論も効きます。」
ずんだもん「配列操作で積極的に使ってね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 基本 */
const values = ["meta", "zunda"];
const [mentor, developer] = values;

/** Example 2: スキップ */
const [, second] = [10, 20, 30];

/** Example 3: rest */
const [head, ...tail] = [1, 2, 3, 4];
```
