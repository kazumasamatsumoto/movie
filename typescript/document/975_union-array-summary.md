# #975 「総まとめ」

四国めたん「配列とUnion型の違いと使い分けをまとめましょう。」
ずんだもん「(string | number)[]は混在、string[] | number[]は排他的だったね。」
四国めたん「はい、型ガードやベストプラクティスも確認しました。」
ずんだもん「意図に合わせて型を設計すれば安全に運用できるよ。」
四国めたん「次は配列のループと型推論を見ていきます。」
ずんだもん「Union配列のマスター完了だよ！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 混在 */
const mixed: (string | number)[] = ["ok", 200];

/** Example 2: 排他的 */
const exclusive: string[] | number[] = ["ok"];

/** Example 3: 型ガード */
const isNumberArray = (value: string[] | number[]): value is number[] =>
  value.every((item) => typeof item === "number");
```
