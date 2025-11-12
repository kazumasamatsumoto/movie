# #407 「戻り値型がundefined」

四国めたん「戻り値がundefinedの関数は値としてundefinedを返します。」
ずんだもん「getOptionalValueは42かundefinedを返すんだね。」
四国めたん「はい。呼び出し側はundefinedチェックが必要です。」
ずんだもん「void関数との違いは値を使うかどうか?」
四国めたん「その通り。voidは用途が副作用ですが、undefinedは値そのものです。」
ずんだもん「undefFuncはreturn undefined; と明示するんだ。」
四国めたん「voidFuncはconsole.logだけして終わります。」
ずんだもん「区別して戻り値型を選ぶのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: undefined戻り値型 */
function getOptionalValue(): number | undefined {
  if (Math.random() > 0.5) {
    return 42;
  }
  return undefined;
}

/** Example 2: 値としてチェック */
const value = getOptionalValue();
if (value !== undefined) {
  console.log(value * 2);
}

/** Example 3: void型との違い */
function voidFunc(): void {
  console.log("Done");
}
function undefFunc(): undefined {
  return undefined;
}
```
