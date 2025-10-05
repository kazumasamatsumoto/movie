# #145 「剰余の型推論」

## 概要
TypeScript v5.9の剰余の型推論について学習します。剰余演算の結果の型が自動的に推論される機能を理解します。

## 学習目標
- 剰余の型推論を理解する
- 型推論の動作を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// 剰余の型推論
let a: number = 17;
let b: number = 5;
let remainder = a % b; // number型と推論

// 型推論の例
let number = 42;       // number型
let isEven = number % 2 === 0; // boolean型と推論

// 実用的な例
let seconds = 125;
let minutes = Math.floor(seconds / 60);
let remainingSeconds = seconds % 60; // number型
```

## 重要なポイント
1. **型推論**: 剰余結果はnumber型と推論
2. **自動判定**: TypeScriptが自動的に型を判定
3. **型安全性**: 型チェックが自動的に行われる

## 次のステップ
次回は、べき乗演算子について学習します。

