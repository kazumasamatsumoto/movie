# #632 「ValidationPipeで型安全に」

四国めたん「ValidationPipeを使えばunknownなリクエストも安全に扱えます」
ずんだもん「class-transformerでDTOに変換したあとclass-validatorで検証するんだね」
四国めたん「はい。anyではなくunknownからDTOへ段階的に絞り込みます」
ずんだもん「Nestのグローバルパイプで一括適用できるのが便利だよ」
四国めたん「pipeで検証すればハンドラは確実な型で受け取れます」
ずんだもん「ValidationPipeを標準にして型安全なAPIを守ろう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: DTO定義 */
export class CreateUserDto {
  @IsEmail()
  email!: string;

  @IsString()
  name!: string;
}

/** Example 2: グローバルパイプ */
app.useGlobalPipes(new ValidationPipe({ whitelist: true, transform: true }));

/** Example 3: コントローラで安全受取 */
@Post("users")
create(@Body() dto: CreateUserDto) {
  return this.service.create(dto);
}
```
