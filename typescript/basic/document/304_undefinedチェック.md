# #304 「undefinedチェック」

四国めたん「undefinedチェックについて学びましょう!」
ずんだもん「undefinedかどうか確認する方法は?」
四国めたん「はい。厳密等価演算子===で型ガードできます。」
ずんだもん「value === undefinedでチェックするんだね!」
四国めたん「その通りです。Nullish Coalescing演算子も便利です。」
ずんだもん「??演算子って何をするの?」
四国めたん「はい。undefined/nullの時だけデフォルト値を使います。」
ずんだもん「オプショナルチェーン?.と組み合わせると、安全に扱えるのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 厳密等価演算子と型ガード */
if (value === undefined) {
  console.log("undefined");
}
function isDefined<T>(value: T | undefined): value is T {
  return value !== undefined;
}

/** Example 2: Nullish Coalescing */
const name = userName ?? "Guest";
const config = settings?.timeout ?? 5000;

/** Example 3: オプショナルチェーン */
const zip = user?.address?.zipCode;
// userまたはaddressがundefinedならundefined
```
