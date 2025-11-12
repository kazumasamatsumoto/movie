# #356 「??と||の違い」

四国めたん「?? と || の違いを理解しましょう!」
ずんだもん「|| は0や空文字もfalsy扱いで上書きしちゃうんだね?」
四国めたん「はい。でも ?? ならnullとundefinedだけを対象にします。」
ずんだもん「音量0を許可したいときは?? が必要?」
四国めたん「その通り。volume ?? 50 なら0を維持できます。」
ずんだもん「booleanのfalseも保持できるの?」
四国めたん「enabled ?? true のようにfalseを尊重できます。」
ずんだもん「値がfalsyでも意味があるなら??を選ぶのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: ?? と || の結果の違い */
const count1 = 0 || 10;   // 10 (0はfalsy)
const count2 = 0 ?? 10;   // 0  (0はnullishではない)

const text1 = "" || "default";   // "default"
const text2 = "" ?? "default";   // ""

/** Example 2: 数値デフォルトへの適用 */
function setVolume(volume: number | null | undefined) {
  const vol = volume ?? 50;  // 0も有効な音量
  console.log(`Volume: ${vol}`);
}

/** Example 3: 真偽値デフォルトへの適用 */
const enabled = config.enabled ?? true;  // falseも有効
const verbose = options.verbose ?? false;
```
