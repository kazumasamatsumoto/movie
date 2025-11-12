# #479 「カスタムエラー」

四国めたん「カスタムエラーを使うとnever関数の意図が伝わります。」
ずんだもん「ValidationErrorやNotFoundErrorを投げる例があったね。」
四国めたん「フィールド情報やIDを持たせることでデバッグできます。」
ずんだもん「neverを返すバリデーション関数にピッタリ!」
四国めたん「エラー設計も型の一部だと意識しましょう。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: カスタムエラー定義 */
class ValidationError extends Error {
  constructor(public field: string, message: string) {
    super(message);
    this.name = "ValidationError";
  }
}

/** Example 2: カスタムエラーを投げる */
function validateAge(age: number): never {
  throw new ValidationError("age", "Age must be positive");
}

/** Example 3: 複数のエラー */
class NotFoundError extends Error {
  constructor(public id: string) {
    super(`Resource ${id} not found`);
    this.name = "NotFoundError";
  }
}
function findUser(id: string): never {
  throw new NotFoundError(id);
}
```
