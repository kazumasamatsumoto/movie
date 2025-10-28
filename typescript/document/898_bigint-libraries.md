# #898 「ライブラリ」

四国めたん「BigInt対応のライブラリを紹介しましょう。」
ずんだもん「bigint-isqrt、bigint-crypto-utils、ethers.jsのBigNumber互換などがあるね。」
四国めたん「用途ごとに最適なライブラリを選択します。」
ずんだもん「TypeScript型定義が整っているかもチェックしよう。」
四国めたん「暗号、数学、固定小数点などジャンルごとに揃っています。」
ずんだもん「ライブラリ活用でBigInt開発を加速しよう！」
四国めたん「依存を増やしすぎないようにレビューも忘れずに。」
ずんだもん「適材適所で採用してね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: bigint-isqrt */
import { sqrt as bigintSqrt } from "bigint-isqrt";
const root = bigintSqrt(123456789n);

/** Example 2: bigint-crypto-utils */
import { modPow } from "bigint-crypto-utils";
const pow = modPow(2n, 1024n, 97n);

/** Example 3: ethers.js BigNumber */
import { BigNumber } from "ethers";
const bigNumber = BigNumber.from("12345678901234567890");
const asBigint = BigInt(bigNumber.toString());
```
