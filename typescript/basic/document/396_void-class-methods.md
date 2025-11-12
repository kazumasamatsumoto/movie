# #396 「クラスメソッド」

四国めたん「クラスでもvoidメソッドが多数登場します。」
ずんだもん「Counter.incrementは状態を更新するだけだね。」
四国めたん「resetも副作用のみです。」
ずんだもん「Componentのinitialize/destroyもログを出すだけ?」
四国めたん「はい。ライフサイクル用のvoidメソッドです。」
ずんだもん「EventEmitter.emitもイベント名をログする副作用だ!」
四国めたん「クラスの責務を明確にするためにもvoidを付けましょう。」
ずんだもん「状態変更メソッドには積極的にvoidを使うのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: クラスメソッド */
class Counter {
  private count = 0;

  increment(): void {
    this.count++;
  }

  reset(): void {
    this.count = 0;
  }
}

/** Example 2: 初期化と破棄 */
class Component {
  initialize(): void {
    console.log("Initializing...");
  }

  destroy(): void {
    console.log("Destroying...");
  }
}

/** Example 3: イベント処理 */
class EventEmitter {
  emit(event: string): void {
    console.log(`Event: ${event}`);
  }
}
```
