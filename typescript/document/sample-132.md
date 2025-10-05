# #132 「Number.isInteger()」

## 概要
TypeScript v5.9のNumber.isInteger()について学習します。値が整数かどうかを判定する関数の使用方法を理解します。

## 学習目標
- Number.isInteger()の基本を理解する
- 整数判定の方法を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// Number.isInteger()
let integer: number = 42;
let decimal: number = 3.14;
let stringNumber: string = "123";

// 整数判定
let isInteger1: boolean = Number.isInteger(integer);     // true
let isInteger2: boolean = Number.isInteger(decimal);     // false
let isInteger3: boolean = Number.isInteger(stringNumber); // false

// 実用的な例
let userAge: number = 25;
if (Number.isInteger(userAge)) {
  console.log("整数の年齢です");
} else {
  console.log("小数の年齢は無効です");
}
```

## 重要なポイント
1. **整数判定**: 値が整数かどうかを判定
2. **小数除外**: 小数はfalseになる
3. **実用性**: 整数の検証に活用

## 次のステップ
次回は、Number.isSafeInteger()について学習します。