# #375 「return文」

四国めたん「void関数でのreturn文の書き方を整理しましょう。」
ずんだもん「validateのように条件によってreturn;するのが基本だね。」
四国めたん「はい。値を返さない早期リターンなら安全です。」
ずんだもん「でもreturn "string"; はエラーになるんだ?」
四国めたん「はい、Type 'string' is not assignable to type 'void' と怒られます。」
ずんだもん「undefinedだけはOKってこと?」
四国めたん「その通り。allowed関数のようにreturn undefined; か単なるreturn; を使います。」
ずんだもん「return文のルールを守ってvoidを使いこなすのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 早期リターン */
function validate(value: string): void {
  if (!value) return;  // 値なし
  if (value.length < 3) return;
  console.log(`Valid: ${value}`);
}

/** Example 2: エラーになる例 */
function invalid(): void {
  return "string";  // エラー
}

/** Example 3: undefinedは許可 */
function allowed(): void {
  return undefined;  // OK
  return;            // OK (推奨)
}
```
