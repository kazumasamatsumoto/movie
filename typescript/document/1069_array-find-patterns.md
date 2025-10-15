# #1069 「パターン集」

四国めたん「find系メソッドの代表的なパターンを整理します。」
ずんだもん「findで単一取得、findIndexで位置取得、findLastで末尾検索、findLastIndexで末尾インデックスだね。」
四国めたん「はい、条件を関数化して再利用すると便利です。」
ずんだもん「パターンをテンプレート化しておくと実装が速くなるよ。」
四国めたん「検索ニーズに合わせて適切なパターンを選択しましょう。」
ずんだん「使い分けをスムーズにしよう！」

---

## 📺 画面表示用コード

```typescript
const values = ["meta", "zunda", "meta"];

const isMeta = (value: string) => value === "meta";

const firstMeta = values.find(isMeta);
const firstMetaIndex = values.findIndex(isMeta);
const lastMeta = values.findLast?.(isMeta);
const lastMetaIndex = values.findLastIndex?.(isMeta);
```
