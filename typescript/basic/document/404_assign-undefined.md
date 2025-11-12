# #404 「変数にundefined代入」

四国めたん「void型の変数にはundefinedだけを代入できます。」
ずんだもん「value: void に undefined を入れる例があったね。」
四国めたん「はい。strictNullChecksではnullも禁止です。」
ずんだもん「undefined型の変数にはundefinedしか入れられない?」
四国めたん「その通りです。」
ずんだもん「実用的には関数の戻り値をvoidで受け取ることが多いの?」
四国めたん「doSomething(): void を呼んだ結果はundefinedなので整合します。」
ずんだもん「代入ルールを理解して型エラーを防ぐのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: void型変数 */
let value: void;
value = undefined;  // OK

/** Example 2: undefined型変数 */
let undef: undefined;
undef = undefined;  // OK

/** Example 3: 戻り値として扱う */
function doSomething(): void {
  console.log("Done");
}
const result: void = doSomething();
```
