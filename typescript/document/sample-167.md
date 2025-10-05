# #167 「parseInt()関数」

## 概要
TypeScript v5.9のparseInt()関数について学習します。文字列を整数に変換する関数の基本的な使用方法を理解します。

## 学習目標
- parseInt()関数の基本を理解する
- 整数変換の仕組みを理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// parseInt()関数
let str1: string = "123";
let str2: string = "123.45";
let str3: string = "abc123";

// 整数変換
let int1: number = parseInt(str1);      // 123
let int2: number = parseInt(str2);      // 123
let int3: number = parseInt(str3);      // NaN

// 実用的な例
let userInput: string = "25";
let userAge: number = parseInt(userInput);

let priceStr: string = "1500円";
let price: number = parseInt(priceStr); // 1500
```

## 重要なポイント
1. **整数変換**: 文字列を整数に変換
2. **小数切り捨て**: 小数部分は無視
3. **実用性**: 文字列入力の数値変換に活用

## 次のステップ
次回は、parseFloat()関数について学習します。
