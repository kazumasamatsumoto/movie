# #128 「isNaN()関数」

## 概要
TypeScript v5.9のisNaN()関数について学習します。値がNaNかどうかを判定する関数の使用方法を理解します。

## 学習目標
- isNaN()関数の基本を理解する
- NaN判定の方法を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// isNaN()関数
let nan: number = NaN;
let normalNumber: number = 100;
let stringValue: string = "abc";

// NaN判定
let isNan1: boolean = isNaN(nan);        // true
let isNan2: boolean = isNaN(normalNumber); // false
let isNan3: boolean = isNaN(stringValue);  // true

// 実用的な例
let userInput: number = parseInt("123");
if (isNaN(userInput)) {
  console.log("無効な数値です");
} else {
  console.log("有効な数値です");
}
```

## 重要なポイント
1. **NaN判定**: 値がNaNかどうかを判定
2. **型変換**: 文字列も数値に変換して判定
3. **実用性**: 数値の検証に活用

## 次のステップ
次回は、Number.isNaN()の違いについて学習します。