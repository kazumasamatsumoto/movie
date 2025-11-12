# #478 「Error型」

四国めたん「neverとError型の関係も押さえましょう。」
ずんだもん「fail(message)は常にErrorを投げていたね。」
四国めたん「TypeErrorやRangeErrorを投げることで原因を明示できます。」
ずんだもん「validate関数ではErrorを作ってstackをログに出していた!」
四国めたん「適切なエラー型でneverを返すとデバッグが楽になります。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Error型の基礎 */
function fail(message: string): never {
  throw new Error(message);
}

/** Example 2: サブクラス */
function invalidType(value: unknown): never {
  throw new TypeError(`Invalid type: ${typeof value}`);
}
function outOfRange(value: number): never {
  throw new RangeError(`Value ${value} is out of range`);
}

/** Example 3: スタックトレース */
function validate(data: unknown): never {
  const error = new Error("Validation failed");
  console.error(error.stack);
  throw error;
}
```
