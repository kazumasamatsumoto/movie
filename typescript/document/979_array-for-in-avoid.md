# #979 「for...inは避ける」

四国めたん「配列にはfor...inを使わないのがベストです。」
ずんだもん「プロパティ列挙用だから順序保証もないんだよね。」
四国めたん「はい、配列要素よりもキー（文字列）を走査してしまいます。」
ずんだもん「配列にはfor、for...of、forEachを使おう。」
四国めたん「既存コードで見つけたらレビューで指摘しましょう。」
ずんだもん「for...inはオブジェクト専用と覚えてね！」

---

## 📺 画面表示用コード

```typescript
const scores = [80, 90, 70];

/** Example 1: for...in (避ける) */
for (const key in scores) {
  console.log(key, scores[key]); // keyはstring
}

/** Example 2: for...of */
for (const score of scores) {
  console.log(score);
}

/** Example 3: forEach */
scores.forEach((score, index) => console.log(index, score));
```
