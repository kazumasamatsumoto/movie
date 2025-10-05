# #177 「精度問題 - 0.1 + 0.2」

## 概要
TypeScript v5.9の精度問題について学習します。0.1 + 0.2が0.3にならない問題の原因と影響を理解します。

## 学習目標
- 精度問題の原因を理解する
- IEEE 754の制限を理解する
- 実用的な影響を理解する

## 画面表示用コード

```typescript
// 精度問題の例
let num1: number = 0.1;
let num2: number = 0.2;
let sum: number = num1 + num2;

console.log(sum); // 0.30000000000000004
console.log(sum === 0.3); // false

// 実用的な例
let price1: number = 0.1;
let price2: number = 0.2;
let total: number = price1 + price2;

console.log(total); // 0.30000000000000004
console.log(total === 0.3); // false
```

## 重要なポイント
1. **精度問題**: 0.1 + 0.2 ≠ 0.3
2. **原因**: IEEE 754の浮動小数点表現
3. **影響**: 数値比較で予期しない結果

## 次のステップ
次回は、丸め誤差について学習します。
