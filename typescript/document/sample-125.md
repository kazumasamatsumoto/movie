# #125 「NaNとは」

## 概要
TypeScript v5.9のNaNについて学習します。Not a Numberを表す特殊な数値として、無効な数値計算の結果を理解します。

## 学習目標
- NaNの基本概念を理解する
- 無効な数値計算の結果を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// NaNとは
let nan: number = NaN;
let invalidResult: number = 0 / 0;

// 実用的な例
let parseResult: number = parseInt("abc"); // NaN
let mathResult: number = Math.sqrt(-1); // NaN

console.log(nan); // NaN
console.log(invalidResult); // NaN
console.log(parseResult); // NaN
```

## 重要なポイント
1. **Not a Number**: 数値ではないことを表現
2. **無効な計算**: 0/0などの無効な計算で生成
3. **解析エラー**: 数値解析に失敗した場合に生成

## 次のステップ
次回は、NaNの型について学習します。