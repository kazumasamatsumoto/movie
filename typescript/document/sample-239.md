# #239 「論理演算子の組み合わせ」

## 概要
TypeScript v5.9の論理演算子の組み合わせについて学習します。複数の論理演算子を組み合わせて使用する方法を理解します。

## 学習目標
- 論理演算子の組み合わせ方法を理解する
- 括弧を使った優先順位の制御を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// 論理演算子の組み合わせ
let isActive: boolean = true;
let hasPermission: boolean = false;
let isCompleted: boolean = true;
let hasData: boolean = false;

// 組み合わせの例
let result1 = (isActive && hasPermission) || isCompleted; // 括弧で優先順位を制御
let result2 = !(isActive && hasPermission) && hasData;    // 否定と組み合わせ
let result3 = isActive && (hasPermission || isCompleted); // ORとANDの組み合わせ

// 実用的な例
let userLoggedIn: boolean = true;
let formValid: boolean = false;
let hasPermission: boolean = true;
let canSubmit = userLoggedIn && (formValid || hasPermission); // 複雑な条件
```

## 重要なポイント
1. **組み合わせ**: 複数の論理演算子を組み合わせ
2. **括弧**: 優先順位を制御するために括弧を使用
3. **実用性**: 複雑な条件分岐に活用

## 次のステップ
次回は、論理演算まとめについて学習します。
