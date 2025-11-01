# #976 「for文」

四国めたん「従来のfor文は配列をループする基本構文です。」
ずんだもん「for (let i = 0; i < arr.length; i++) { ... } って書くやつだね。」
四国めたん「インデックス操作が必要なときに便利です。」
ずんだもん「TypeScriptではiの型がnumber、arr[i]の型が要素型になるよ。」
四国めたん「for文で細かな制御が必要な場面を押さえておきましょう。」
ずんだもん「基本を復習してね！」

---

## 📺 画面表示用コード

```typescript
const scores = [80, 90, 70];

/** Example 1: 基本 */
for (let i = 0; i < scores.length; i++) {
  console.log(i, scores[i]);
}

/** Example 2: インデックス制御 */
for (let i = scores.length - 1; i >= 0; i--) {
  console.log("reverse", scores[i]);
}

/** Example 3: 累積 */
let total = 0;
for (let i = 0; i < scores.length; i++) {
  total += scores[i];
}
```
