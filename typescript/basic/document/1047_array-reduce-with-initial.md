# #1047 「初期値あり - U型」

四国めたん「初期値を渡したreduceはアキュムレータ型Uを自由に設定できます。」
ずんだもん「配列から別の型に変換したいときに便利なんだね。」
四国めたん「初期値とコールバックの戻り値を揃えてU型の結果を得ます。」
ずんだもん「空配列にも安全に対応できるよ。」
四国めたん「初期値ありのパターンを積極的に使ってください。」
ずんだもん「柔軟な集約ができるね！」

---

## 📺 画面表示用コード

```typescript
const values = ["meta", "zunda"];

/** Example 1: Set */
const set = values.reduce<Set<string>>((acc, cur) => acc.add(cur), new Set());

/** Example 2: Map */
const map = values.reduce<Map<string, number>>((acc, cur, index) => acc.set(cur, index), new Map());

/** Example 3: カスタム型 */
const grouped = values.reduce<Record<string, number>>((acc, cur) => {
  acc[cur] = (acc[cur] ?? 0) + 1;
  return acc;
}, {});
```
