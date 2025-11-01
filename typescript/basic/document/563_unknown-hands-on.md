# #563 「unknown実践例」

四国めたん「unknownを活用した実践例を見てみましょう」
ずんだもん「APIレスポンスを検証しながらDTOに落とし込む流れが良いね」
四国めたん「型ガードとアサーションを組み合わせて信頼できるデータにします」
ずんだもん「ログ用にunknownのまま残すのも安全だよ」
四国めたん「異常系ではエラーとしてラップして返すのがポイントです」
ずんだもん「実装に組み込めば型安全な境界が作れるね！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: DTO変換 */
type UserDto = { id: number; name: string };
function toUserDto(input: unknown): UserDto | null {
  if (typeof input === "object" && input !== null && "id" in input && "name" in input) {
    const record = input as Record<string, unknown>;
    if (typeof record.id === "number" && typeof record.name === "string") {
      return { id: record.id, name: record.name };
    }
  }
  return null;
}

/** Example 2: ログを残す */
function logUnknown(value: unknown) {
  console.log("raw payload", value);
}

/** Example 3: エラーラップ */
function ensureUser(input: unknown): UserDto {
  const user = toUserDto(input);
  if (!user) throw new TypeError("Invalid user");
  return user;
}
```
