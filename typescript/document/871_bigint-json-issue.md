# #871 「JSONの問題」

四国めたん「JSONはbigintを直接表現できません。」
ずんだもん「JSON.stringifyするとTypeErrorになるんだね。」
四国めたん「文字列に変換してから埋め込む必要があります。」
ずんだもん「APIで数値として返すと桁落ちする危険があるよ。」
四国めたん「JSONの仕様はIEEE754に基づくので対策が必須です。」
ずんだもん「問題点を理解して変換戦略を用意しよう！」
四国めたん「シリアライズ・デシリアライズでBigIntを保護してください。」
ずんだもん「JSONとのギャップに注意してね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: stringify失敗 */
try {
  JSON.stringify({ value: 1n });
} catch (error) {
  console.error("TypeError", error);
}

/** Example 2: 文字列化 */
const payload = { value: 1n.toString() };
console.log(JSON.stringify(payload));

/** Example 3: bigint-aware replacer */
const json = JSON.stringify({ amount: 1000n }, (_, v) => (typeof v === "bigint" ? v.toString() : v));
```
