# #166 「Number()関数」

## 概要
TypeScript v5.9のNumber()関数について学習します。値を数値に変換する関数の基本的な使用方法を理解します。

## 学習目標
- Number()関数の基本を理解する
- 型変換の仕組みを理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// Number()関数
let str: string = "123";
let bool: boolean = true;
let nullValue: null = null;

// 数値変換
let num1: number = Number(str);      // 123
let num2: number = Number(bool);     // 1
let num3: number = Number(nullValue); // 0

// 実用的な例
let userInput: string = "25";
let userAge: number = Number(userInput);

let isActive: boolean = true;
let activeValue: number = Number(isActive); // 1
```

## 重要なポイント
1. **型変換**: 様々な型を数値に変換
2. **文字列**: 数値文字列を数値に変換
3. **実用性**: データ変換に活用

## 次のステップ
次回は、parseInt()関数について学習します。
