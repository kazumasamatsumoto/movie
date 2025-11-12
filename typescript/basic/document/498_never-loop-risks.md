# #498 「リスク」

四国めたん「無限ループにはCPU占有などのリスクがあります。」
ずんだもん「badLoop()は何もせず回り続けてた。」
四国めたん「goodLoop()やasyncLoop()のように待機を入れて負荷を下げましょう。」
ずんだもん「副作用だけでなくリソースへの影響も意識するのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 悪い例 */
function badLoop(): never {
  while (true) {
    // CPU 100%
  }
}

/** Example 2: 良い例 */
function goodLoop(): never {
  while (true) {
    doWork();
    sleep(100);
  }
}

/** Example 3: 非同期ループ */
async function asyncLoop(): never {
  while (true) {
    await processTask();
    await delay(1000);
  }
}
```
