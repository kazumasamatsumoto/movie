# #409 「互換性」

四国めたん「voidとundefinedには代入互換性があります。」
ずんだもん「let v: void = undefined; はOKだったね。」
四国めたん「はい。逆方向も多くの場合許可されます。」
ずんだもん「関数の戻り値だと違いが出る?」
四国めたん「returnsVoidはreturn undefined; が許可されますが、returnsUndefinedは型が厳密です。」
ずんだもん「f1: () => void に () => undefined を代入するのはOK?」
四国めたん「はい。でも逆はケースによってはエラーです。」
ずんだもん「互換性ルールを理解して安心して代入するのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 代入互換性 */
let v: void = undefined;
let u: undefined = undefined;
let v2: void = u;

/** Example 2: 関数の戻り値 */
function returnsVoid(): void {
  return undefined;
}
function returnsUndefined(): undefined {
  return undefined;
}

/** Example 3: 代入の互換性 */
const f1: () => void = (): undefined => undefined;
// const f2: () => undefined = (): void => {};
```
