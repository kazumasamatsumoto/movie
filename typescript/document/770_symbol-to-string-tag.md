# #770 「Symbol.toStringTag」

四国めたん「Symbol.toStringTagはObject.prototype.toStringの表示名を変えます。」
ずんだもん「[object Custom]みたいに表示させられるんだよね。」
四国めたん「デバッグで識別しやすくなる利点があります。」
ずんだもん「クラスに設定するとインスタンス全部に効くよ。」
四国めたん「ただしこの値は列挙されないので意図的に使いましょう。」
ずんだもん「ツールと連携するときに重宝するね。」
四国めたん「Symbol.toStringTagで識別しやすいオブジェクトを作りましょう。」
ずんだもん「ロガーや検査ツールが見やすくなるよ！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: プレーンオブジェクトに設定 */
const resource = {
  [Symbol.toStringTag]: "Resource",
};
console.log(Object.prototype.toString.call(resource)); // [object Resource]

/** Example 2: クラスで設定 */
class UserCollection {
  [Symbol.toStringTag] = "UserCollection";
}
console.log(Object.prototype.toString.call(new UserCollection()));

/** Example 3: ライブラリとの連携 */
function isResource(value: unknown): boolean {
  return Object.prototype.toString.call(value) === "[object Resource]";
}
console.log(isResource(resource)); // true
```
