# #718 「条件付き型の活用」

四国めたん「条件付き型を使えば高度な推論でanyを避けられます」
ずんだもん「T extends U ? X : Y みたいに型レベルで分岐するんだね」
四国めたん「はい。入力に応じて戻り値の型を変えるジェネリクスで重宝します」
ずんだもん「utility型を自作するとリファクタも楽になるよ」
四国めたん「条件付き型で抽象化すればanyに頼らず汎用性を確保できます」
ずんだもん「型レベルのif文を味方につけよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 条件付き型 */
type PromiseValue<T> = T extends Promise<infer U> ? U : T;

/** Example 2: 利用 */
type A = PromiseValue<Promise<string>>; // string
type B = PromiseValue<number>; // number

/** Example 3: 関数に応用 */
function unwrap<T>(value: T): PromiseValue<T> {
  return (value instanceof Promise ? value.then((v) => v) : value) as PromiseValue<T>;
}
```
