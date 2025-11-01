# #620 「ユーザー入力の取り扱い」

四国めたん「ユーザー入力はunknownで受けて検証しましょう」
ずんだもん「フォームやURLパラメータは何が来るかわからないもんね」
四国めたん「はい。文字列かどうか、数値に変換できるかを確認します」
ずんだもん「バリデーション関数を共有化すると開発が楽になるよ」
四国めたん「入力の安全性を確保すればアプリ全体が堅牢になります」
ずんだもん「unknown起点でのチェックを徹底しよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 入力取得 */
function getInput(): unknown {
  return (document.querySelector("input") as HTMLInputElement).value;
}

/** Example 2: 検証 */
const isNonEmptyString = (value: unknown): value is string =>
  typeof value === "string" && value.trim().length > 0;

/** Example 3: 利用例 */
const input = getInput();
if (isNonEmptyString(input)) console.log(input.toUpperCase());
```
