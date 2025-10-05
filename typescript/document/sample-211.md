# #211 「booleanリテラル型」

## 概要
TypeScript v5.9のbooleanリテラル型について学習します。trueまたはfalseの特定の値のみを許可する型の使用方法を理解します。

## 学習目標
- booleanリテラル型の基本を理解する
- 特定の値の制限を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// booleanリテラル型
let isActive: true = true;        // trueのみ許可
let isCompleted: false = false;   // falseのみ許可

// 実用的な例
let userLoggedIn: true = true;    // trueのみ許可
let formValid: false = false;     // falseのみ許可

// 型の制限
// isActive = false; // エラー: Type 'false' is not assignable to type 'true'
// isCompleted = true; // エラー: Type 'true' is not assignable to type 'false'
```

## 重要なポイント
1. **リテラル型**: 特定の値のみを許可
2. **型制限**: より厳密な型制御
3. **実用性**: 定数の型安全性を保つ

## 次のステップ
次回は、デフォルト値について学習します。
