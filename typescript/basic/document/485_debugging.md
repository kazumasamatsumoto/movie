# #485 「デバッグ」

四国めたん「never関数にもデバッグ手法を仕込んでおきましょう。」
ずんだもん「failでcontextやconsole.traceを出していた!」
四国めたん「DEBUGフラグで詳細を出すassertNeverも便利です。」
ずんだもん「throw前にdebuggerを置くテクも紹介されてたね。」
四国めたん「戻らない処理こそ情報を残しておくべきです。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: デバッグログ付きエラー */
function fail(message: string, context?: unknown): never {
  console.error("Error context:", context);
  console.trace();
  throw new Error(message);
}

/** Example 2: 条件付きデバッグ */
const DEBUG = true;
function assertNever(value: never): never {
  if (DEBUG) {
    console.error("Unexpected value:", value);
  }
  throw new Error(`Unhandled case: ${value}`);
}

/** Example 3: debugger停止 */
function throwError(message: string): never {
  debugger;
  throw new Error(message);
}
```
