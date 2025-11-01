# #977 「for...ofの型推論」

四国めたん「for...ofを使うと要素型が自動で推論されます。」
ずんだもん「for (const score of scores) { ... } みたいに書くやつだね。」
四国めたん「scoreの型は配列の要素型になります。」
ずんだもん「indexが不要ならfor...ofの方が読みやすいよ。」
四国めたん「推論を活かして簡潔にループを書きましょう。」
ずんだもん「for...ofの型推論を覚えてね！」

---

## 📺 画面表示用コード

```typescript
const scores = [80, 90, 70];

/** Example 1: 基本 */
for (const score of scores) {
  console.log(score); // score: number
}

/** Example 2: Union */
const tokens: (string | number)[] = ["ok", 200];
for (const token of tokens) {
  // token: string | number
}

/** Example 3: タプル */
const entries: Array<[string, number]> = [["a", 1]];
for (const [key, value] of entries) {
  console.log(key, value);
}
```
