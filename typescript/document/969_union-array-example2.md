# #969 「実例(2)」

四国めたん「別の実例として、APIレスポンスで文字列リストか数値リストを返すケースを見ましょう。」
ずんだもん「クライアント側でどちらか判定して処理を分けるんだね。」
四国めたん「はい、型ガードを経由して正しいロジックに分岐します。」
ずんだもん「失敗ケースでは例外を投げるなど決めておこう。」
四国めたん「Union配列を扱うフロントエンドの典型パターンです。」
ずんだもん「現場でよく使う構造だよ！」

---

## 📺 画面表示用コード

```typescript
type Payload = string[] | number[];

const response: Payload = Math.random() > 0.5 ? ["a", "b"] : [1, 2, 3];

function isStringArray(value: Payload): value is string[] {
  return value.every((item) => typeof item === "string");
}

function render(payload: Payload) {
  if (isStringArray(payload)) {
    payload.forEach((item) => console.log("tag", item));
  } else {
    payload.forEach((id) => console.log("id", id));
  }
}

render(response);
```
