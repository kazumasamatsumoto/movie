# #882 「JSON表現方法」

四国めたん「BigIntをJSONで表現する方法を決めましょう。」
ずんだもん「文字列、数値文字列+単位、オブジェクトラップの3パターンが多いよね。」
四国めたん「はい、"123"、{"value":"123"}, {"value":"123","unit":"wei"}のように表せます。」
ずんだもん「受信側が復元しやすい形を選ぼう。」
四国めたん「スキーマでフォーマットを明示してドキュメント化するのが大切です。」
ずんだもん「JSON表現を統一してBigIntを安全に流通させよう！」
四国めたん「テストケースもフォローしてください。」
ずんだもん「表現方法を合意してから実装してね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: シンプル文字列 */
const simple = { amount: 1234567890n.toString() };

/** Example 2: ラップ形式 */
const wrapped = { amount: { value: 1234567890n.toString() } };

/** Example 3: 単位付き */
const withUnit = { amount: { value: 1234567890n.toString(), unit: "wei" } };
```
