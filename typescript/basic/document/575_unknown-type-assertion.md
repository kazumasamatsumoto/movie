# #575 「unknownと型アサーション」

四国めたん「unknownを操作したいときは型アサーションも選択肢です」
ずんだもん「value as string みたいに断言するやつだね」
四国めたん「はい。ただし安全な根拠があるときに限定しましょう」
ずんだもん「テスト済みの値やスキーマ検証後なら使いやすいよ」
四国めたん「アサーション乱用はany化と変わらないので慎重に」
ずんだもん「証明したうえで最小限に使うのがベストだね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: アサーション利用 */
const payload: unknown = "text";
const text = payload as string;
console.log(text.toLowerCase());

/** Example 2: スキーマ検証後 */
function requireNumber(value: unknown): number {
  if (typeof value !== "number") throw new TypeError("number only");
  return value;
}

/** Example 3: DOM API */
const element = document.getElementById("app");
const app = element as HTMLElement | null;
```
