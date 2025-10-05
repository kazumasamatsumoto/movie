# #147 「べき乗の型推論」

## 概要
TypeScript v5.9のべき乗の型推論について学習します。べき乗演算の結果の型が自動的に推論される機能を理解します。

## 学習目標
- べき乗の型推論を理解する
- 型推論の動作を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// べき乗の型推論
let base: number = 2;
let exponent: number = 3;
let result = base ** exponent; // number型と推論

// 型推論の例
let side = 5;          // number型
let area = side ** 2;  // number型と推論

// 実用的な例
let rate = 1.1;
let years = 3;
let finalAmount = 1000 * (rate ** years); // number型
```

## 重要なポイント
1. **型推論**: べき乗結果はnumber型と推論
2. **自動判定**: TypeScriptが自動的に型を判定
3. **型安全性**: 型チェックが自動的に行われる

## 次のステップ
次回は、インクリメントについて学習します。

