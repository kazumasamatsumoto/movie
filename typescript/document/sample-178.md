# #178 「丸め誤差」

## 概要
TypeScript v5.9の丸め誤差について学習します。浮動小数点数の精度制限による誤差の仕組みを理解します。

## 学習目標
- 丸め誤差の仕組みを理解する
- 精度制限の影響を理解する
- 実用的な例を理解する

## 画面表示用コード

```typescript
// 丸め誤差の例
let num1: number = 0.1;
let num2: number = 0.2;
let sum: number = num1 + num2;

console.log(sum); // 0.30000000000000004

// 実用的な例
let userAge: number = 25.5;
let productPrice: number = 1500.99;
let total: number = userAge + productPrice;

console.log(total); // 1526.4899999999998
console.log(total.toFixed(2)); // "1526.49"
```

## 重要なポイント
1. **丸め誤差**: 精度制限による誤差
2. **影響**: 計算結果が期待値と異なる
3. **対処**: toFixed()などで表示を調整

## 次のステップ
次回は、回避方法(1)について学習します。
