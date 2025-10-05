# #085 「バリデーション実例」

## 概要
TypeScript v5.9のバリデーション実例について学習します。実際のAPIでstring型のバリデーションを行う例を理解します。

## 学習目標
- 実践的なバリデーション例を理解する
- 複数のバリデーションの組み合わせを理解する
- エラーハンドリングを理解する

## 画面表示用コード

```typescript
// バリデーション実例
import { IsString, IsNotEmpty, Length, IsEmail } from 'class-validator';

export class CreateUserDto {
  @IsString()
  @IsNotEmpty()
  @Length(1, 50)
  name: string;

  @IsString()
  @IsEmail()
  email: string;

  @IsString()
  @IsNotEmpty()
  @Length(3, 20)
  username: string;
}

export class UpdateProfileDto {
  @IsString()
  @IsOptional()
  @Length(0, 200)
  bio?: string;
}
```

## 重要なポイント
1. **複数バリデーション**: 複数のデコレータを組み合わせ
2. **@Length()**: 文字列の長さを検証
3. **@IsNotEmpty()**: 空文字列でないことを検証

## 次のステップ
次回は、間違い(1)について学習します。