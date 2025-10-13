# #967 「配列Union型の型ガード」

四国めたん「string[] | number[]のようなUnion型配列を扱うには型ガードが必要です。」
ずんだもん「Array.isArray()と要素チェックを組み合わせるんだね。」
四国めたん「はい、ユーザー定義型述語でstring[]かnumber[]かを判定すると便利です。」
ずんだもん「ガードを使えば分岐後に型が確定するから処理が楽になるよ。」
四国めたん「型ガードで配列Unionを安全に扱いましょう。」
ずんだもん「再利用できる関数を用意してね！」

---

## 📺 画面表示用コード

```typescript
function isStringArray(value: string[] | number[]): value is string[] {
  return value.every((item) => typeof item === "string");
}

function isNumberArray(value: string[] | number[]): value is number[] {
  return value.every((item) => typeof item === "number");
}

const payload: string[] | number[] = Math.random() > 0.5 ? ["a"] : [1, 2, 3];

if (isStringArray(payload)) {
  payload.forEach((s) => console.log(s.toUpperCase()));
} else if (isNumberArray(payload)) {
  payload.forEach((n) => console.log(n.toFixed(2)));
}
```
