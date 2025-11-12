# #432 「デフォルト型パラメータ」

四国めたん「ジェネリクスにデフォルト型を設定すると便利です。」
ずんだもん「Callback<T = void> にすれば型引数を省略できるんだね。」
四国めたん「はい。voidCallbackのように引数無しで使えます。」
ずんだもん「もちろんnumberCallbackみたいに型を指定することもできる?」
四国めたん「その通り。必要に応じてTを上書きします。」
ずんだもん「Handler<TData = void, TResult = void> で複数のデフォルトを付ける例もあった!」
四国めたん「ジェネリクスの柔軟性がぐっと上がります。」
ずんだもん「デフォルトを活用して宣言を簡潔にするのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: デフォルト型パラメータ */

type Callback<T = void> = (value: T) => void;
const voidCallback: Callback = (v) => {
  console.log("Callback called");
};

/** Example 2: 型引数を指定 */

const numberCallback: Callback<number> = (n) => {
  console.log(n * 2);
};

/** Example 3: 複数の型パラメータ */

type Handler<TData = void, TResult = void> = (data: TData) => TResult;
const logger: Handler = () => {
  console.log("Log");
};
```
