# #968 「実例(1)」

四国めたん「string[] | number[]を使った実例として、設定値を配列で受け取るケースを見ましょう。」
ずんだもん「文字列のリストか数値のリストが来るやつだね。」
四国めたん「型ガードでどちらかを判定して処理します。」
ずんだもん「共通処理は関数にまとめると再利用しやすいよ。」
四国めたん「実例で配列Union型の扱いを体験してください。」
ずんだもん「柔軟な設定APIを安全に扱えるね！」

---

## 📺 画面表示用コード

```typescript
function isStringArray(value: string[] | number[]): value is string[] {
  return value.every((item) => typeof item === "string");
}

function applySetting(values: string[] | number[]) {
  if (isStringArray(values)) {
    console.log("string settings", values.join(","));
  } else {
    console.log("numeric settings", values.reduce((acc, cur) => acc + cur, 0));
  }
}

applySetting(["dev", "prod"]);
applySetting([100, 200]);
```
