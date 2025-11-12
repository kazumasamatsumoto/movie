# #366 「間違い(1) - 混同」

四国めたん「!演算子は論理否定と記号が同じなので混同しやすいです。」
ずんだもん「const result1 = !value と value! は全然違う役割なんだね。」
四国めたん「はい。前者はbooleanを反転、後者はnullishを除去します。」
ずんだもん「if (!user!) みたいに書いたら意味不明になる?」
四国めたん「そうです。構文エラーにもなりかねないので避けましょう。」
ずんだもん「明確に比較したいときは user === null のように書けばいい?」
四国めたん「その通り。truthyチェックをする場合も user を単体で評価します。」
ずんだもん「役割の違いを整理して書き間違いを防ぐのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 混同しやすい例 */
const value: boolean | null = getValue();
const result1 = !value;   // 論理否定
const result2 = value!;   // Non-null Assertion

/** Example 2: 誤った書き方 */
if (!user!) {  // 混乱しやすい
  // ...
}

/** Example 3: 明確な比較 */
if (user === null) {  // 明確
  // ...
}
if (!user) {  // truthyチェック
  // ...
}
```
