# #190 「数値計算まとめ」

## 概要
TypeScript v5.9の数値計算まとめについて学習します。数値計算の要点と重要な機能のまとめを理解します。

## 学習目標
- 数値計算の要点を整理する
- 主要な機能の使い分けを理解する
- 実用的な応用を理解する

## 画面表示用コード

```typescript
// 数値計算まとめ

// 1. 精度問題の理解
let num1: number = 0.1 + 0.2;
console.log(num1 === 0.3); // false

// 2. 回避方法
function addDecimals(a: number, b: number): number {
  const factor = 100;
  return (Math.round(a * factor) + Math.round(b * factor)) / factor;
}

// 3. 適切な比較
function isEqual(a: number, b: number): boolean {
  return Math.abs(a - b) < 1e-10;
}

// 4. BigIntの活用
let largeId: bigint = 1234567890123456789n;
```

## 重要なポイント
1. **精度問題**: IEEE 754の制限による問題
2. **回避方法**: 整数演算やライブラリの使用
3. **適切な比較**: イプシロン比較の活用
4. **BigInt**: 大きな数値の正確な処理

## 次のステップ
次回は、Angularフォームでのnumber型について学習します。
