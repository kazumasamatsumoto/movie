# #102 「number型の宣言 - let age: number」

## 概要
TypeScript v5.9のnumber型宣言について学習します。型注釈を使用して明示的に数値型を指定する方法を理解します。

## 学習目標
- number型の変数宣言の基本構文を理解する
- 型注釈の役割と重要性を理解する
- 宣言と代入の違いを理解する

## 画面表示用コード

```typescript
// number型の宣言
let age: number;
let price: number;
let count: number;

// 後で値を代入
age = 30;
price = 2980.50;
count = -5;

// 実用的な例
let userAge: number = 25;
let productPrice: number = 1500;
let itemCount: number = 10;
```

## 重要なポイント
1. **型注釈**: `: number` で型を明示的に指定
2. **未初期化**: 宣言だけでは値はundefined
3. **型安全性**: 宣言時に型を指定することで、後で型チェックが行われる

## 次のステップ
次回は、number型への代入について学習します。