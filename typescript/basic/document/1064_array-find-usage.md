# #1064 「使い分け」

四国めたん「find、findIndex、findLast、findLastIndexの使い分けを整理しましょう。」
ずんだもん「値が欲しいならfind/findLast、インデックスが欲しいならfindIndex/findLastIndexだね。」
四国めたん「検索方向も前方か後方かで選びます。」
ずんだもん「結果が見つからないときの戻り値も確認しておこう。」
四国めたん「目的に応じて最適なメソッドを選択してください。」
ずんだもん「検索ニーズに合わせて使い分けよう！」

---

## 📺 画面表示用コード

```typescript
const entries = ["meta", "zunda", "meta"];

const firstMeta = entries.find((value) => value === "meta");
const lastMeta = entries.findLast?.((value) => value === "meta");

const firstMetaIndex = entries.findIndex((value) => value === "meta");
const lastMetaIndex = entries.findLastIndex?.((value) => value === "meta");
```
