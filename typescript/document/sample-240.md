# #240 「論理演算まとめ」

## 概要
TypeScript v5.9の論理演算まとめについて学習します。論理演算子の要点と重要な機能のまとめを理解します。

## 学習目標
- 論理演算の要点を整理する
- 主要な機能の使い分けを理解する
- 実用的な応用を理解する

## 画面表示用コード

```typescript
// 論理演算まとめ

// 1. AND演算子（&&）
let isActive: boolean = true;
let hasPermission: boolean = false;
let canProceed: boolean = isActive && hasPermission; // false

// 2. OR演算子（||）
let canAccess: boolean = isActive || hasPermission; // true

// 3. NOT演算子（!）
let isInactive: boolean = !isActive; // false

// 4. 二重否定（!!）
let userName: string = "John";
let hasName: boolean = !!userName; // true

// 5. 実用的な例
let userLoggedIn: boolean = true;
let formValid: boolean = false;
let canSubmit: boolean = userLoggedIn && formValid; // false
```

## 重要なポイント
1. **AND演算子**: 両方の値がtrueの場合にtrue
2. **OR演算子**: 片方の値がtrueの場合にtrue
3. **NOT演算子**: boolean値を反転
4. **二重否定**: 値をboolean型に変換
5. **実用性**: 複雑な条件分岐に活用

## 次のステップ
次回は、null型について学習します。
