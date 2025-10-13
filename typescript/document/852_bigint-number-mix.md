# #852 「numberとの混在 - エラー」

四国めたん「bigintとnumberを直接演算するとTypeErrorになります。」
ずんだもん「1n + 1みたいな式はエラーになるんだね。」
四国めたん「はい、型を揃えるかNumber()/BigInt()で変換してから計算しましょう。」
ずんだもん「TypeScriptもコンパイル時に警告してくれるよ。」
四国めたん「暗黙変換がないことで精度の意図を明確にできます。」
ずんだもん「混在エラーを活かして安全性を高めよう！」
四国めたん「チームでもルール化して事故を防ぎましょう。」
ずんだもん「bigintとnumberの境界を大事にしてね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 実行時エラー */
try {
  // @ts-expect-error bigintとnumberの混在
  console.log(1n + 1);
} catch (error) {
  console.error("TypeError", error);
}

/** Example 2: 変換して演算 */
const safeSum = BigInt(1) + 1n;

/** Example 3: ユーティリティ */
function addMixed(a: number | bigint, b: number | bigint): number | bigint {
  if (typeof a === "bigint" && typeof b === "bigint") return a + b;
  return Number(a) + Number(b);
}
```
