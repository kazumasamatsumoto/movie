# #138 「減算演算子」

## 概要
TypeScript v5.9の減算演算子について学習します。数値を引き算する-演算子の基本的な使用方法を理解します。

## 学習目標
- 減算演算子の基本を理解する
- 数値の引き算方法を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// 減算演算子
let a: number = 30;
let b: number = 10;
let difference: number = a - b; // 20

// 実用的な例
let totalPrice: number = 1200;
let discount: number = 200;
let finalPrice: number = totalPrice - discount; // 1000

let currentYear: number = 2024;
let birthYear: number = 1990;
let age: number = currentYear - birthYear; // 34
```

## 重要なポイント
1. **引き算**: 2つの数値を引き算
2. **結果**: 数値同士の減算は数値になる
3. **実用性**: 計算処理やデータ処理に活用

## 次のステップ
次回は、減算の型推論について学習します。