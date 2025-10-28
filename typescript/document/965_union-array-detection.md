# #965 「string[] | number[]の判定」

四国めたん「string[] | number[]を扱うときは配列の中身を見て型を判断します。」
ずんだもん「typeof array[0] === "string" みたいに判定するんだね。」
四国めたん「lengthが0の場合は別の基準を決める必要があります。」
ずんだもん「カスタム型ガードで判定ロジックを共通化すると楽だよ。」
四国めたん「配列全体の型判定を用意して安全に扱いましょう。」
ずんだもん「Union配列の判定をしっかり覚えてね！」

---

## 📺 画面表示用コード

```typescript
function isStringArray(value: string[] | number[]): value is string[] {
  return value.every((item) => typeof item === "string");
}

function isNumberArray(value: string[] | number[]): value is number[] {
  return value.every((item) => typeof item === "number");
}

const payload: string[] | number[] = Math.random() > 0.5 ? ["a"] : [1, 2];

if (isStringArray(payload)) {
  payload.forEach((s) => console.log(s.toUpperCase()));
} else if (isNumberArray(payload)) {
  payload.forEach((n) => console.log(n.toFixed(2)));
}
```
