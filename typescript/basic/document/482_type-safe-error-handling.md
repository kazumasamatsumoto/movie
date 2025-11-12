# #482 「型安全なエラーハンドリング」

四国めたん「neverを使うと型安全にエラーを扱えます。」
ずんだもん「processDataはnullならthrowErrorしてたね。」
四国めたん「カスタムエラーで詳細を持たせることもできます。」
ずんだもん「ensure関数でnullを省けていた!」
四国めたん「エラー処理と型絞り込みを同時にこなせます。」
ずんだもん「型安全なエラー設計をneverで実践するのだ!"

---

## 📺 画面表示用コード

```typescript
/** Example 1: 型安全なエラー処理 */
function processData(data: string | null): string {
  if (data === null) {
    throwError("Data is null");
  }
  return data.toUpperCase();
}
function throwError(message: string): never {
  throw new Error(message);
}

/** Example 2: カスタムエラー */
class InvalidDataError extends Error {
  constructor(public data: unknown) {
    super("Invalid data");
  }
}
function validateData(data: unknown): never {
  throw new InvalidDataError(data);
}

/** Example 3: 型の絞り込み */
function ensure<T>(value: T | null, message: string): T {
  if (value === null) {
    throwError(message);
  }
  return value;
}
```
