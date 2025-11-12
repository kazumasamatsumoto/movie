# #389 「明示的return」

四国めたん「void関数でもreturn; を明示する場面があります。」
ずんだもん「processDataではnullチェック後にreturn;してるね。」
四国めたん「はい。不要な処理を避けるための早期終了です。」
ずんだもん「notifyも通知設定が無ければreturn;で抜けてる!」
四国めたん「その通り。条件に応じて処理を打ち切ります。」
ずんだもん「invalidでreturn "value"; と書くとエラーなのは覚えておく!」
四国めたん「void関数に値を返すと型エラーになる点を忘れないでください。」
ずんだもん「returnの書き方を正しく選ぶのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 早期リターン */
function processData(data: string | null): void {
  if (data === null) return;
  console.log(data.toUpperCase());
}

/** Example 2: 条件分岐 */
function notify(user: User): void {
  if (!user.notifications) return;
  sendEmail(user.email);
  logNotification(user.id);
}

/** Example 3: エラーになる例 */
function invalid(): void {
  return "value";  // エラー
}
```
