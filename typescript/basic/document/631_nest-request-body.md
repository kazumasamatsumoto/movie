# #631 「Nest.jsリクエストボディのunknown扱い」

四国めたん「Nest.jsでもリクエストボディはunknownとして扱うのが安全です」
ずんだもん「@Body() data: anyって書くと型チェックがなくなるんだよね」
四国めたん「はい。DTOやValidationPipeに渡す前はunknownで受け止めましょう」
ずんだもん「まずはguardとtransformで期待する型に変換するんだね」
四国めたん「そうです。フレームワークでも型安全な境界を意識するのが大切です」
ずんだもん「Nestのリクエスト処理にunknown思想を取り入れよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Controllerでunknown受け取り */
@Post("users")
createUser(@Body() payload: unknown) {
  return this.service.create(payload);
}

/** Example 2: サービス側でガード */
isCreateUserDto(payload: unknown): payload is CreateUserDto {
  return typeof payload === "object" && payload !== null && "email" in payload;
}

/** Example 3: 変換処理 */
create(payload: unknown) {
  if (!isCreateUserDto(payload)) throw new BadRequestException();
  return this.repo.save(payload);
}
```
