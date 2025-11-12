# #542 「DTOバリデーション」

四国めたん「DTOバリデーションでもneverが活躍するよ。」
ずんだもん「ValidationResult<T>はvalidフラグで成功/失敗を分けてたね。」
四国めたん「handleValidation()でvalidと!validを両方チェックしてcheck: never = result; を置く。」
ずんだもん「DtoTypeをcreate/updateに限定してtransformDto()で型安全に変換してたのだ。」
四国めたん「typeが増えたらconst check: never = type; が教えてくれる。」
ずんだもん「ValidationRuleもrequired/email/minLengthのUnionだったよ。」
四国めたん「applyRule()で条件ごとに処理し、最後はcheck: never = rule; で締める。」
ずんだもん「バリデーションの抜け漏れをneverで防ごう。」

---

## 📺 画面表示用コード

```typescript
/** Example 1: ValidationResult */
type ValidationResult<T> =
  | { valid: true; data: T }
  | { valid: false; errors: ValidationError[] };

function validate<T>(dto: T): ValidationResult<T> {
  const errors = validateSync(dto);
  if (errors.length === 0) return { valid: true, data: dto };
  return { valid: false, errors };
}

function handleValidation<T>(result: ValidationResult<T>): T {
  if (result.valid) return result.data;
  if (!result.valid) throw new BadRequestException(result.errors);
  const check: never = result;
  return check;
}
```

```typescript
/** Example 2: DTO変換 */
type CreateUserDto = { name: string; email: string };
type UpdateUserDto = { name?: string; email?: string };
type DtoType = "create" | "update";

function transformDto(type: DtoType, data: any): CreateUserDto | UpdateUserDto {
  if (type === "create") return plainToClass(CreateUserDto, data);
  if (type === "update") return plainToClass(UpdateUserDto, data);
  const check: never = type;
  throw new Error("Invalid DTO type");
}
```

```typescript
/** Example 3: カスタムルール */
type ValidationRule =
  | { type: "required"; field: string }
  | { type: "email"; field: string }
  | { type: "minLength"; field: string; min: number };

function applyRule(rule: ValidationRule, value: any): boolean {
  if (rule.type === "required") return value != null;
  if (rule.type === "email") return /\S+@\S+\.\S+/.test(value);
  if (rule.type === "minLength") return value.length >= rule.min;
  const check: never = rule;
  return false;
}
```
