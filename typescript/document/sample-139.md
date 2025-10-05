# #139 「減算の型推論」

## 概要
TypeScript v5.9の減算の型推論について学習します。減算演算の結果の型が自動的に推論される機能を理解します。

## 学習目標
- 減算の型推論を理解する
- 型推論の動作を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// 減算の型推論
let a: number = 30;
let b: number = 10;
let difference = a - b; // number型と推論

// 型推論の例
let totalPrice = 1200;  // number型
let discount = 200;     // number型
let finalPrice = totalPrice - discount; // number型と推論

// 実用的な例
let currentYear = 2024;
let birthYear = 1990;
let age = currentYear - birthYear; // number型
```

## 重要なポイント
1. **型推論**: 減算結果はnumber型と推論
2. **自動判定**: TypeScriptが自動的に型を判定
3. **型安全性**: 型チェックが自動的に行われる

## 次のステップ
次回は、乗算演算子について学習します。