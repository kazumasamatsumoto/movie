# #158 「Number型の宣言」

## 概要
TypeScript v5.9のNumber型宣言について学習します。Number型の宣言方法と使用を避けるべき理由を理解します。

## 学習目標
- Number型の宣言方法を理解する
- Number型の問題点を理解する
- 避けるべき理由を理解する

## 画面表示用コード

```typescript
// Number型（避けるべき）
// let ageObj: Number = new Number(30); // 非推奨
// let priceObj: Number = new Number(2980.50); // 非推奨

// 正しい方法：number型を使用
let age: number = 30;
let price: number = 2980.50;

// 型の違い
console.log(typeof age);        // "number"
// console.log(typeof ageObj);  // "object"

// 実用的な例
let userAge: number = 25;
let productPrice: number = 1500;
let totalPrice: number = userAge + productPrice;
```

## 重要なポイント
1. **非推奨**: Number型の使用は避けるべき
2. **問題点**: パフォーマンスと型の不一致
3. **推奨**: number型を使用する

## 次のステップ
次回は、Numberコンストラクタについて学習します。
