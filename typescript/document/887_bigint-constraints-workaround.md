# #887 「制約の回避方法」

四国めたん「BigIntの制約を回避するテクニックをまとめましょう。」
ずんだもん「Math関数が使えないときは独自実装、JSONは文字列化、性能はアルゴリズム改善だったね。」
四国めたん「はい、必要に応じてdecimalライブラリとの併用も検討します。」
ずんだもん「小数が必要なら固定小数点戦略を採用するといいよ。」
四国めたん「変換とシリアライズを共通化すると制約に振り回されません。」
ずんだもん「回避策をセットで覚えてBigIntを安心して使おう！」
四国めたん「ドキュメントに制約と回避策を記載しておきましょう。」
ずんだもん「問題を先回りして解決しようね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: sqrt代替 */
import { sqrt as bigintSqrt } from "bigint-isqrt";

/** Example 2: 固定小数点 */
const CENT = 100n;
function toFixed(amount: number) {
  return BigInt(Math.round(amount * Number(CENT)));
}

/** Example 3: 変換ユーティリティ */
export const BigIntTransport = {
  serialize: (value: bigint) => value.toString(),
  deserialize: (value: string) => BigInt(value),
};
```
