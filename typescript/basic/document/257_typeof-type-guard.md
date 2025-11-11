# #257 「typeof型ガード」

四国めたん「typeof型ガードについて学びましょう!」
ずんだもん「typeofでプリミティブ型を判定できるんだね!」
四国めたん「はい。string、number、booleanなどの型チェックに使えます。」
ずんだもん「if文で型を絞り込むと、その中では安全にメソッドが使えるの?」
四国めたん「その通りです。各型専用のメソッドが使えるようになります。」
ずんだもん「unknownからnumberに絞り込んで演算するのも安全だね!」
四国めたん「型が一致しない場合はundefinedを返すパターンもよく使われます。」
ずんだもん「型安全な処理ができるから、バグを防げるのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 複数の型の処理 */
function processValue(value: string | number | boolean) {
  if (typeof value === 'string') {
    console.log(value.toUpperCase());
  } else if (typeof value === 'number') {
    console.log(value.toFixed(2));
  } else {
    console.log(!value);
  }
}

/** Example 2: 型安全な処理 */
function double(value: unknown): number | undefined {
  if (typeof value === 'number') {
    return value * 2;
  }
  return undefined;
}
```
