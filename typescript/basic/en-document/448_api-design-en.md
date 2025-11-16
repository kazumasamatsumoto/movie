# #448 "API Design"

Shikoku Metan: "Void responses are part of good API design."
Zundamon: "We saw DELETE/POST endpoints returning 204 or 202."
Shikoku Metan: "delete, send, and process use Promise<void> to signal completion."
Zundamon: "Business logic lives in services while HTTP status conveys the result?"
Shikoku Metan: "Exactly, and empty bodies save bandwidth."
Zundamon: "BatchController enqueues work and returns 202 appropriately."
Shikoku Metan: "Returning void tells clients no payload is expected."
Zundamon: "I'll apply void semantics across REST APIs!"

---

## 📺 Code for Display

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

/** Example 2: Notification API */
@Controller('notifications')
export class NotificationsController {
  @Post('send')
  @HttpCode(204)
  async send(@Body() dto: NotificationDto): Promise<void> {
    await this.notificationService.send(dto);
  }
}

/** Example 3: Batch API */
@Controller('batch')
export class BatchController {
  @Post('process')
  @HttpCode(202)
  async process(@Body() dto: BatchDto): Promise<void> {
    await this.batchService.enqueue(dto);
  }
}
```
