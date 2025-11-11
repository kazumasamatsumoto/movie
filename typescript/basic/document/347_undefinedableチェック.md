# #347 「undefinedableチェック」

四国めたん「undefinedableのチェック方法を学びましょう!」
ずんだもん「厳密等価演算子でundefinedと比較するんだね!」
四国めたん「はい。value !== undefined で型ガードが効きます。」
ずんだもん「typeof演算子でもチェックできるの?」
四国めたん「その通りです。typeof value === "string" で文字列型に絞り込めます。」
ずんだもん「Optional Chainingも使えるの?」
四国めたん「はい。value?.length のように、安全にプロパティアクセスできます。」
ずんだもん「適切なチェックで安全なコードを書くのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 基本的なチェック */
function process(value: string | undefined) {
  if (value !== undefined) {
    console.log(value.toUpperCase());
  }
}

/** Example 2: typeof演算子でのチェック */
if (typeof value === "string") {
  console.log(value.length);
}

/** Example 3: Optional Chainingとデフォルト値 */
const length = value?.length ?? 0;
const upper = value?.toUpperCase();
```
