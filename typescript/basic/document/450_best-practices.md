# #450 「ベストプラクティス」

四国めたん「void型のベストプラクティスをまとめましょう。」
ずんだもん「Angularコンポーネントではサービス呼び出しをvoidメソッドに閉じ込めるんだね。」
四国めたん「Nest.jsコントローラはPromise<void>でRESTのステータスに集中します。」
ずんだもん「RxJSではSubject<void>やdestroy$を使って終了シグナルを流すんだ?」
四国めたん「はい。ngOnDestroyでvoidのストリームを閉じます。」
ずんだもん「フロントもバックもvoidを使い分ければ設計が明瞭になる!」
四国めたん「副作用の意図を明示してメンテナンス性を高めましょう。」
ずんだもん「ベストプラクティスを実践してvoid力を高めるのだ!」

---

## 📺 画面表示用コード

```typescript
/** Example 1: Angularコンポーネント */
@Component({...})
export class UserComponent {
  onClick(): void {
    this.service.save(this.user);
  }
}

/** Example 2: Nest.jsコントローラ */
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
