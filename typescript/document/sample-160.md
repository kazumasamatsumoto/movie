# #160 「Numberオブジェクトの問題」

## 概要
TypeScript v5.9のNumberオブジェクト問題について学習します。Numberオブジェクトの使用による問題点を理解します。

## 学習目標
- Numberオブジェクトの問題点を理解する
- 型の不一致問題を理解する
- 適切な回避方法を理解する

## 画面表示用コード

```typescript
// Numberオブジェクトの問題点

// 1. 型の不一致
// let numObj: Number = new Number(30);
// let num: number = 30;
// console.log(numObj === num); // false

// 2. オブジェクト比較の問題
// let obj1 = new Number(30);
// let obj2 = new Number(30);
// console.log(obj1 === obj2); // false（異なるオブジェクト）

// 正しい方法
let num1: number = 30;
let num2: number = 30;
console.log(num1 === num2); // true

// 実用的な例
let userAge: number = 25;
let productPrice: number = 1500;
console.log(userAge === 25); // true
```

## 重要なポイント
1. **型の不一致**: Numberオブジェクトとnumber型は異なる
2. **比較問題**: オブジェクト比較で予期しない結果
3. **回避方法**: number型を使用する

## 次のステップ
次回は、Numberからnumberへの変換について学習します。
