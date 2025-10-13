# #787 「obj[symbol] = value」

四国めたん「シンボルキーはブラケット記法で代入します。」
ずんだもん「obj[token] = valueみたいに書けばいいんだね。」
四国めたん「はい、点記法は使えないので必ず[]でアクセスします。」
ずんだもん「Object.definePropertyを使うと属性も指定できるよ。」
四国めたん「TypeScriptではRecord<symbol, T>よりもMapを使う方が型付けしやすい場合もあります。」
ずんだもん「代入パターンを覚えてメタデータを安全に持たせよう！」
四国めたん「オブジェクト拡張時に役立つテクニックです。」
ずんだもん「記法を押さえてシンボル活用を進めよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: ブラケット代入 */
const STATE = Symbol("state");
const machine: Record<string, unknown> = {};
machine[STATE] = { status: "idle" };

/** Example 2: defineProperty */
const store: Record<string | symbol, unknown> = {};
Object.defineProperty(store, STATE, {
  value: { status: "idle" },
  writable: true,
  enumerable: false,
});

/** Example 3: 更新 */
machine[STATE] = { status: "running" };
```
