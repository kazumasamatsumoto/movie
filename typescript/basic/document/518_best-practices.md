# #518 「ベストプラクティス」

四国めたん「網羅性チェックのベストプラクティスを並べてみよう。」
ずんだもん「まずはassertNever()とexhaustiveCheck()を共通化することだね。」
四国めたん「Result型のunwrap()はsuccessならvalue、失敗ならerrorを投げてた。」
ずんだもん「elseでexhaustiveCheck(result)を呼べば新しいvariantにも即対応。」
四国めたん「Actionのexecute()はswitch文でsave/load/deleteを呼び分けてたよ。」
ずんだもん「defaultでexhaustiveCheck(action)を返す統一パターンが綺麗。」
四国めたん「ヘルパーを育てればどのUnionでも同じ構造にできる。」
ずんだもん「チーム全体でベストプラクティスを共有しよう。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: ヘルパー関数 */
function assertNever(value: never, message?: string): never {
  throw new Error(message ?? `Unexpected value: ${value}`);
}

function exhaustiveCheck(value: never): never {
  return assertNever(value, "Unhandled case");
}

/** Example 2: Result型での利用 */
type Result<T, E> =
  | { success: true; value: T }
  | { success: false; error: E };

function unwrap<T, E>(result: Result<T, E>): T {
  if (result.success) return result.value;
  if (!result.success) throw result.error;
  return exhaustiveCheck(result);
}

/** Example 3: switchパターン */
type Action = "save" | "load" | "delete";

function execute(action: Action): void {
  switch (action) {
    case "save":
      return save();
    case "load":
      return load();
    case "delete":
      return remove();
    default:
      return exhaustiveCheck(action);
  }
}
```
