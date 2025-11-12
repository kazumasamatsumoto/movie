# #541 「型安全なエラーハンドリング」

四国めたん「ResultやEitherでエラーを型安全に扱おう。」
ずんだもん「Result<T, E>はokフラグで成功と失敗を分けてたね。」
四国めたん「divide()はゼロ割なら{ ok: false }、それ以外は値を返してた。」
ずんだもん「handleResult()でresult.okを二段階でチェックしてconst check: neverを置くのだ。」
四国めたん「Either<L, R>ではtype: 'left' | 'right'でJSONパースの結果を表してた。」
ずんだもん「parseJson()は成功ならright、失敗ならleftにErrorを入れてたよ。」
四国めたん「AppErrorのhandleError()もvalidation/network/businessを全部網羅してた。」
ずんだもん「unknownなエラーはneverチェックで即座に検知できるね。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Result型でdivide */
type Result<T, E> =
  | { ok: true; value: T }
  | { ok: false; error: E };

function divide(a: number, b: number): Result<number, string> {
  if (b === 0) return { ok: false, error: "Division by zero" };
  return { ok: true, value: a / b };
}

function handleResult(result: Result<number, string>): number {
  if (result.ok) return result.value;
  if (!result.ok) throw new Error(result.error);
  const check: never = result;
  return check;
}
```

```typescript
/** Example 2: Either型 */
type Either<L, R> =
  | { type: "left"; value: L }
  | { type: "right"; value: R };

function parseJson<T>(json: string): Either<Error, T> {
  try {
    return { type: "right", value: JSON.parse(json) };
  } catch (e) {
    return { type: "left", value: e as Error };
  }
}
```

```typescript
/** Example 3: AppErrorの処理 */
type AppError =
  | { type: "validation"; field: string }
  | { type: "network"; code: number }
  | { type: "business"; message: string };

function handleError(error: AppError): string {
  if (error.type === "validation") return `Invalid: ${error.field}`;
  if (error.type === "network") return `HTTP ${error.code}`;
  if (error.type === "business") return error.message;
  const check: never = error;
  return "Unknown error";
}
```
