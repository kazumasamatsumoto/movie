# #889 「ベストプラクティス」

四国めたん「BigIntの制約を踏まえたベストプラクティスを整理します。」
ずんだもん「変換・シリアライズ・演算を共通ユーティリティにまとめるんだったね。」
四国めたん「はい、制約に触れる処理は一箇所に集約しましょう。」
ずんだもん「Math関数を使いたい場合はラッパー関数を用意しておくと安心だよ。」
四国めたん「パフォーマンスやメモリは計測し、必要ならnumberとのハイブリッド戦略を採用します。」
ずんだもん「ベストプラクティスを守ることで制約を怖がらずに済むね。」
四国めたん「ドキュメントとテストで制約対策を明文化しましょう。」
ずんだもん「BigInt運用の指針として活用してね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 共通ユーティリティ */
export const BigIntUtil = {
  toString: (value: bigint) => value.toString(),
  fromString: (value: string) => BigInt(value),
};

/** Example 2: ラッパー */
import { sqrt as bigintSqrt } from "bigint-isqrt";
export const MathBigInt = {
  sqrt: bigintSqrt,
};

/** Example 3: ハイブリッド処理 */
function compute(value: number | bigint) {
  return typeof value === "bigint" ? value : BigInt(Math.round(value));
}
```
