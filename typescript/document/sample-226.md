# #226 「論理積AND - &&」

## 概要
TypeScript v5.9の論理積ANDについて学習します。&&演算子で両方の値がtrueの場合にtrueを返す演算子の使用方法を理解します。

## 学習目標
- 論理積ANDの基本を理解する
- &&演算子の使用方法を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// 論理積AND - &&
let isActive: boolean = true;
let hasPermission: boolean = true;
let isCompleted: boolean = false;

// 基本的な使用
let canProceed: boolean = isActive && hasPermission; // true
let canAccess: boolean = isActive && isCompleted;    // false

// 実用的な例
let userLoggedIn: boolean = true;
let formValid: boolean = false;
let canSubmit: boolean = userLoggedIn && formValid; // false

// 条件分岐での使用
if (isActive && hasPermission) {
  console.log("アクセス可能です");
}
```

## 重要なポイント
1. **論理積**: 両方の値がtrueの場合にtrue
2. **条件分岐**: 複数の条件を組み合わせ
3. **実用性**: 複雑な条件分岐に活用

## 次のステップ
次回は、ANDの型推論について学習します。
