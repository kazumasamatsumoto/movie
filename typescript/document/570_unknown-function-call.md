# #570 「unknownは関数呼び出し不可」

四国めたん「unknownを関数として呼び出すこともできません」
ずんだもん「value()って書くとコンパイルが怒るよね」
四国めたん「はい。関数かどうかをチェックするか型アサーションが必要です」
ずんだもん「typeof value === \"function\" で守るのが定番だよ」
四国めたん「コールシグネチャを保証してから実行しましょう」
ずんだもん「安全確認を標準化すればバグを封じ込められるね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 呼び出しはエラー */
const maybeFn: unknown = () => "ok";
// maybeFn(); // ❌

/** Example 2: 関数チェック */
if (typeof maybeFn === "function") {
  console.log(maybeFn());
}

/** Example 3: 型アサーション */
type Handler = () => string;
const forcedFn = maybeFn as Handler;
console.log(forcedFn());
```
