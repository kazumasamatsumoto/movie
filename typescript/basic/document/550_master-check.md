# #550 「マスターチェック」

四国めたん「最後はneverのマスター確認だよ。」
ずんだもん「Law1〜4でUnion/Intersection/Exclude/Extractの基本法則を再確認したね。」
四国めたん「neverReturn()を呼ぶとunreachable: neverにしか代入できないのもポイント。」
ずんだもん「Statusのhandle()はpending/success/errorをすべて処理してexhaustiveCheck(status)に渡してた。」
四国めたん「Result<T, E>やApiResponse<T>のUnionもエラー処理の定番だね。」
ずんだもん「unwrap()やhandleResponse()で最後にconst check: never = result; を置けばミスに気付ける。」
四国めたん「マスターパターンを覚えればnever設計は怖くない。」
ずんだもん「仕様変更が来ても型が守ってくれるのだ。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 基本法則のおさらい */
type Law1 = string | never;              // string
type Law2 = string & never;              // never
type Law3 = Exclude<string, never>;      // string
type Law4 = Extract<never, string>;      // never

function neverReturn(): never {
  throw new Error();
}

const unreachable: never = neverReturn();
```

```typescript
/** Example 2: 網羅性チェック */
type Status = "pending" | "success" | "error";

function exhaustiveCheck(value: never): never {
  throw new Error(`Unhandled: ${value}`);
}

function handle(status: Status): string {
  if (status === "pending") return "処理中";
  if (status === "success") return "成功";
  if (status === "error") return "エラー";
  return exhaustiveCheck(status);
}
```

```typescript
/** Example 3: 型安全なパターン */
type Result<T, E> =
  | { ok: true; value: T }
  | { ok: false; error: E };

type ApiResponse<T> =
  | { status: "success"; data: T }
  | { status: "error"; error: string };

function unwrap<T, E>(result: Result<T, E>): T {
  if (result.ok) return result.value;
  if (!result.ok) throw result.error;
  const check: never = result;
  return check;
}
```
