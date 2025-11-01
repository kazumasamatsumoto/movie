# #831 「number型との違い」

四国めたん「bigintは整数のみ、numberはIEEE754の倍精度浮動小数点数です。」
ずんだもん「だからsmallintからfloatまでまとめて扱うnumberとは性質が違うんだね。」
四国めたん「bigintは任意精度ですが算術演算でnumberと混在できません。」
ずんだもん「numberはNaNやInfinityがあるけどbigintには存在しないよ。」
四国めたん「型も別なのでUnionで扱うときは変換処理が必須です。」
ずんだもん「違いを理解して使い分けよう！」
四国めたん「適材適所でprecisionと機能を選択してください。」
ずんだもん「numberとbigintの区別が精度を守るコツだよ！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: typeof */
console.log(typeof 1n); // "bigint"
console.log(typeof 1); // "number"

/** Example 2: 演算不可 */
// 1n + 1; // TypeError at runtime, コンパイル時もエラー

/** Example 3: 変換 */
const price: number | bigint = 100n;
const normalized = typeof price === "bigint" ? Number(price) : price;
```
