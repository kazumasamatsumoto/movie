# #161 「Numberからnumberへ」

## 概要
TypeScript v5.9のNumberからnumberへの変換について学習します。Numberオブジェクトをプリミティブのnumber型に変換する方法を理解します。

## 学習目標
- Numberからnumberへの変換方法を理解する
- valueOf()メソッドの使用方法を理解する
- 実用的な変換例を理解する

## 画面表示用コード

```typescript
// Numberからnumberへの変換

// 1. valueOf()メソッド
// let numObj = new Number(30);
// let num: number = numObj.valueOf(); // number型に変換

// 2. Number()関数
// let numObj = new Number(30);
// let num: number = Number(numObj); // number型に変換

// 3. 数値リテラル（推奨）
let num: number = 30; // 最初からnumber型

// 実用的な例
let userData = {
  age: 25,
  price: 1500
};

let userAge: number = Number(userData.age);
let productPrice: number = Number(userData.price);
```

## 重要なポイント
1. **valueOf()**: Numberオブジェクトをnumber型に変換
2. **Number()関数**: 型変換の汎用関数
3. **推奨**: 最初からnumber型を使用する

## 次のステップ
次回は、自動ボックス化について学習します。
