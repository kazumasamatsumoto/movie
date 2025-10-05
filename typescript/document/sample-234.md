# #234 「論理否定NOT - !」

## 概要
TypeScript v5.9の論理否定NOTについて学習します。!演算子でboolean値を反転する演算子の使用方法を理解します。

## 学習目標
- 論理否定NOTの基本を理解する
- !演算子の使用方法を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// 論理否定NOT - !
let isActive: boolean = true;
let hasPermission: boolean = false;
let isCompleted: boolean = true;

// 基本的な使用
let isInactive: boolean = !isActive;        // false
let hasNoPermission: boolean = !hasPermission; // true
let isNotCompleted: boolean = !isCompleted; // false

// 実用的な例
let userLoggedIn: boolean = true;
let formValid: boolean = false;
let userLoggedOut: boolean = !userLoggedIn; // false
let formInvalid: boolean = !formValid;      // true
```

## 重要なポイント
1. **論理否定**: boolean値を反転
2. **条件の反転**: 条件の意味を反転
3. **実用性**: 条件分岐の制御に活用

## 次のステップ
次回は、NOTの型推論について学習します。
