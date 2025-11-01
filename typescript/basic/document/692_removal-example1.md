# #692 「any排除実例①」

四国めたん「実例としてユーザーサービスのany排除を紹介します」
ずんだもん「service.getUser(id): any をunknownに変えてDTOにマップしたんだよね」
四国めたん「はい。ValidationPipeを追加したことでAPI層の型安全性が向上しました」
ずんだもん「テストもユーザDTOを基準に書き換えて再発防止できたよ」
四国めたん「小さな変更で体験が大きく改善した好例です」
ずんだもん「現場のナレッジをチームで共有しよう！」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 変更前 */
class UserService {
  async getUser(id: string): Promise<any> {
    const res = await fetch(`/users/${id}`);
    return res.json();
  }
}

/** Example 2: 変更後 */
type UserDto = { id: string; email: string };
class SafeUserService {
  async getUser(id: string): Promise<unknown> {
    const res = await fetch(`/users/${id}`);
    return res.json();
  }
}

/** Example 3: DTO変換 */
function toUserDto(value: unknown): UserDto {
  if (typeof value !== "object" || value === null) throw new TypeError("invalid");
  const record = value as Record<string, unknown>;
  return { id: String(record.id), email: String(record.email) };
}
```
