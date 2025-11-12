# #533 「型変換」

四国めたん「neverを使うと色んな型変換が書けるよ。」
ずんだもん「Without<T, U>はUnionから特定の型だけ除いてくれたね。」
四国めたん「string | number | booleanからnumberだけを残していたのが爽快。」
ずんだもん「PickByType<T, ValueType>ならオブジェクトの中で型がマッチするキーだけ拾える。」
四国めたん「nameとemailがstringだからピックアップできたのだ。」
ずんだもん「DeepOmit<T, K>はネストした_idを全部取り除いてたよ。」
四国めたん「再帰マッピングで深いオブジェクトも綺麗にできる。」
ずんだもん「型変換を駆使してAPIレスポンスを整えよう。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Unionからの除外 */
type Without<T, U> = T extends U ? never : T;
type Numbers = Without<string | number | boolean, string | boolean>; // number
```

```typescript
/** Example 2: 型でプロパティを選択 */
type PickByType<T, ValueType> = {
  [K in keyof T as T[K] extends ValueType ? K : never]: T[K];
};

type StringProps = PickByType<{
  name: string;
  age: number;
  email: string;
}, string>; // { name: string; email: string }
```

```typescript
/** Example 3: DeepOmitでネストを削除 */
type DeepOmit<T, K extends string> = {
  [P in keyof T as P extends K ? never : P]:
    T[P] extends object ? DeepOmit<T[P], K> : T[P];
};

type Clean = DeepOmit<{
  _id: string;
  user: { _id: string; name: string };
}, "_id">; // { user: { name: string } }
```
