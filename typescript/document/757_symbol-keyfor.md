# #757 「Symbol.keyFor()」

四国めたん「Symbol.keyForはグローバルシンボルのキーを逆引きできます。」
ずんだもん「Symbol.forで作った値にしか使えないんだよね。」
四国めたん「通常のSymbol()で生成した値はundefinedになります。」
ずんだもん「キーが取れるとデバッグやログに便利だよ。」
四国めたん「存在しないシンボルを渡した場合はnullではなくundefinedです。」
ずんだもん「挙動を知っていれば例外処理が書きやすいね。」
四国めたん「Symbol.keyForでグローバルレジストリを可視化できます。」
ずんだもん「活用してシンボル管理をしやすくしよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: キーの逆引き */
const shared = Symbol.for("shared:logger");
console.log(Symbol.keyFor(shared)); // "shared:logger"

/** Example 2: 通常のSymbolには使えない */
const local = Symbol("local");
console.log(Symbol.keyFor(local)); // undefined

/** Example 3: ログ出力ユーティリティ */
const describeSymbol = (value: symbol) => Symbol.keyFor(value) ?? value.description ?? \"<local>\";
console.log(describeSymbol(shared)); // \"shared:logger\"
console.log(describeSymbol(local)); // \"local\"
```
