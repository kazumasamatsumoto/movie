# #911 「配列型とは」

四国めたん「TypeScriptの配列型について学びましょう！」
ずんだもん「JavaScriptと同じ配列を型システムで表現できるんだよね。」
四国めたん「はい、要素型を指定することで要素ごとの型チェックが効きます。」
ずんだもん「number[]やArray<string>みたいに宣言するんだったね。」
四国めたん「配列型を使えば要素操作やメソッドの型補完が強化されます。」
ずんだもん「型安全な配列操作をマスターしよう！」
四国めたん「まずは基本構文から確認しましょう。」
ずんだもん「配列型でバグを減らすぞ！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: number配列 */
const scores: number[] = [80, 95, 70];

/** Example 2: string配列 */
const tags: Array<string> = ["ts", "angular", "nest"];

/** Example 3: 型推論 */
const versions = ["5.9", "7.0"]; // 推論: string[]
```
