# #723 「代替実例②」

四国めたん「次の例はユーティリティ関数のanyをジェネリクスと条件付き型で置き換えたケースです」
ずんだもん「以前はmerge(objA, objB): anyだったんだよね」
四国めたん「はい。Merge<T, U>型を定義して戻り値を正しく推論できるようにしました」
ずんだもん「呼び出し側の補完が効くようになってバグが減ったよ」
四国めたん「実装も変わらず、型定義を整えるだけで効果が出ました」
ずんだもん「共通関数を型安全にして開発体験を上げよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Merge型 */
type Merge<T, U> = {
  [K in keyof T | keyof U]: K extends keyof U
    ? U[K]
    : K extends keyof T
    ? T[K]
    : never;
};

/** Example 2: 型付き関数 */
function merge<T, U>(left: T, right: U): Merge<T, U> {
  return { ...left, ...right } as Merge<T, U>;
}

/** Example 3: 利用 */
const merged = merge({ id: 1, name: "A" }, { name: "B", email: "b@example.com" });
// 推論結果: { id: number; name: string; email: string }
```
