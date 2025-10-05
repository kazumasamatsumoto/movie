# #123 「Infinityの生成 - 1/0」

## 概要
TypeScript v5.9のInfinityの生成について学習します。数値計算でInfinityが生成される方法を理解し、計算結果の予測を学びます。

## 学習目標
- Infinityの生成方法を理解する
- 計算による生成を理解する
- 実用的な例を理解する

## 画面表示用コード

```typescript
// Infinityの生成
let result1: number = 1 / 0;        // Infinity
let result2: number = -1 / 0;       // -Infinity
let result3: number = Number.MAX_VALUE * 2; // Infinity

// 実用的な例
let division: number = 100 / 0;     // Infinity
let multiplication: number = Number.MAX_VALUE * 10; // Infinity

console.log(result1); // Infinity
console.log(result2); // -Infinity
console.log(division); // Infinity
```

## 重要なポイント
1. **0除算**: 1/0でInfinityが生成
2. **負の0除算**: -1/0で-Infinityが生成
3. **オーバーフロー**: 大きな数値の計算で生成

## 次のステップ
次回は、-Infinityについて学習します。