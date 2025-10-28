# #755 「Symbol.for("key")の挙動」

四国めたん「Symbol.for("key")は、既存のシンボルがあればそれを返し、なければ登録します。」
ずんだもん「キーは文字列に変換されるから、1でも"1"でも同じ扱いだよね。」
四国めたん「グローバルレジストリは文字列キー一本で管理されます。」
ずんだもん「初回呼び出しで登録され、次から同じ値が返るってことだね。」
四国めたん「Symbol.keyForを使うと逆引きもできます。」
ずんだもん「挙動を知っていればデバッグしやすくなるよ。」
四国めたん「キー命名を誤ると意図せず共有されるので注意しましょう。」
ずんだもん「挙動を理解して安全に活用しよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 初回登録と再取得 */
const firstCall = Symbol.for("shared");
const secondCall = Symbol.for("shared");
console.log(Object.is(firstCall, secondCall)); // true

/** Example 2: 引数は文字列キー */
const numericKey = Symbol.for(String(1));
const explicitKey = Symbol.for(\"1\");
console.log(numericKey === explicitKey); // true: どちらも\"1\"として登録

/** Example 3: Symbol.keyForで逆引き */
const key = Symbol.keyFor(firstCall);
console.log(key); // "shared"
```
