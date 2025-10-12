# #568 「unknownはメソッド呼び出し不可」

四国めたん「unknown値でメソッドを呼ぶとコンパイルエラーになります」
ずんだもん「value.toUpperCase()みたいに書けないんだよね」
四国めたん「はい。型ガードでstringだと証明してから呼び出してください」
ずんだもん「カスタムガードを作れば複雑な型も扱いやすくなるよ」
四国めたん「メソッド呼び出し前の証明が安全性を担保します」
ずんだもん「エディタのエラーを味方にしていこう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 直接呼び出しはエラー */
const maybeText: unknown = "hello";
// maybeText.toUpperCase(); // ❌

/** Example 2: typeofで許可 */
if (typeof maybeText === "string") {
  console.log(maybeText.toUpperCase());
}

/** Example 3: カスタムガード */
const isDate = (value: unknown): value is Date => value instanceof Date;
const maybeDate: unknown = new Date();
if (isDate(maybeDate)) {
  console.log(maybeDate.getTime());
}
```
