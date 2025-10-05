# #146 「べき乗演算子 - a ** b」

## 概要
TypeScript v5.9のべき乗演算子について学習します。数値のべき乗を計算する**演算子の基本的な使用方法を理解します。

## 学習目標
- べき乗演算子の基本を理解する
- 数値のべき乗計算方法を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// べき乗演算子
let base: number = 2;
let exponent: number = 3;
let result: number = base ** exponent; // 8

// 実用的な例
let side: number = 5;
let area: number = side ** 2; // 25 (正方形の面積)

let rate: number = 1.1;
let years: number = 3;
let finalAmount: number = 1000 * (rate ** years); // 複利計算
```

## 重要なポイント
1. **べき乗**: 底と指数を指定してべき乗を計算
2. **結果**: 数値同士のべき乗演算は数値になる
3. **実用性**: 数学計算やデータ処理に活用

## 次のステップ
次回は、べき乗の型推論について学習します。

