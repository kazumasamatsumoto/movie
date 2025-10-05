# #105 「型推論でnumber型」

## 概要
TypeScript v5.9のnumber型推論について学習します。数値リテラルから自動的に型を推論する機能を理解します。

## 学習目標
- 型推論の基本概念を理解する
- 型推論と明示的型注釈の違いを理解する
- 型推論の利点と注意点を理解する

## 画面表示用コード

```typescript
// 型推論の例
let age = 30;           // number型と推論
let price = 2980.50;    // number型と推論
let count = -5;         // number型と推論

// 型安全性は保たれる
// age = "30"; // エラー: Type 'string' is not assignable to type 'number'

// 実用的な例
let userAge = 25;       // number型
let productPrice = 1500; // number型
let discountRate = 0.1;  // number型
```

## 重要なポイント
1. **自動型判定**: 数値リテラルから型を自動推論
2. **コードの簡潔性**: 型注釈を書く手間が省ける
3. **型安全性**: 推論された型に対して型チェックが行われる

## 次のステップ
次回は、constでnumber型について学習します。