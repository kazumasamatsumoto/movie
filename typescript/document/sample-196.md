# #196 「間違い(1) - 浮動小数点比較」

## 概要
TypeScript v5.9の浮動小数点比較の間違いについて学習します。===で浮動小数点数を直接比較する間違いを理解します。

## 学習目標
- 浮動小数点比較の間違いを理解する
- 精度問題の影響を理解する
- 適切な比較方法を理解する

## 画面表示用コード

```typescript
// 間違い(1) - 浮動小数点比較
let num1: number = 0.1 + 0.2;
let num2: number = 0.3;

// ❌ 間違い
console.log(num1 === num2); // false

// ✅ 正しい方法
function isEqual(a: number, b: number): boolean {
  return Math.abs(a - b) < 1e-10;
}

console.log(isEqual(num1, num2)); // true

// 実用的な例
let price1: number = 100.50;
let price2: number = 100.50;
console.log(isEqual(price1, price2)); // true
```

## 重要なポイント
1. **間違い**: ===で浮動小数点数を直接比較
2. **問題**: 精度問題で期待した結果にならない
3. **解決**: イプシロン比較を使用

## 次のステップ
次回は、間違い(2)について学習します。
