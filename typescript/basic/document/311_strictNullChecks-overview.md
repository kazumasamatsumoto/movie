# #311 「strictNullChecksとは」

四国めたん「strictNullChecksについて学びましょう!」
ずんだもん「null と undefined を厳密にチェックするオプションなの?」
四国めたん「はい。無効時は全ての型にnullとundefinedが含まれますが、有効時は明示的に指定が必要です。」
ずんだもん「strictNullChecks: false だと string型にnullを代入できるんだね!」
四国めたん「その通りです。でもそれは実行時エラーの原因になる危険なコードです。」
ずんだもん「有効にすると string | null のように明示的に書く必要があるの?」
四国めたん「はい。tsconfig.jsonで設定でき、strict: trueにも含まれています。」
ずんだもん「nullポインタ例外を防ぐために、有効にするのが推奨なのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: strictNullChecks: false (無効) */
let name: string = null; // OK (エラーなし)
let age: number = undefined; // OK

/** Example 2: strictNullChecks: true (有効) */
let name: string = null; // エラー
let name: string | null = null; // OK

/** Example 3: tsconfig.jsonで設定 */
{
  "compilerOptions": {
    "strictNullChecks": true
  }
}
```
