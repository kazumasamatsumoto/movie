# #124 「-Infinity」

## 概要
TypeScript v5.9の-Infinityについて学習します。負の無限大を表す特殊な数値として、正の無限大との違いを理解します。

## 学習目標
- -Infinityの基本概念を理解する
- Infinityとの違いを理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// -Infinity
let negativeInfinity: number = -Infinity;
let positiveInfinity: number = Infinity;

// 実用的な例
let minValue: number = -Infinity;
let maxValue: number = Infinity;

// 計算で生成される
let result: number = -1 / 0; // -Infinity

console.log(negativeInfinity); // -Infinity
console.log(minValue); // -Infinity
console.log(result); // -Infinity
```

## 重要なポイント
1. **負の無限大**: 負の方向の無限大を表現
2. **符号の違い**: Infinityと-Infinityの符号が異なる
3. **計算生成**: -1/0などの計算で生成

## 次のステップ
次回は、NaNについて学習します。