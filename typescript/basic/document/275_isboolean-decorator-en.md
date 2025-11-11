# #275 "@IsBoolean() Decorator"

Shikoku Metan: "Let's learn about the @IsBoolean() decorator!"
Zundamon: "It's a class-validator decorator that validates boolean types!"
Shikoku Metan: "That's right. By adding it to DTO properties, they're automatically checked."
Zundamon: "Combined with @IsOptional(), we can create optional properties too, right?"
Shikoku Metan: "Exactly. We can define optional flags."
Zundamon: "If the string 'true' is sent, it becomes an error!"
Shikoku Metan: "Strict type checking prevents invalid data in advance."
Zundamon: "Validation error messages are automatically generated, so convenient!"

---

## 📺 Code for Display

```typescript
// @IsBoolean() decorator

import { IsBoolean, IsOptional } from 'class-validator';

export class UpdateSettingsDto {
  @IsBoolean()
  emailNotification: boolean;

  @IsBoolean()
  @IsOptional()
  pushNotification?: boolean;
}

// Validation success example
const valid = { emailNotification: true };

// Validation failure example
const invalid = { emailNotification: 'true' }; // Error
```
