# #274 「Nest.jsのDTOとboolean」

四国めたん「Nest.jsのDTOでbooleanを扱ってみましょう!」
ずんだもん「DTOはData Transfer Objectで、データの受け渡しに使うんだよね!」
四国めたん「はい。class-validatorを使って型チェックができます。」
ずんだもん「@IsBoolean()デコレータでboolean型の検証ができるんだね?」
四国めたん「その通りです。不正な値が送られてきた時にエラーを返せます。」
ずんだもん「isActiveやisAdminなど、フラグを管理するのに便利だね!」
四国めたん「Controllerで@Body()を使ってDTOを受け取ります。」
ずんだもん「型安全なAPIを作るのに重要な仕組みなのだ!」

---

## 📺 画面表示用コード

```typescript
// Nest.jsのDTOとboolean

import { IsBoolean, IsString } from 'class-validator';

export class CreateUserDto {
  @IsString()
  name: string;

  @IsBoolean()
  isActive: boolean;

  @IsBoolean()
  isAdmin: boolean;
}

@Controller('users')
export class UsersController {
  @Post()
  create(@Body() dto: CreateUserDto) {
    return { success: dto.isActive };
  }
}
```
