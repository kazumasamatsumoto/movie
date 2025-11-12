# #500 「無限ループまとめ」

四国めたん「無限ループのポイントをまとめましょう。」
ずんだもん「eventLoopのような基本を押さえる!」
四国めたん「遅延や待機を入れてCPUを守りましょう。」
ずんだもん「safeLoopでエラーハンドリングするのも大切。」
四国めたん「これらを意識すれば安定したループが書けます。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 基本ループ */
function eventLoop(): never {
  while (true) {
    const event = getEvent();
    processEvent(event);
  }
}

/** Example 2: 適切な待機 */
async function serverLoop(): never {
  while (true) {
    const request = await waitForRequest();
    await handleRequest(request);
    await delay(100);
  }
}

/** Example 3: エラーハンドリング */
function safeLoop(): never {
  while (true) {
    try {
      processTask();
    } catch (error) {
      console.error(error);
    }
  }
}
```
