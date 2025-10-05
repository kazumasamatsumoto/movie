# #084 「@IsString()デコレータ」

## 概要
TypeScript v5.9の@IsString()デコレータについて学習します。プロパティがstring型であることを検証するデコレータを理解します。

## 学習目標
- @IsString()デコレータの基本を理解する
- バリデーションの追加方法を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// @IsString()デコレータ
import { IsString, IsOptional } from 'class-validator';

export class UserDto {
  @IsString()
  name: string;

  @IsString()
  email: string;

  @IsString()
  @IsOptional()
  description?: string;
}

export class ProductDto {
  @IsString()
  name: string;

  @IsString()
  category: string;

  @IsString()
  @IsOptional()
  tags?: string;
}
```

## 重要なポイント
1. **@IsString()**: string型であることを検証
2. **@IsOptional()**: オプショナルなプロパティ
3. **バリデーション**: APIの入力検証に活用

## 次のステップ
次回は、バリデーション実例について学習します。