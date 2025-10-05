# #159 「Numberコンストラクタ」

## 概要
TypeScript v5.9のNumberコンストラクタについて学習します。Numberコンストラクタの使用方法と問題点を理解します。

## 学習目標
- Numberコンストラクタの使用方法を理解する
- Numberコンストラクタの問題点を理解する
- 適切な代替方法を理解する

## 画面表示用コード

```typescript
// Numberコンストラクタ（避けるべき）
// let numObj = new Number(30); // 非推奨

// 正しい方法：数値リテラル
let num: number = 30;

// 型の違い
console.log(typeof num);        // "number"
// console.log(typeof numObj);  // "object"

// 比較の問題
let num1: number = 30;
let num2: number = 30;
console.log(num1 === num2); // true

// let obj1 = new Number(30);
// let obj2 = new Number(30);
// console.log(obj1 === obj2); // false
```

## 重要なポイント
1. **非推奨**: Numberコンストラクタの使用は避けるべき
2. **問題点**: オブジェクト型になるため比較で問題
3. **推奨**: 数値リテラルを使用する

## 次のステップ
次回は、Numberオブジェクトの問題について学習します。
