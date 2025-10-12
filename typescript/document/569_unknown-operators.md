# #569 「unknownは演算子利用不可」

四国めたん「unknownに算術演算子や比較演算子を直接使うとエラーです」
ずんだもん「value + 1って書いた瞬間に止められるんだよね」
四国めたん「はい。型ガードで数値か文字列に絞ってから演算してください」
ずんだもん「演算が必要な場面こそ適切な検証が重要だよ」
四国めたん「安全確認のあとに処理する流れを徹底しましょう」
ずんだもん「ツールの警告を味方にしてミスを防ごう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 演算子はエラー */
const maybeNumber: unknown = "10";
// maybeNumber + 1; // ❌
// maybeNumber > 0; // ❌

/** Example 2: number判定 */
if (typeof maybeNumber === "number") {
  console.log(maybeNumber + 1);
}

/** Example 3: string判定 */
if (typeof maybeNumber === "string") {
  console.log(maybeNumber.trim());
}
```
