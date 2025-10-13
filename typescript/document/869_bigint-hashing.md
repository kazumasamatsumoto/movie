# #869 「ハッシュ化」

四国めたん「bigintをハッシュキーに使う場合は文字列化するのが一般的です。」
ずんだもん「MapやSetのキーにそのままbigintを使うこともできるよね。」
四国めたん「はい、JavaScriptのMapは同じBigInt値を同一扱いします。」
ずんだもん「ハッシュ関数に渡すときはエンディアンや桁数に注意しよう。」
四国めたん「crypto.createHashへ渡すときはバイト列に変換します。」
ずんだもん「BigIntのハッシュ化を正しく設計してね！」
四国めたん「識別子として使う場合は一貫したフォーマットに揃えましょう。」
ずんだもん「ハッシュ運用でBigIntを活かそう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Mapキー */
const cache = new Map<bigint, string>();
cache.set(123n, "value");

/** Example 2: 文字列化 */
const key = 1234567890n.toString();

/** Example 3: Node.jsのハッシュ */
import { createHash } from "crypto";
function hashBigint(value: bigint): string {
  const hex = value.toString(16);
  return createHash("sha256").update(hex, "hex").digest("hex");
}
```
