# #275 「@IsBoolean()デコレータ」

四国めたん「@IsBoolean()デコレータについて学びましょう!」
ずんだもん「class-validatorのデコレータで、boolean型を検証できるんだね!」
四国めたん「はい。DTOのプロパティに付けることで自動的にチェックされます。」
ずんだもん「@IsOptional()と組み合わせると、オプショナルなプロパティも作れるよね?」
四国めたん「その通りです。省略可能なフラグを定義できます。」
ずんだもん「文字列の'true'が送られてきたらエラーになるんだね!」
四国めたん「厳密な型チェックにより、不正なデータを事前に防げます。」
ずんだもん「バリデーションエラーメッセージも自動で生成されるから便利なのだ!」

---

## 📺 画面表示用コード

```typescript
// @IsBoolean()デコレータ

import { IsBoolean, IsOptional } from 'class-validator';

export class UpdateSettingsDto {
  @IsBoolean()
  emailNotification: boolean;

  @IsBoolean()
  @IsOptional()
  pushNotification?: boolean;
}

// バリデーション成功例
const valid = { emailNotification: true };

// バリデーション失敗例
const invalid = { emailNotification: 'true' }; // エラー
```
