# #264 「falsyチェック」

四国めたん「falsyチェックについて学びましょう!」
ずんだもん「値が存在しないかチェックする方法だね!」
四国めたん「はい。!を使って値を評価するとfalsyかどうか判定できます。」
ずんだもん「falsyな値ってどんなもの?」
四国めたん「その通りです。false、0、空文字、null、undefined、NaNの6つです。」
ずんだもん「これらは全部falseになるんだね!」
四国めたん「はい。Boolean()で確認すると全てfalseを返します。」
ずんだもん「エラーハンドリングに役立つのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: falsyチェック */
function process(value: string | number | null) {
  if (!value) {
    // falsyな値の場合
    console.log('値が存在しないか、falsy値です');
  }
}

/** Example 2: falsy値の例 */
console.log(Boolean(false));    // false
console.log(Boolean(0));        // false
console.log(Boolean(''));       // false
console.log(Boolean(null));     // false
console.log(Boolean(undefined));// false
console.log(Boolean(NaN));      // false
```
