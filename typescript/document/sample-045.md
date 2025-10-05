# #045 「Stringオブジェクトの問題点」

## 概要
TypeScript v5.9のStringオブジェクト問題点について学習します。型の不一致、比較の問題、パフォーマンスの低下などの問題を理解します。

## 学習目標
- Stringオブジェクトの問題点を理解する
- 型の不一致の問題を理解する
- 比較の問題を理解する

## 画面表示用コード

```typescript
// Stringオブジェクトの問題点

// 1. 型の不一致
// let strObj: String = new String("Hello");
// let str: string = "Hello";
// console.log(strObj === str); // false

// 2. オブジェクト比較の問題
// let obj1 = new String("Hello");
// let obj2 = new String("Hello");
// console.log(obj1 === obj2); // false（異なるオブジェクト）

// 正しい方法
let str1: string = "Hello";
let str2: string = "Hello";
console.log(str1 === str2); // true

// 実用的な例
let userName: string = "Alice";
let userInput: string = "Alice";
console.log(userName === userInput); // true
```

## 重要なポイント
1. **型の不一致**: String型とstring型は異なる
2. **比較の問題**: オブジェクトは異なるインスタンス
3. **パフォーマンス**: オブジェクト型は重い

## 次のステップ
次回は、Stringからstringへの変換について学習します。