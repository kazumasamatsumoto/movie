# #185 「金銭計算の注意点」

## 概要
TypeScript v5.9の金銭計算の注意点について学習します。浮動小数点数の精度問題を避けるための注意点を理解します。

## 学習目標
- 金銭計算の注意点を理解する
- 精度問題の回避方法を理解する
- 実用的な実装方法を理解する

## 画面表示用コード

```typescript
// 金銭計算の注意点
function calculatePrice(price: number, tax: number): number {
  // 整数演算で精度を保つ
  const factor = 100;
  const priceInt = Math.round(price * factor);
  const taxInt = Math.round(tax * factor);
  const totalInt = priceInt + taxInt;
  
  return totalInt / factor;
}

// 実用的な例
let productPrice: number = 100.50;
let tax: number = 8.25;
let total: number = calculatePrice(productPrice, tax);

console.log(total); // 108.75
console.log(total.toFixed(2)); // "108.75"
```

## 重要なポイント
1. **整数演算**: 小数を整数に変換して計算
2. **精度保持**: 計算後に元の精度に戻す
3. **実用性**: 金銭計算の正確性を保つ

## 次のステップ
次回は、BigIntの紹介について学習します。
