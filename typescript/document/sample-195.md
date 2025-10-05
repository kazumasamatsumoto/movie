# #195 「数値範囲のバリデーション」

## 概要
TypeScript v5.9の数値範囲のバリデーションについて学習します。数値が指定した範囲内かどうかを検証する方法を理解します。

## 学習目標
- 数値範囲のバリデーション方法を理解する
- @Min、@Max、@Rangeデコレータを理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// 数値範囲のバリデーション
import { IsNumber, Min, Max, Range } from 'class-validator';

export class ProductDto {
  @IsNumber()
  @Min(0)
  @Max(1000000)
  price: number;

  @IsNumber()
  @Min(1)
  @Max(1000)
  quantity: number;

  @IsNumber()
  @Range(0, 100)
  discount: number;
}

// 実用的な例
export class UserDto {
  @IsNumber()
  @Min(0)
  @Max(120)
  age: number;

  @IsNumber()
  @Min(0)
  salary: number;
}
```

## 重要なポイント
1. **@Min/@Max**: 数値の最小値・最大値チェック
2. **@Range**: 数値の範囲チェック
3. **実用性**: データの整合性を保つ

## 次のステップ
次回は、間違い(1)について学習します。
