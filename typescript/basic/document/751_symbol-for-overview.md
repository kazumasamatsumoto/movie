# #751 「Symbol.for()とは」

四国めたん「Symbol.forはグローバルシンボルレジストリを使うAPIです。」
ずんだもん「同じキーで呼ぶと同じシンボルが返るんだよね。」
四国めたん「アプリ全体で共有したい識別子に向いています。」
ずんだもん「DIトークンをライブラリ間で共通化するときに便利だよ。」
四国めたん「Symbol()と違って再取得が可能なのが特徴です。」
ずんだもん「共有前提のときに使い分けたいね。」
四国めたん「グローバルなので名前の付け方には注意が必要です。」
ずんだもん「Symbol.forで安全に共有しよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: グローバルレジストリから取得 */
const tokenA = Symbol.for("shared-token");
const tokenB = Symbol.for("shared-token");
console.log(tokenA === tokenB); // true

/** Example 2: 新規キーは自動登録 */
const initial = Symbol.for("first-call");
console.log(typeof initial); // "symbol"

/** Example 3: 通常のSymbolとの比較 */
const local = Symbol("first-call");
console.log(local === Symbol.for("first-call")); // false
```
