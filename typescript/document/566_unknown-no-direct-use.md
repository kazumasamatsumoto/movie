# #566 「unknown値は直接使えない」

四国めたん「unknownの値は直接操作できないと理解しましょう」
ずんだもん「プロパティアクセスも演算も全部コンパイルが止めるんだよね」
四国めたん「はい。必ずガードかアサーションを挟む必要があります」
ずんだもん「直接使えない制限こそが型安全の源だよ」
四国めたん「エディタのエラー表示を活用して忘れを防ぎましょう」
ずんだもん「チームでルールを共有しておくと安心だね」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 直接操作NG */
const value: unknown = "text";
// value.trim(); // ❌
// value.length; // ❌

/** Example 2: ガードで許可 */
if (typeof value === "string") {
  console.log(value.trim());
}

/** Example 3: アサーションで許可 */
const forced = value as string;
console.log(forced.toUpperCase());
```
