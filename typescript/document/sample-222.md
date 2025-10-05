# #222 「リテラル型とboolean型の違い」

## 概要
TypeScript v5.9のリテラル型とboolean型の違いについて学習します。型の厳密性と代入可能な値の範囲の違いを理解します。

## 学習目標
- リテラル型とboolean型の違いを理解する
- 型の厳密性を理解する
- 適切な型選択を理解する

## 画面表示用コード

```typescript
// リテラル型とboolean型の違い

// boolean型 - trueとfalse両方許可
let flag1: boolean = true;   // OK
let flag2: boolean = false;  // OK

// trueリテラル型 - trueのみ許可
let flag3: true = true;      // OK
// let flag4: true = false;  // エラー

// falseリテラル型 - falseのみ許可
let flag5: false = false;    // OK
// let flag6: false = true;  // エラー

// 実用的な例
let userLoggedIn: boolean = true;    // 変更可能
const isProduction: true = true;     // 変更不可、trueのみ
```

## 重要なポイント
1. **boolean型**: trueとfalse両方を許可
2. **リテラル型**: 特定の値のみを許可
3. **使い分け**: 用途に応じて適切な型を選択

## 次のステップ
次回は、型推論（const使用時）について学習します。
