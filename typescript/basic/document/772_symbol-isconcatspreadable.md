# #772 「Symbol.isConcatSpreadable」

四国めたん「Symbol.isConcatSpreadableはArray.prototype.concatの挙動を制御します。」
ずんだもん「trueにすると配列風オブジェクトが展開されるんだね。」
四国めたん「falseにすると配列でも展開されず一括で挿入されます。」
ずんだもん「可変長の合成処理で役立ちそうだよ。」
四国めたん「TypeScriptではboolean型として扱います。」
ずんだもん「挙動を理解してconcatの細かなチューニングに活かそう！」
四国めたん「テストで結果を確認するのを忘れずに。」
ずんだもん「isConcatSpreadableで配列操作を柔軟に！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 配列風オブジェクトを展開 */
const arrayLike = {
  0: "a",
  1: "b",
  length: 2,
  [Symbol.isConcatSpreadable]: true,
};
console.log(["x"].concat(arrayLike)); // ["x", "a", "b"]

/** Example 2: 展開を抑制 */
const numbers = [1, 2];
numbers[Symbol.isConcatSpreadable] = false;
console.log([0].concat(numbers)); // [0, [1, 2]]

/** Example 3: utility */
function concatOnce<T>(base: T[], extra: T[]) {
  extra[Symbol.isConcatSpreadable] = false;
  return base.concat(extra);
}
console.log(concatOnce([1], [2, 3])); // [1, [2, 3]]
```
