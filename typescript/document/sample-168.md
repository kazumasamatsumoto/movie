# #168 「parseFloat()関数」

## 概要
TypeScript v5.9のparseFloat()関数について学習します。文字列を浮動小数点数に変換する関数の基本的な使用方法を理解します。

## 学習目標
- parseFloat()関数の基本を理解する
- 浮動小数点変換の仕組みを理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// parseFloat()関数
let str1: string = "123.45";
let str2: string = "123";
let str3: string = "abc123.45";

// 浮動小数点変換
let float1: number = parseFloat(str1);      // 123.45
let float2: number = parseFloat(str2);      // 123
let float3: number = parseFloat(str3);      // NaN

// 実用的な例
let userInput: string = "25.5";
let userAge: number = parseFloat(userInput);

let priceStr: string = "1500.99円";
let price: number = parseFloat(priceStr); // 1500.99
```

## 重要なポイント
1. **浮動小数点変換**: 文字列を浮動小数点数に変換
2. **小数保持**: 小数部分も保持
3. **実用性**: 小数を含む文字列の数値変換に活用

## 次のステップ
次回は、暗黙的な型変換について学習します。
