# #506 「if-else文の網羅性」

四国めたん「switchだけじゃなくif-elseでも網羅性を作れるよ。」
ずんだもん「まずはStatus型とexhaustiveCheck()を定義してたね。」
四国めたん「handleStatus()でpending/success/errorをif-elseでさばいてた。」
ずんだもん「最後にelse return exhaustiveCheck(status); でneverを受けるの。」
四国めたん「条件を1個でも忘れるとそこへ落ちて型エラーになる。」
ずんだもん「Statusにtimeoutを足したバージョンではまさに怒られてた。」
四国めたん「ifチェーンでも追加ケースを検知できるのがポイント。」
ずんだもん「Unionを増やすたびにexhaustiveCheckでテスト代わりだね。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: neverを返すヘルパー */
type Status = "pending" | "success" | "error";

function exhaustiveCheck(value: never): never {
  throw new Error(`Unhandled: ${value}`);
}

/** Example 2: if-elseで網羅 */
function handleStatus(status: Status): string {
  if (status === "pending") return "処理中";
  else if (status === "success") return "成功";
  else if (status === "error") return "エラー";
  else return exhaustiveCheck(status);
}

/** Example 3: ケース追加で検知 */
type StatusWithTimeout = "pending" | "success" | "error" | "timeout";

function handle(status: StatusWithTimeout): string {
  if (status === "pending") return "処理中";
  // 残りを省略するとexhaustiveCheckが型エラーを出す
  return exhaustiveCheck(status);
}
```
