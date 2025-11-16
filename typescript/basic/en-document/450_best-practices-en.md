# #450 "Best Practices"

Shikoku Metan: "Let's recap void best practices."
Zundamon: "Angular components wrap service calls in void methods."
Shikoku Metan: "Nest.js controllers use Promise<void> and focus on HTTP statuses."
Zundamon: "RxJS leverages Subject<void> or destroy$ to emit completion signals?"
Shikoku Metan: "Exactly—ngOnDestroy closes those streams."
Zundamon: "Front and back ends stay clear when void is used intentionally."
Shikoku Metan: "Highlight side effects to improve maintainability."
Zundamon: "I'll follow these practices to boost my void skills!"

---

## 📺 Code for Display

```typescript
/** Example 1: Angular component */
@Component({...})
export class UserComponent {
  onClick(): void {
    this.service.save(this.user);
  }
}

/** Example 2: Nest controller */
@Controller('users')
export class UsersController {
  @Delete(':id')
  @HttpCode(204)
  async delete(@Param('id') id: string): Promise<void> {
    await this.usersService.delete(id);
  }
}

/** Example 3: RxJS Observable */
private destroy$ = new Subject<void>();
ngOnDestroy(): void {
  this.destroy$.next();
  this.destroy$.complete();
}
```
