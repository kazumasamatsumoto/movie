# #254 「null/undefinedの比較」

四国めたん「nullとundefinedの比較について学びましょう!」
ずんだもん「この2つって似てるけど違うんだよね?」
四国めたん「はい。==では等しいと判定されますが、===では異なります。」
ずんだもん「null == undefinedはtrueなの?」
四国めたん「その通りです。しかしnull === undefinedはfalseになります。」
ずんだもん「厳密に判定したい場合は===を使うべきなんだね!」
四国めたん「はい。型述語関数を使うとより型安全になります。」
ずんだもん「isNullやisUndefined関数で明示的にチェックするのが良いのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: ==による比較（型変換あり） */
console.log(null == undefined);  // true

/** Example 2: ===による比較（厳密） */
console.log(null === undefined); // false
console.log(null === null);      // true
console.log(undefined === undefined); // true

/** Example 3: 型安全なチェック */
function isNull(value: unknown): value is null {
  return value === null;
}

function isUndefined(value: unknown): value is undefined {
  return value === undefined;
}
```
