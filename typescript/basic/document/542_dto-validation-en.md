# #542 "DTO Validation"

Shikoku Metan: "Never helps keep DTO validation exhaustive."
Zundamon: "ValidationResult<T> split success and failure via valid."
Shikoku Metan: "handleValidation() checks both branches then hits check: never = result;."
Zundamon: "transformDto() accepted only create/update DTO types."
Shikoku Metan: "Adding a new type would break at const check: never = type;."
Zundamon: "ValidationRule listed required/email/minLength."
Shikoku Metan: "applyRule() handles each case before check: never = rule;."
Zundamon: "Let never guard your validation logic."

---

## 📺 Code for Display

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
/** Example 2: DTO transformation */
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
/** Example 3: Custom rules */
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
