# #733 「ユニーク性保証」

四国めたん「Symbolは生成のたびに固有値が作られるため衝突しません。」
ずんだもん「説明文が同じでも別物になるのが嬉しいところだよ。」
四国めたん「ハッシュマップの内部キーやDIコンテナのトークンとして安全です。」
ずんだもん「Nest.jsのInjectトークンを自作するときもシンボルなら被らないね。」
四国めたん「等価比較で必ずfalseになる性質がユニーク性の証です。」
ずんだもん「開発チームが増えても名前がぶつからなくて助かるよ。」
四国めたん「環境を跨いだ識別子管理にも安心して使えます。」
ずんだもん「ユニーク性保証で型安全と設計の両方を守ろう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 説明文が同じでも別値 */
const tokenA = Symbol("service");
const tokenB = Symbol("service");
console.log(tokenA === tokenB); // false

/** Example 2: Mapでの衝突防止 */
const container = new Map<symbol, object>();
container.set(tokenA, { impl: "A" });
container.set(tokenB, { impl: "B" });
console.log(container.size); // 2 それぞれ独立

/** Example 3: シングルトンな識別子 */
const TOKENS = {
  LOGGER: Symbol("LOGGER"),
  CONFIG: Symbol("CONFIG"),
} as const;
console.log(TOKENS.LOGGER !== TOKENS.CONFIG); // true
```
