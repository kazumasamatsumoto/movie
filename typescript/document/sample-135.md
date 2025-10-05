# #135 「特殊な数値まとめ」

## 概要
TypeScript v5.9の特殊な数値まとめについて学習します。Infinity、NaN、判定関数の要点を整理し、数値処理の理解を深めます。

## 学習目標
- 特殊な数値の要点を整理する
- 判定関数の使い分けを理解する
- 実用的な応用を理解する

## 画面表示用コード

```typescript
// 特殊な数値まとめ

// 1. 特殊な数値
let infinity: number = Infinity;
let negativeInfinity: number = -Infinity;
let nan: number = NaN;

// 2. 判定関数
let isNan: boolean = Number.isNaN(nan);
let isFinite: boolean = Number.isFinite(infinity);
let isInteger: boolean = Number.isInteger(42);
let isSafe: boolean = Number.isSafeInteger(123);

// 3. 実用的な例
let userInput: number = parseFloat("123.45");
if (Number.isFinite(userInput) && Number.isSafeInteger(userInput)) {
  console.log("有効な整数です");
}
```

## 重要なポイント
1. **特殊な数値**: Infinity、-Infinity、NaN
2. **判定関数**: Number.isNaN()、Number.isFinite()など
3. **実用性**: 数値の検証とエラーハンドリング

## 次のステップ
次回は、加算演算子について学習します。