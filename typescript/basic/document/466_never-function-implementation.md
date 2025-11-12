# #466 「関数の実装」

四国めたん「never関数は必ず制御を戻さない実装にしましょう。」
ずんだもん「failはthrowだけ、loopはwhile(true)だったね。」
四国めたん「console.logだけしてreturnするとvoid扱いになってしまいます。」
ずんだもん「invalid() の例がまさにそれ!」
四国めたん「実装がルールを破ると型エラーで指摘されます。」
ずんだもん「never関数はthrowか無限ループに限定するのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: throw文 */
function fail(message: string): never {
  throw new Error(message);
}

/** Example 2: 無限ループ */
function loop(): never {
  while (true) {
    doWork();
  }
}

/** Example 3: エラーになる例 */
function invalid(): never {
  console.log("Error");
  // return;
}
```
