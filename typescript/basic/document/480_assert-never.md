# #480 「assertNever関数」

四国めたん「最後にassertNever関数を押さえましょう。」
ずんだもん「unexpectedケースで必ずthrowするやつだね。」
四国めたん「handleStatusやgetColorで網羅性を保証していました。」
ずんだもん「Colorに新しい値を追加したら型エラーで気付ける!」
四国めたん「neverによる最終防衛ラインとして常備しておきましょう。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: assertNever定義 */
function assertNever(value: never): never {
  throw new Error(`Unexpected value: ${value}`);
}

/** Example 2: ステータス処理 */
type Status = "pending" | "success" | "error";
function handleStatus(status: Status): void {
  switch (status) {
    case "pending":
      console.log("Pending");
      break;
    case "success":
      console.log("Success");
      break;
    case "error":
      console.log("Error");
      break;
    default:
      assertNever(status);
  }
}

/** Example 3: 型追加時の検出 */
type Color = "red" | "blue" | "green";
function getColor(color: Color): string {
  switch (color) {
    case "red": return "#ff0000";
    case "blue": return "#0000ff";
    default: return assertNever(color);
  }
}
```
