# #980 「forEachの型」

四国めたん「配列のforEachメソッドはコールバックに要素型・インデックス・配列を渡します。」
ずんだもん「(value: T, index: number, array: T[]) => void の形だね。」
四国めたん「戻り値は無視されるので注意しましょう。」
ずんだもん「型推論が効くので型注釈は不要だけど、明示することもできるよ。」
四国めたん「forEachの型を理解してコールバックを正しく設計しましょう。」
ずんだもん「基礎を押さえてね！」

---

## 📺 画面表示用コード

```typescript
const users = ["meta", "zunda"];

/** Example 1: 推論 */
users.forEach((user, index, array) => {
  console.log(user.toUpperCase(), index, array.length);
});

/** Example 2: 明示的型 */
users.forEach((user: string) => console.log(user));

/** Example 3: 汎用 */
function logEach<T>(items: T[], callback: (value: T, index: number, array: T[]) => void) {
  items.forEach(callback);
}
```
