# #184 「Math.absを使った比較」

## 概要
TypeScript v5.9のMath.absを使った比較について学習します。絶対値を使って数値の差を比較する方法を理解します。

## 学習目標
- Math.absを使った比較方法を理解する
- 絶対値の計算を理解する
- 実用的な実装方法を理解する

## 画面表示用コード

```typescript
// Math.absを使った比較
function isEqual(a: number, b: number, tolerance: number = 1e-10): boolean {
  return Math.abs(a - b) < tolerance;
}

// 実用的な例
let num1: number = 0.1 + 0.2;
let num2: number = 0.3;

console.log(num1 === num2); // false
console.log(isEqual(num1, num2)); // true

// 実用的な例
let price1: number = 100.50;
let price2: number = 100.50;
console.log(isEqual(price1, price2)); // true
```

## 重要なポイント
1. **Math.abs**: 絶対値を取得
2. **差の比較**: 数値の差を比較
3. **実用性**: 浮動小数点数の等価性判定

## 次のステップ
次回は、金銭計算の注意点について学習します。
