# #446 「Nest.jsコントローラ」

四国めたん「Nest.jsのコントローラでもPromise<void>がよく使われます。」
ずんだもん「UsersController.deleteは@HttpCode(204)で戻り値なしだったね。」
四国めたん「POSTやPUTでも副作用だけならPromise<void>にします。」
ずんだもん「HTTPステータスで結果を伝えて、ボディは空にするんだ?」
四国めたん「はい。RESTのベストプラクティスです。」
ずんだもん「void戻り値でAPI設計が明確になるね。」
四国めたん「副作用を伴うエンドポイントはPromise<void>で統一しましょう。」
ずんだもん「Nest.jsコントローラもvoid設計を徹底するのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: DELETEコントローラ */
@Controller('users')
export class UsersController {
  @Delete(':id')
  @HttpCode(204)
  async delete(@Param('id') id: string): Promise<void> {
    await this.usersService.delete(id);
  }
}

/** Example 2: POSTでのvoid */
@Controller('notifications')
export class NotificationsController {
  @Post('send')
  @HttpCode(204)
  async send(@Body() dto: SendDto): Promise<void> {
    await this.notificationService.send(dto);
  }
}

/** Example 3: PUT更新 */
@Put(':id')
@HttpCode(204)
async update(@Param('id') id: string, @Body() dto: UpdateDto): Promise<void> {
  await this.service.update(id, dto);
}
```
