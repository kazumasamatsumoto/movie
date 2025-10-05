# #164 「なぜnumberを使うべきか」

## 概要
TypeScript v5.9のnumber型使用理由について学習します。number型を使用すべき理由と利点を理解します。

## 学習目標
- number型の利点を理解する
- 型安全性の重要性を理解する
- パフォーマンスの違いを理解する

## 画面表示用コード

```typescript
// number型を使うべき理由

// 1. 型安全性
let userAge: number = 25;
// userAge = "25"; // エラー: Type 'string' is not assignable to type 'number'

// 2. パフォーマンス
let productPrice: number = 1500; // 軽量なプリミティブ型

// 3. 一貫性
let userData = {
  age: 25,
  price: 1500
};
let totalValue: number = userData.age + userData.price;

// 4. 予測可能な動作
let num1: number = 30;
let num2: number = 30;
console.log(num1 === num2); // 常にtrue
```

## 重要なポイント
1. **型安全性**: コンパイル時の型チェック
2. **パフォーマンス**: 軽量で高速
3. **一貫性**: 予測可能な動作

## 次のステップ
次回は、Number型使用禁止について学習します。
