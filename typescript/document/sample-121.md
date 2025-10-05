# #121 「Infinityとは」

## 概要
TypeScript v5.9のInfinityについて学習します。無限大を表す特殊な数値として、数値計算で無限大が必要な場面で使用される重要な概念です。

## 学習目標
- Infinityの基本概念を理解する
- 無限大の表現方法を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// Infinityとは
let infinity: number = Infinity;
let negativeInfinity: number = -Infinity;

// 実用的な例
let maxValue: number = Infinity;
let minValue: number = -Infinity;

// 計算で生成される
let result1: number = 1 / 0; // Infinity
let result2: number = -1 / 0; // -Infinity

console.log(infinity); // Infinity
console.log(result1); // Infinity
```

## 重要なポイント
1. **無限大**: 数値の上限を超える値を表現
2. **正負**: Infinityと-Infinityの両方が存在
3. **計算生成**: 1/0などの計算で自動生成

## 次のステップ
次回は、Infinityの型について学習します。