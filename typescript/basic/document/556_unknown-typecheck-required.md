# #556 「unknownは型チェック必須」

四国めたん「unknownを使うときは必ず型チェックを通過させましょう」
ずんだもん「typeofやinstanceofを挟まないとコンパイルが止まるんだよね」
四国めたん「はい。チェック済みのブロック内でのみ安全に操作できます」
ずんだもん「Type Guardを設計すると保守性が上がるよ」
四国めたん「プロジェクトルールとして型チェックを必須にするのが推奨です」
ずんだもん「レビューでガード忘れを見つける仕組みも用意したいね」

---

## 📺 画面表示用コード

```typescript
/** Example 1: typeofチェック */
function printLength(value: unknown) {
  if (typeof value === "string") {
    console.log(value.length);
  }
}

/** Example 2: instanceofチェック */
function handleError(error: unknown) {
  if (error instanceof Error) {
    console.error(error.message);
  }
}

/** Example 3: カスタム型ガード */
function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null;
}
```
