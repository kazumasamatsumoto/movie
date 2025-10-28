# #933 「範囲外アクセス」

四国めたん「存在しないインデックスにアクセスするとundefinedが返ります。」
ずんだもん「TypeScriptの型は要素型だけど、実行時はundefinedを返すんだね。」
四国めたん「範囲チェックをせずに使うと実行時エラーにつながる可能性があります。」
ずんだもん「lengthで境界を確認するか、atメソッドを使うといいよ。」
四国めたん「安全対策を取りながらアクセスしましょう。」
ずんだもん「範囲外アクセスに気をつけてね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: undefined */
const list = ["a", "b"];
const missing = list[5]; // undefined

/** Example 2: guard */
const value = list[5];
if (value !== undefined) {
  console.log(value.toUpperCase());
}

/** Example 3: lengthチェック */
function getLast<T>(items: T[]): T | undefined {
  return items.length > 0 ? items[items.length - 1] : undefined;
}
```
