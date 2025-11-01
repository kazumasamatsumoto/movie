# #737 「Symbol()とSymbol()の比較」

四国めたん「Symbol()で生成した値は毎回別物なので===は必ずfalseです。」
ずんだもん「Object.isで比べても同じ結果になるんだよね。」
四国めたん「同じ変数を参照するときだけtrueになります。」
ずんだもん「Symbol.forを使うと共有プール経由でtrueになるケースがあるよ。」
四国めたん「比較検証で挙動を理解しておくとデバッグが楽です。」
ずんだもん「一意なトークンを使い回す場合は変数を保持してね。」
四国めたん「値を落とすと二度と同じSymbolは作れません。」
ずんだもん「挙動を把握して安全に比較しよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: === は false */
const a = Symbol("id");
const b = Symbol("id");
console.log(a === b); // false

/** Example 2: 同じ参照なら true */
const c = a;
console.log(c === a); // true

/** Example 3: Symbol.for は共有 */
const poolA = Symbol.for("shared");
const poolB = Symbol.for("shared");
console.log(poolA === poolB); // true
```
