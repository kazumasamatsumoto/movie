# #299 「初期化されていない変数」

四国めたん「初期化されていない変数について学びましょう!」
ずんだもん「宣言だけして値を入れない変数のこと?」
四国めたん「はい。その場合、変数の値はundefinedになります。」
ずんだもん「console.logするとundefinedって出るんだね!」
四国めたん「その通りです。strictモードでは初期化が必要になることもあります。」
ずんだもん「エラーを防ぐために明示的にundefinedを入れるの?」
四国めたん「はい。Union型で宣言して、適切にチェックします。」
ずんだもん「!== undefinedで確認してから使うのが安全なのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 初期化されていない変数 */
let name: string | undefined;
console.log(name); // undefined

/** Example 2: strictモードでのエラー */
// let id: number; // エラー: 初期化が必要
// id = 42;  // OK

/** Example 3: 明示的なundefined */
let value: string | undefined = undefined;
if (value !== undefined) {
  console.log(value.toUpperCase());
}
```
