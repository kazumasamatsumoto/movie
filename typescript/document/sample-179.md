# #179 「回避方法(1) - 整数演算」

## 概要
TypeScript v5.9の整数演算による回避方法について学習します。小数を整数に変換して計算する方法を理解します。

## 学習目標
- 整数演算による回避方法を理解する
- 小数の整数変換を理解する
- 実用的な実装方法を理解する

## 画面表示用コード

```typescript
// 整数演算による回避
function addDecimals(a: number, b: number): number {
  const factor = 100; // 小数点以下2桁
  return (Math.round(a * factor) + Math.round(b * factor)) / factor;
}

// 実用的な例
let price1: number = 0.1;
let price2: number = 0.2;
let total: number = addDecimals(price1, price2);

console.log(total); // 0.3
console.log(total === 0.3); // true

// 金銭計算の例
let yen1: number = 100.50;
let yen2: number = 200.25;
let totalYen: number = addDecimals(yen1, yen2);
```

## 重要なポイント
1. **整数演算**: 小数を整数に変換して計算
2. **精度保持**: 計算後に元の精度に戻す
3. **実用性**: 金銭計算などに活用

## 次のステップ
次回は、回避方法(2)について学習します。
