# #104 「number型の初期化」

## 概要
TypeScript v5.9のnumber型初期化について学習します。宣言と同時に初期値を設定する効率的な方法を理解します。

## 学習目標
- 変数の初期化の基本構文を理解する
- 初期化の利点を理解する
- 適切な初期化方法を習得する

## 画面表示用コード

```typescript
// number型の初期化
let age: number = 30;
let price: number = 2980.50;
let count: number = 0;
let result: number = 10 * 5 + 3;

// 実用的な例
let userAge: number = 25;
let productPrice: number = 1500;
let taxRate: number = 0.1;
let totalPrice: number = productPrice * (1 + taxRate);
```

## 重要なポイント
1. **一行で完結**: 宣言、型指定、初期化を同時に実行
2. **未定義回避**: 初期化によりundefined状態を避けられる
3. **意図の明確化**: コードの意図が明確になる

## 次のステップ
次回は、型推論でnumber型について学習します。