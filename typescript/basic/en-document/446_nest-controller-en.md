# #446 "Nest.js Controllers"

Shikoku Metan: "Promise<void> is common inside Nest.js controllers."
Zundamon: "UsersController.delete returned Promise<void> with @HttpCode(204)."
Shikoku Metan: "POST or PUT endpoints do the same when they only cause side effects."
Zundamon: "So we communicate outcome via HTTP status while leaving the body empty?"
Shikoku Metan: "Exactly—classic REST style."
Zundamon: "Void responses make API intent clear."
Shikoku Metan: "Use Promise<void> consistently for side-effect endpoints."
Zundamon: "I'll enforce void-oriented Nest controllers!"

---

## 📺 Code for Display

```typescript
/** Example 1: DELETE controller */
@Controller('users')
export class UsersController {
  @Delete(':id')
  @HttpCode(204)
  async delete(@Param('id') id: string): Promise<void> {
    await this.usersService.delete(id);
  }
}

/** Example 2: POST example */
@Controller('notifications')
export class NotificationsController {
  @Post('send')
  @HttpCode(204)
  async send(@Body() dto: SendDto): Promise<void> {
    await this.notificationService.send(dto);
  }
}

/** Example 3: PUT update */
@Put(':id')
@HttpCode(204)
async update(@Param('id') id: string, @Body() dto: UpdateDto): Promise<void> {
  await this.service.update(id, dto);
}
```
