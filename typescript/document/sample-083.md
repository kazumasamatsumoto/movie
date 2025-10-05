# #083 「Nest.jsのDTOとstring型」

## 概要
TypeScript v5.9のNest.js DTOとstring型について学習します。データ転送オブジェクトでAPIの入出力データを定義する方法を理解します。

## 学習目標
- DTOの基本概念を理解する
- string型プロパティの定義方法を理解する
- バリデーションとの連携を理解する

## 画面表示用コード

```typescript
// Nest.jsのDTOとstring型
import { IsString, IsEmail } from 'class-validator';

export class CreateUserDto {
  @IsString()
  name: string;

  @IsEmail()
  email: string;

  @IsString()
  role: string;
}

export class UpdateUserDto {
  @IsString()
  name?: string;

  @IsString()
  role?: string;
}
```

## 重要なポイント
1. **DTO**: データ転送オブジェクトの定義
2. **型安全性**: string型でAPIの型安全性を確保
3. **バリデーション**: デコレータでバリデーションを追加

## 次のステップ
次回は、@IsString()デコレータについて学習します。