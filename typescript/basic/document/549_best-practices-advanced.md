# #549 「ベストプラクティス」

四国めたん「never運用のベストプラクティスをおさらいしよう。」
ずんだもん「utils/exhaustive.tsにexhaustiveCheck()とassertNever()をまとめてたね。」
四国めたん「共通ヘルパーを用意すればどの層でも表記が揃うの。」
ずんだもん「Result<T, E>やDomainEventには必ず判別プロパティを持たせていた。」
四国めたん「switchやifチェーンのdefaultでexhaustiveCheck(event, 'handleEvent')を呼ぶのが定番。」
ずんだもん「サービス層ではResultを返してコントローラー側で分岐させてたよ。」
四国めたん「UserController.getUser()の最後でもexhaustiveCheck(result)が番をしてる。」
ずんだもん「チーム全体で同じヘルパーとパターンを共有しよう。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: 共通ヘルパー */
export function exhaustiveCheck(value: never, context?: string): never {
  const msg = context
    ? `Unhandled case in ${context}: ${JSON.stringify(value)}`
    : `Unhandled case: ${JSON.stringify(value)}`;
  throw new Error(msg);
}

export function assertNever(value: never): never {
  throw new Error(`Unexpected value: ${value}`);
}
```

```typescript
/** Example 2: 判別Union */
type Result<T, E> =
  | { success: true; value: T }
  | { success: false; error: E };

type DomainEvent =
  | { type: "UserCreated"; userId: string }
  | { type: "UserUpdated"; userId: string; data: any };

function handleEvent(event: DomainEvent): void {
  switch (event.type) {
    case "UserCreated":
      return this.onCreate(event);
    case "UserUpdated":
      return this.onUpdate(event);
    default:
      return exhaustiveCheck(event, "handleEvent");
  }
}
```

```typescript
/** Example 3: サービス層の活用 */
@Injectable()
export class UserService {
  async getUser(id: string): Promise<Result<User, UserError>> {
    try {
      const user = await this.repository.findById(id);
      if (!user) return { success: false, error: { type: "notfound", id } };
      return { success: true, value: user };
    } catch (e) {
      return { success: false, error: { type: "internal", message: e.message } };
    }
  }
}

@Controller("users")
export class UserController {
  @Get(":id")
  async getUser(@Param("id") id: string): Promise<UserDto> {
    const result = await this.service.getUser(id);

    if (result.success) return this.toDto(result.value);
    if (!result.success && result.error.type === "notfound") throw new NotFoundException();
    if (!result.success && result.error.type === "internal") throw new InternalServerErrorException();
    return exhaustiveCheck(result, "UserController.getUser");
  }
}
```
