# #1059 「型の絞り込み」

四国めたん「型述語でfindを使うと戻り値の型が絞り込まれます。」
ずんだもん「string | number の配列からstringだけ探すとstring | undefinedになるんだね。」
四国めたん「はい、結果に対して追加の型チェックが不要になります。」
ずんだもん「Union配列を扱うときに重宝するよ。」
四国めたん「型の絞り込み効果を確認して使いこなしてください。」
ずんだもん「安全に一件だけ取得できるね！」

---

## 📺 画面表示用コード

```typescript
const tokens: (string | number)[] = ["ok", 200, "ng"];

const firstString = tokens.find((token): token is string => typeof token === "string");

if (firstString) {
  console.log(firstString.toUpperCase());
}
```
