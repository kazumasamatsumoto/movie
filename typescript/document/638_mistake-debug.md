# #638 「unknownデバッグのコツ」

四国めたん「unknownを扱うときのデバッグでは型情報をログに残すと効果的です」
ずんだもん「typeofやArray.isArrayの結果を記録して原因を絞るんだよね」
四国めたん「はい。安全なログ関数を作ってガードの漏れを検出しましょう」
ずんだもん「エラーメッセージに期待した型も含めると再発防止になるよ」
四国めたん「デバッグこそ型ガードの精度を上げるチャンスです」
ずんだもん「unknownの挙動を観察してガードを進化させよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: デバッグログ */
function debugUnknown(value: unknown) {
  console.log({
    type: typeof value,
    isArray: Array.isArray(value),
    keys: typeof value === "object" && value !== null ? Object.keys(value) : [],
  });
}

/** Example 2: 期待型を明示 */
function expectString(value: unknown): string {
  if (typeof value !== "string") {
    throw new TypeError(`expected string but got ${typeof value}`);
  }
  return value;
}

/** Example 3: ガード漏れ検出 */
function assertHasId(value: unknown): asserts value is { id: number } {
  if (typeof value !== "object" || value === null || !("id" in value)) {
    console.error("payload", value);
    throw new TypeError("id property required");
  }
}
```
