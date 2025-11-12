# #431 「ジェネリクスのvoid型」

四国めたん「ジェネリクスでもvoid型を使えます。」
ずんだもん「Callback<T> = (value: T) => void みたいな定義があったね。」
四国めたん「はい。Tにnumberを渡せばnumberを受け取る副作用関数になります。」
ずんだもん「Promise<T>でもvoidを型引数にできるの?」
四国めたん「saveData(): Promise<void> のように書けます。」
ずんだもん「Handler<User> = (data: User) => void もよく使うよね。」
四国めたん「ジェネリクスでvoidを扱うと副作用ハンドラを再利用しやすいです。」
ずんだもん「汎用的なvoidハンドラを設計するのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: ジェネリクスでvoid型 */

type Callback<T> = (value: T) => void;
const numberCallback: Callback<number> = (n) => {
  console.log(n);
};

/** Example 2: Promiseでのvoid */

async function saveData(): Promise<void> {
  await database.save();
}

/** Example 3: 関数型のジェネリクス */

type Handler<T> = (data: T) => void;
const userHandler: Handler<User> = (user) => {
  console.log(user.name);
};
```
