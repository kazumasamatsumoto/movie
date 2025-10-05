# #143 「除算の型推論」

## 概要
TypeScript v5.9の除算の型推論について学習します。除算演算の結果の型が自動的に推論される機能を理解します。

## 学習目標
- 除算の型推論を理解する
- 型推論の動作を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// 除算の型推論
let a: number = 20;
let b: number = 4;
let quotient = a / b; // number型と推論

// 型推論の例
let totalAmount = 1200; // number型
let people = 4;         // number型
let perPerson = totalAmount / people; // number型と推論

// 実用的な例
let price = 1000;
let discountRate = 0.2;
let discountAmount = price * discountRate; // number型
```

## 重要なポイント
1. **型推論**: 除算結果はnumber型と推論
2. **自動判定**: TypeScriptが自動的に型を判定
3. **型安全性**: 型チェックが自動的に行われる

## 次のステップ
次回は、剰余演算子について学習します。

