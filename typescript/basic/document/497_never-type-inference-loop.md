# #497 「型推論」

四国めたん「TypeScriptはループの終わり方によってneverかvoidを推論します。」
ずんだもん「loop1()はbreakもreturnも無いからneverなんだね。」
四国めたん「loop2()は条件次第で抜けるからvoidです。」
ずんだもん「loop3()もforeverフラグで戻れる可能性があるんだ。」
四国めたん「推論結果を理解して意図と違う場合は明示的に注釈を付けましょう。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: never推論 */
function loop1() {
  while (true) {
    doWork();
  }
}

/** Example 2: void推論 */
function loop2() {
  while (true) {
    doWork();
    if (shouldStop()) {
      break;
    }
  }
}

/** Example 3: 条件で変わる */
function loop3(forever: boolean) {
  while (true) {
    process();
    if (!forever) return;
  }
}
```
