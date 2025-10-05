# #136 「加算演算子 - a + b」

## 概要
TypeScript v5.9の加算演算子について学習します。数値を足し算する+演算子の基本的な使用方法を理解します。

## 学習目標
- 加算演算子の基本を理解する
- 数値の足し算方法を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// 加算演算子
let a: number = 10;
let b: number = 20;
let sum: number = a + b; // 30

// 実用的な例
let price: number = 1000;
let tax: number = 100;
let total: number = price + tax; // 1100

let userAge: number = 25;
let yearsToAdd: number = 5;
let futureAge: number = userAge + yearsToAdd; // 30
```

## 重要なポイント
1. **足し算**: 2つの数値を足し算
2. **結果**: 数値同士の加算は数値になる
3. **実用性**: 計算処理やデータ処理に活用

## 次のステップ
次回は、加算の型推論について学習します。