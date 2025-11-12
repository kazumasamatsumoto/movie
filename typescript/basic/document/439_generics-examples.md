# #439 「実例」

四国めたん「ジェネリクスとvoidを組み合わせた実例を見てみましょう。」
ずんだもん「EventEmitter<T> クラスが登場したね。」
四国めたん「onでリスナーを登録し、emitで呼び出します。」
ずんだもん「string版のemitterはemit('Hello')でメッセージを流してた。」
四国めたん「型パラメータを省略すればvoidイベント用のemitterも作れます。」
ずんだもん「ジェネリクスのおかげで好きなデータ型でイベントを扱えるんだね。」
四国めたん「void型ならemit()だけで完結します。」
ずんだもん「実践的なvoidジェネリクスをマスターするのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: イベントエミッター */

class EventEmitter<T = void> {
  private listeners: Array<(data: T) => void> = [];

  on(listener: (data: T) => void): void {
    this.listeners.push(listener);
  }

  emit(data: T): void {
    this.listeners.forEach(fn => fn(data));
  }
}

/** Example 2: 使用例 */

const emitter = new EventEmitter<string>();
emitter.on((msg) => console.log(msg));
emitter.emit("Hello");

/** Example 3: void型のエミッター */

const voidEmitter = new EventEmitter();
voidEmitter.on(() => console.log("Event"));
voidEmitter.emit();
```
