# #545 「ベストプラクティス」

四国めたん「neverを活かすベストプラクティスを整理しよう。」
ずんだもん「共通ヘルパーexhaustiveCheck()やassertNever()はutilsにまとめると便利。」
四国めたん「Result<T, E>やDomainEventのように判別プロパティを必ず持たせるのがコツ。」
ずんだもん「handleEvent()はswitchで全部のtypeを処理してdefaultでexhaustiveCheckを呼んでた。」
四国めたん「サービス層でResultを返せばコントローラー側で分岐しやすい。」
ずんだもん「UserServiceがok: true/falseを返して、UserControllerが結果に応じて例外を投げてたもんね。」
四国めたん「どの層でもneverヘルパーを使って漏れを即検出しよう。」
ずんだもん「型安全なエラー処理が当たり前になるんだ。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: sharedヘルパー */
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
/** Example 3: サービスとコントローラー */
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
