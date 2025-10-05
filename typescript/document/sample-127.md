# #127 「NaNの生成 - 0/0」

## 概要
TypeScript v5.9のNaNの生成について学習します。数値計算でNaNが生成される方法を理解し、エラーハンドリングの基礎を学びます。

## 学習目標
- NaNの生成方法を理解する
- 無効な計算による生成を理解する
- 実用的な例を理解する

## 画面表示用コード

```typescript
// NaNの生成
let result1: number = 0 / 0;        // NaN
let result2: number = NaN + 1;      // NaN
let result3: number = Math.sqrt(-1); // NaN

// 実用的な例
let division: number = 0 / 0;       // NaN
let parseError: number = parseInt("abc"); // NaN
let invalidMath: number = Math.log(-1); // NaN

console.log(result1); // NaN
console.log(division); // NaN
console.log(parseError); // NaN
```

## 重要なポイント
1. **0除算**: 0/0でNaNが生成
2. **NaN伝播**: NaNを含む計算はNaNになる
3. **無効な数学関数**: 定義域外の値でNaNが生成

## 次のステップ
次回は、isNaN()関数について学習します。