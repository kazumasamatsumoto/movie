# #657 「anyが招くランタイムエラー②」

四国めたん「2つ目はanyを関数として呼び出してしまうパターンです」
ずんだもん「value()って呼んだら実際はオブジェクトだったケースだね」
四国めたん「はい。anyだとコンパイルが止めないので本番でTypeErrorが発生します」
ずんだもん「typeof value === \"function\"で確認しておけば安心だよ」
四国めたん「unknownにすればコンパイル時に警告してくれます」
ずんだもん「呼び出し前のチェックを習慣化しよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: any関数呼び出し */
const maybeFn: any = {};
maybeFn(); // TypeError: maybeFn is not a function

/** Example 2: unknownで保護 */
const safeFn: unknown = {};
if (typeof safeFn === "function") {
  safeFn();
}

/** Example 3: 型ガード */
const isFunction = (value: unknown): value is (...args: unknown[]) => unknown =>
  typeof value === "function";
```
