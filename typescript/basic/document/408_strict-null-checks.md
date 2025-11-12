# #408 「strictNullChecks」

四国めたん「strictNullChecksの有無でvoidとundefinedの扱いが変わります。」
ずんだもん「trueならvoidValueにnullを入れられないんだね。」
四国めたん「はい。undefinedのみ許可されます。」
ずんだもん「strictNullChecks: false だとnullも入っちゃうの?」
四国めたん「入りますが非推奨です。」
ずんだもん「f1(): void と f2(): undefined の違いも押さえておく!」
四国めたん「voidは戻り値を気にせず、undefined型はundefinedを返す関数です。」
ずんだもん「設定ごとの挙動を理解するのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: strictNullChecks: true */
let voidValue: void;
voidValue = undefined;
let undefValue: undefined;
undefValue = undefined;

/** Example 2: strictNullChecks: false */
let value: void;
value = undefined;
value = null;

/** Example 3: 関数の戻り値 */
function f1(): void {}
function f2(): undefined {
  return undefined;
}
```
