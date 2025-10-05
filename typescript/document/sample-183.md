# #183 「イプシロン比較」

## 概要
TypeScript v5.9のイプシロン比較について学習します。浮動小数点数の等価性を判定する方法を理解します。

## 学習目標
- イプシロン比較の仕組みを理解する
- 微小な誤差範囲での比較を理解する
- 実用的な実装方法を理解する

## 画面表示用コード

```typescript
// イプシロン比較
function epsilonEqual(a: number, b: number, epsilon: number = 1e-10): boolean {
  return Math.abs(a - b) < epsilon;
}

// 実用的な例
let num1: number = 0.1 + 0.2;
let num2: number = 0.3;

console.log(num1 === num2); // false
console.log(epsilonEqual(num1, num2)); // true

// 実用的な例
let price1: number = 100.50;
let price2: number = 100.50;
console.log(epsilonEqual(price1, price2)); // true
```

## 重要なポイント
1. **イプシロン**: 微小な誤差範囲
2. **比較**: 絶対値の差で比較
3. **実用性**: 浮動小数点数の等価性判定

## 次のステップ
次回は、Math.absを使った比較について学習します。
