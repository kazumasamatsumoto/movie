# #1068 「ベストプラクティス」

四国めたん「find系メソッドを使うときのベストプラクティスを整理します。」
ずんだもん「戻り値がundefinedになりうることへの対処、条件を関数化する、findLastはランタイムチェック、だったね。」
四国めたん「はい、単一取得ならfind、複数ならfilterを選びます。」
ずんだん「結果をそのまま使う前に必ず存在確認をしよう。」
四国めたん「ベストプラクティスを守って堅牢な検索処理を書いてください。」
ずんだもん「安全で読みやすいコードを目指そう！」

---

## 📺 画面表示用コード

```typescript
const values = ["meta", "zunda"];

/** Example 1: 存在チェック */
const found = values.find((value) => value === "meta");
if (!found) throw new Error("not found");

/** Example 2: 条件を関数化 */
const isZunda = (value: string) => value === "zunda";
const zunda = values.find(isZunda);

/** Example 3: find vs filter */
const first = values.find((value) => value.startsWith("m"));
const all = values.filter((value) => value.startsWith("m"));
```
