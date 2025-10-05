# #189 「浮動小数点のベストプラクティス」

## 概要
TypeScript v5.9の浮動小数点のベストプラクティスについて学習します。精度問題を避けるための推奨事項を理解します。

## 学習目標
- 浮動小数点のベストプラクティスを理解する
- 精度問題の回避方法を理解する
- 実用的な実装方法を理解する

## 画面表示用コード

```typescript
// 浮動小数点のベストプラクティス

// 1. 整数演算の使用
function addDecimals(a: number, b: number): number {
  const factor = 100;
  return (Math.round(a * factor) + Math.round(b * factor)) / factor;
}

// 2. 適切な比較
function isEqual(a: number, b: number): boolean {
  return Math.abs(a - b) < 1e-10;
}

// 3. 表示用のフォーマット
let price: number = 1500.99;
let displayPrice: string = price.toFixed(2);

// 実用的な例
let total: number = addDecimals(0.1, 0.2);
console.log(isEqual(total, 0.3)); // true
```

## 重要なポイント
1. **整数演算**: 小数を整数に変換して計算
2. **適切な比較**: イプシロン比較を使用
3. **表示フォーマット**: toFixed()で表示を調整

## 次のステップ
次回は、数値計算まとめについて学習します。
