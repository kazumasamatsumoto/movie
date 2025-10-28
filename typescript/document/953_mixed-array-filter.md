# #953 「filter操作」

四国めたん「filterを使うときは型述語を使って要素型を絞り込むと便利です。」
ずんだもん「(item): item is string => typeof item === "string" みたいなやつだね。」
四国めたん「filter結果がstring[]などに変わるのでその後の処理が楽になります。」
ずんだもん「単純な真偽値だけだとUnionのままだから注意しよう。」
四国めたん「型述語filterを活用して混合配列を扱いやすくしましょう。」
ずんだもん「型安全なfilterを覚えてね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 型述語 */
const values: (string | number)[] = ["ok", 200, "ng"];
const strings = values.filter((item): item is string => typeof item === "string");

/** Example 2: numbers */
const numbers = values.filter((item): item is number => typeof item === "number");

/** Example 3: カスタム述語 */
function isNonEmptyString(value: unknown): value is string {
  return typeof value === "string" && value.length > 0;
}
const nonEmpty = values.filter(isNonEmptyString);
```
