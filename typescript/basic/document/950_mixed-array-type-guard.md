# #950 「型ガード」

四国めたん「混合型配列では型ガードが重要です。」
ずんだもん「typeofやユーザー定義型述語で要素の型を判別するんだね。」
四国めたん「配列メソッドのコールバック内でも活用できます。」
ずんだもん「型ガードがあるとIDE補完も正確になるよ。」
四国めたん「要素処理の前に型ガードを入れる習慣を付けましょう。」
ずんだもん「安全に操作するための基本だね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: typeof */
function isString(value: unknown): value is string {
  return typeof value === "string";
}

const values: (string | number)[] = ["ok", 200];
if (isString(values[0])) {
  console.log(values[0].toUpperCase());
}

/** Example 2: in演算子 */
function isError(value: unknown): value is { error: string } {
  return typeof value === "object" && value !== null && "error" in value;
}

/** Example 3: filter */
const onlyStrings = values.filter(isString); // string[]
```
