# #156 「Numberとnumberの違い」

## 概要
TypeScript v5.9のNumberとnumberの違いについて学習します。プリミティブ型とオブジェクト型の違いを理解し、適切な型選択を行います。

## 学習目標
- Numberとnumberの違いを理解する
- プリミティブ型とオブジェクト型の違いを理解する
- 適切な型選択方法を理解する

## 画面表示用コード

```typescript
// number型（推奨）- プリミティブ型
let age: number = 30;
let price: number = 2980.50;

// Number型（非推奨）- オブジェクト型
// let ageObj: Number = new Number(30); // 避けるべき

// 型の違い
console.log(typeof age);        // "number"
// console.log(typeof ageObj);  // "object"

// 実用的な例
let userAge: number = 25;
let productPrice: number = 1500;
let totalPrice: number = userAge + productPrice;
```

## 重要なポイント
1. **プリミティブ型**: number型は軽量で効率的
2. **オブジェクト型**: Number型は重く、比較で問題が発生
3. **推奨**: 常にnumber型を使用する

## 次のステップ
次回は、number型の宣言について学習します。
