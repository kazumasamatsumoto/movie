# #633 「型安全なAPI設計」

四国めたん「型安全なAPI設計ではDTOと型ガードをセットで考えます」
ずんだもん「Nest.jsなら入出力の両方に型を定義できるね」
四国めたん「はい。unknown境界→ValidationPipe→DTO→サービスと流れを作ります」
ずんだもん「レスポンスも型を返せばフロントが安心だよ」
四国めたん「API契約をTypeScriptの型で表現するのが理想です」
ずんだもん「型安全な設計でバックエンドとフロントの齟齬を減らそう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: API契約型 */
type UserResponse = { id: number; email: string };

/** Example 2: サービス層 */
createUser(dto: CreateUserDto): Promise<UserResponse> {
  return this.repo.save(dto);
}

/** Example 3: コントローラの戻り値型 */
@Post("users")
async create(@Body() dto: CreateUserDto): Promise<UserResponse> {
  return this.service.createUser(dto);
}
```
