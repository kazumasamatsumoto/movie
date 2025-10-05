# #108 「整数と小数の区別なし」

## 概要
TypeScript v5.9の整数と小数の区別について学習します。TypeScriptでは整数と小数を区別せず、すべてnumber型として扱うことを理解します。

## 学習目標
- 整数と小数の区別がないことを理解する
- JavaScriptの仕様を引き継ぐことを理解する
- 数値計算の理解を深める

## 画面表示用コード

```typescript
// 整数と小数の区別なし
let integer: number = 100;    // 整数
let decimal: number = 3.14;   // 小数
let negative: number = -50;   // 負数

// すべて同じnumber型
console.log(typeof integer);  // "number"
console.log(typeof decimal);  // "number"
console.log(typeof negative); // "number"

// 実用的な例
let userAge: number = 25;     // 整数
let productPrice: number = 2980.50; // 小数
let discountRate: number = 0.1;     // 小数
```

## 重要なポイント
1. **型の統一**: 整数と小数は同じnumber型
2. **JavaScript互換**: JavaScriptの仕様を引き継ぐ
3. **計算の柔軟性**: 整数と小数の混在した計算が可能

## 次のステップ
次回は、number型の範囲について学習します。