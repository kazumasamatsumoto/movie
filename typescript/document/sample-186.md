# #186 「BigIntの紹介」

## 概要
TypeScript v5.9のBigIntについて学習します。任意精度の整数を扱える型の基本的な使用方法を理解します。

## 学習目標
- BigIntの基本を理解する
- 任意精度の整数を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// BigIntの紹介
let bigInt1: bigint = 123456789012345678901234567890n;
let bigInt2: bigint = BigInt("123456789012345678901234567890");

// 演算
let sum: bigint = bigInt1 + bigInt2;
let product: bigint = bigInt1 * bigInt2;

// 実用的な例
let largeId: bigint = 1234567890123456789n;
let userId: bigint = BigInt("9876543210987654321");

console.log(largeId.toString());
console.log(userId.toString());
```

## 重要なポイント
1. **任意精度**: number型の制限を超える大きな整数
2. **nサフィックス**: 数値リテラルにnを付与
3. **実用性**: 大きな数値の計算に活用

## 次のステップ
次回は、BigIntとnumberの違いについて学習します。
