# #141 「乗算の型推論」

## 概要
TypeScript v5.9の乗算の型推論について学習します。乗算演算の結果の型が自動的に推論される機能を理解します。

## 学習目標
- 乗算の型推論を理解する
- 型推論の動作を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// 乗算の型推論
let a: number = 5;
let b: number = 6;
let product = a * b; // number型と推論

// 型推論の例
let price = 1000;    // number型
let quantity = 3;    // number型
let total = price * quantity; // number型と推論

// 実用的な例
let rate = 0.1;
let amount = 5000;
let tax = amount * rate; // number型
```

## 重要なポイント
1. **型推論**: 乗算結果はnumber型と推論
2. **自動判定**: TypeScriptが自動的に型を判定
3. **型安全性**: 型チェックが自動的に行われる

## 次のステップ
次回は、除算演算子について学習します。

