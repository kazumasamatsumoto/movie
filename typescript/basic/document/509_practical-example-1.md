# #509 「実践例(1)」

四国めたん「実践例その1は数値reducerの網羅性だよ。」
ずんだもん「Actionはincrement/decrement/resetの3種類だったね。」
四国めたん「reducer()でifチェーンを書いてconst check: never = action;で締めてた。」
ずんだもん「新しいアクションを追加したときに即エラーになる設計だ。」
四国めたん「multiplyを足した例だとreducerが未対応だから型が怒る。」
ずんだもん「payload付きの型でもneverチェックは問題なく動くよ。」
四国めたん「この仕組みなら安全にアクションを増やしていけるね。」
ずんだもん「Unionの現場投入でもneverが守ってくれるのだ。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 数値カウンターのAction */
type Action =
  | { type: "increment"; payload: number }
  | { type: "decrement"; payload: number }
  | { type: "reset" };

/** Example 2: reducerで網羅チェック */
function reducer(state: number, action: Action): number {
  if (action.type === "increment") return state + action.payload;
  if (action.type === "decrement") return state - action.payload;
  if (action.type === "reset") return 0;
  const check: never = action;
  return state;
}

/** Example 3: 追加アクションでエラー */
type ExtendedAction =
  | { type: "increment"; payload: number }
  | { type: "decrement"; payload: number }
  | { type: "reset" }
  | { type: "multiply"; payload: number };

// reducer側がmultiplyを処理しないと型エラーで気付ける
```
