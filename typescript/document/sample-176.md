# #176 「IEEE 754とは」

## 概要
TypeScript v5.9のIEEE 754について学習します。浮動小数点数の標準規格の特徴と制限を理解します。

## 学習目標
- IEEE 754の基本を理解する
- 浮動小数点数の特徴を理解する
- 特殊な値（NaN、Infinity）を理解する

## 画面表示用コード

```typescript
// IEEE 754の特徴
let num1: number = 0.1;
let num2: number = 0.2;
let sum: number = num1 + num2;

console.log(sum); // 0.30000000000000004

// 特殊な値
let infinity: number = Infinity;
let negativeInfinity: number = -Infinity;
let notANumber: number = NaN;

console.log(Number.isFinite(infinity)); // false
console.log(Number.isNaN(notANumber)); // true
```

## 重要なポイント
1. **標準規格**: 浮動小数点数の国際標準
2. **精度問題**: 0.1 + 0.2 ≠ 0.3
3. **特殊な値**: NaN、Infinity、-Infinity

## 次のステップ
次回は、精度問題について学習します。
