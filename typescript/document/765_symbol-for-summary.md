# #765 「グローバルシンボルまとめ」

四国めたん「Symbol.forはグローバルに共有できるシンボルを返すAPIでしたね。」
ずんだもん「同じキーなら同じ値が返るからモジュール間通信に使えるんだった。」
四国めたん「キーは文字列一つ、命名規約で衝突を避けましょう。」
ずんだもん「Symbol.keyForで逆引きもできたよ。」
四国めたん「注意点はレジストリから削除できないことです。」
ずんだもん「用途を理解してSymbol()と使い分けよう。」
四国めたん「次はWell-known Symbolsを見ていきます。」
ずんだもん「グローバルシンボルを押さえたら準備万端だね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: グローバルキーの作成 */
const KEY = Symbol.for("myapp:shared");

/** Example 2: 値の共有 */
(globalThis as any)[KEY] = { featureEnabled: true };

/** Example 3: 再取得 */
const keyAgain = Symbol.for("myapp:shared");
console.log((globalThis as any)[keyAgain]);
```
