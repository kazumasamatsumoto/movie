# #501 「網羅性チェックとは」

四国めたん「今日は網羅性チェックの基本を押さえるよ。」
ずんだもん「Status型みたいに列挙したリテラルを全部扱うやつだね。」
四国めたん「handleStatus()のdefaultでneverを受けると漏れがすぐわかるの。」
ずんだもん「incomplete()はerrorケースを忘れて怒られてたもん。」
四国めたん「const exhaustive: never = status; って書くと型が見張ってくれる。」
ずんだもん「Color型でもassertNever()で未処理を投げられるんだね。」
四国めたん「色を追加した瞬間にビルドが落ちるのは安心。」
ずんだもん「網羅性チェックで仕様変更にもドンと構えよう。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: handleStatusの網羅性 */
type Status = "pending" | "success" | "error";

function handleStatus(status: Status): void {
  switch (status) {
    case "pending":
      console.log("保留中");
      break;
    case "success":
      console.log("成功");
      break;
    case "error":
      console.log("失敗");
      break;
    default:
      const exhaustive: never = status;
      throw new Error(`未処理: ${exhaustive}`);
  }
}

/** Example 2: ケース漏れの検知 */
function incomplete(status: Status): void {
  switch (status) {
    case "pending":
      console.log("保留中");
      break;
    case "success":
      console.log("成功");
      break;
    default:
      const exhaustive: never = status;
      throw new Error(`漏れ: ${exhaustive}`);
  }
}

/** Example 3: Color型でのassertNever */
type Color = "red" | "blue" | "green";

function assertNever(value: never): never {
  throw new Error(`Unhandled color: ${value}`);
}

function getHex(color: Color): string {
  switch (color) {
    case "red":
      return "#ff0000";
    case "blue":
      return "#0000ff";
    case "green":
      return "#00ff00";
    default:
      return assertNever(color);
  }
}
```
