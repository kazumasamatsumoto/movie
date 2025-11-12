# #495 「イベントループ」

四国めたん「イベントループも典型的なnever関数です。」
ずんだもん「eventLoop()がイベントを待ってdispatchしてた。」
四国めたん「mainLoopではpollEvents()で複数処理をまとめていました。」
ずんだもん「priorityLoopで優先度付きの処理にも触れてたね。」
四国めたん「設計に合わせてループ構造を変えましょう。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 基本ループ */
function eventLoop(): never {
  while (true) {
    const event = waitForEvent();
    dispatchEvent(event);
  }
}

/** Example 2: 複数ソース */
function mainLoop(): never {
  while (true) {
    const events = pollEvents();
    for (const event of events) {
      handleEvent(event);
    }
  }
}

/** Example 3: 優先度付き */
function priorityLoop(): never {
  while (true) {
    const event = getHighestPriorityEvent();
    if (event) {
      processEvent(event);
    } else {
      idle();
    }
  }
}
```
