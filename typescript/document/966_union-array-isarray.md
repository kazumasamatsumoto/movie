# #966 「Array.isArray()」

四国めたん「Array.isArray()は配列かどうかを判定する組み込み関数です。」
ずんだもん「Unionで配列と単体の値が混ざるときに活躍するね。」
四国めたん「はい、string[] | string のような型でもisArrayで分岐できます。」
ずんだもん「配列確定後にさらに要素の型判定を続けると安全だよ。」
四国めたん「Array.isArray()を活用して型ガードを組み立てましょう。」
ずんだもん「ベーシックなパターンを押さえておこう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Union */
function normalize(value: string | string[]): string[] {
  return Array.isArray(value) ? value : [value];
}

/** Example 2: さらなる判定 */
function isStringArray(value: unknown): value is string[] {
  return Array.isArray(value) && value.every((item) => typeof item === "string");
}

/** Example 3: ガード */
const payload: string[] | string = "ok";
if (Array.isArray(payload)) {
  payload.forEach((p) => console.log(p));
}
```
