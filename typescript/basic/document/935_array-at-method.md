# #935 「atメソッド」

四国めたん「配列のatメソッドを使うと安全に要素を取得できます。」
ずんだもん「arr.at(0)って書くやつだね。」
四国めたん「範囲外の場合はundefinedを返しますし、負のインデックスも対応しています。」
ずんだもん「TypeScriptでは戻り値がT | undefinedになるからガードが書きやすいよ。」
四国めたん「ES2022以降のランタイムで使えるメソッドです。」
ずんだもん「atメソッドで安全なアクセスを覚えてね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 基本 */
const data = ["a", "b", "c"];
const first = data.at(0); // string | undefined

/** Example 2: 範囲外 */
const missing = data.at(10); // undefined

/** Example 3: 負のインデックス */
const last = data.at(-1); // "c"
```
