# #448 「API設計」

四国めたん「voidレスポンスはAPI設計でも有効です。」
ずんだもん「DELETEやPOSTで204/202を返すコントローラが紹介されてたね。」
四国めたん「deleteやsend、processはPromise<void>で完了を伝えます。」
ずんだもん「ビジネスロジックはサービス層に委譲し、HTTPステータスで結果を示すんだ?」
四国めたん「はい。レスポンスボディを空にして通信量も抑えられます。」
ずんだもん「BatchControllerみたいにキュー投入だけなら202が適切!」
四国めたん「voidを返すことでAPI利用者に『結果は不要』と示せます。」
ずんだもん「REST APIでもvoid設計を活用するのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: DELETE API */
@Controller('posts')
export class PostsController {
  @Delete(':id')
  @HttpCode(204)
  async delete(@Param('id') id: string): Promise<void> {
    await this.postsService.delete(id);
  }
}

/** Example 2: 通知送信API */
@Controller('notifications')
export class NotificationsController {
  @Post('send')
  @HttpCode(204)
  async send(@Body() dto: NotificationDto): Promise<void> {
    await this.notificationService.send(dto);
  }
}

/** Example 3: バッチ処理API */
@Controller('batch')
export class BatchController {
  @Post('process')
  @HttpCode(202)
  async process(@Body() dto: BatchDto): Promise<void> {
    await this.batchService.enqueue(dto);
  }
}
```
