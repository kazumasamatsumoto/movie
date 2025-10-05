# #194 「@IsNumber()デコレータ」

## 概要
TypeScript v5.9の@IsNumber()デコレータについて学習します。数値型のバリデーションを行うデコレータの使用方法を理解します。

## 学習目標
- @IsNumber()デコレータの基本を理解する
- 数値バリデーションの仕組みを理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// @IsNumber()デコレータ
import { IsNumber, IsOptional } from 'class-validator';

export class ProductDto {
  @IsNumber()
  id: number;

  @IsNumber()
  price: number;

  @IsOptional()
  @IsNumber()
  discount?: number;
}

// 実用的な例
export class UserDto {
  @IsNumber()
  age: number;

  @IsNumber()
  salary: number;

  @IsOptional()
  @IsNumber()
  bonus?: number;
}
```

## 重要なポイント
1. **@IsNumber**: 数値型のバリデーション
2. **@IsOptional**: オプショナルなプロパティ
3. **実用性**: APIの型安全性を保つ

## 次のステップ
次回は、数値範囲のバリデーションについて学習します。
