# #230 「論理和OR - ||」

## 概要
TypeScript v5.9の論理和ORについて学習します。||演算子で片方の値がtrueの場合にtrueを返す演算子の使用方法を理解します。

## 学習目標
- 論理和ORの基本を理解する
- ||演算子の使用方法を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// 論理和OR - ||
let isActive: boolean = true;
let hasPermission: boolean = false;
let isCompleted: boolean = false;

// 基本的な使用
let canProceed: boolean = isActive || hasPermission; // true
let canAccess: boolean = isCompleted || hasPermission; // false

// 実用的な例
let userLoggedIn: boolean = true;
let formValid: boolean = false;
let canAccess: boolean = userLoggedIn || formValid; // true

// 条件分岐での使用
if (isActive || hasPermission) {
  console.log("アクセス可能です");
}
```

## 重要なポイント
1. **論理和**: 片方の値がtrueの場合にtrue
2. **条件分岐**: 複数の条件のいずれかが満たされる場合
3. **実用性**: 複数の条件分岐に活用

## 次のステップ
次回は、ORの型推論について学習します。
