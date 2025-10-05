# #193 「Nest.jsのDTOとnumber型」

## 概要
TypeScript v5.9のNest.jsのDTOとnumber型について学習します。Nest.jsのDTOでnumber型を定義する方法を理解します。

## 学習目標
- Nest.jsのDTOでのnumber型定義を理解する
- class-validatorの使用方法を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// Nest.jsのDTOとnumber型
import { IsNumber, IsOptional, Min, Max } from 'class-validator';
import { Transform } from 'class-transformer';

export class CreateProductDto {
  @IsNumber()
  @Min(0)
  price: number;

  @IsNumber()
  @Min(1)
  quantity: number;

  @IsOptional()
  @IsNumber()
  @Min(0)
  @Max(100)
  discount?: number;
}

// 実用的な例
export class UpdateUserDto {
  @IsNumber()
  @Min(0)
  @Max(120)
  age: number;
}
```

## 重要なポイント
1. **@IsNumber**: 数値型のバリデーション
2. **@Min/@Max**: 数値の範囲チェック
3. **実用性**: APIの型安全性を保つ

## 次のステップ
次回は、@IsNumber()デコレータについて学習します。
