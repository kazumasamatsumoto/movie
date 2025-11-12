# #545 "Best Practices"

Shikoku Metan: "Let's collect never-driven best practices."
Zundamon: "Shared helpers like exhaustiveCheck() and assertNever() belong in utils."
Shikoku Metan: "Always give discriminated unions a type/kind/success flag."
Zundamon: "handleEvent() switched on event.type and defaulted to exhaustiveCheck."
Shikoku Metan: "Returning Result<T, E> from services lets controllers branch safely."
Zundamon: "UserService returned success true/false, and UserController threw exceptions accordingly."
Shikoku Metan: "Use never helpers at every layer to catch leaks fast."
Zundamon: "Make type-safe error handling the norm."

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
/** Example 3: Service + controller */
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
