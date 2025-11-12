# #549 "Best Practices"

Shikoku Metan: "Let's recap never-focused best practices."
Zundamon: "utils/exhaustive.ts centralizes exhaustiveCheck() and assertNever()."
Shikoku Metan: "Shared helpers keep every layer consistent."
Zundamon: "Result<T, E> and DomainEvent always include discriminants."
Shikoku Metan: "Default branches call exhaustiveCheck(event, 'handleEvent')."
Zundamon: "Services returning Result let controllers branch cleanly."
Shikoku Metan: "UserController.getUser() ends with exhaustiveCheck(result) as a last resort."
Zundamon: "Share these helpers across the team."

---

## 📺 Code for Display

```typescript
/** Example 1: Shared helpers */
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
/** Example 2: Discriminated unions */
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
/** Example 3: Service usage */
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
