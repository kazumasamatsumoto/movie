# #238 「論理演算子の優先順位」

## 概要
TypeScript v5.9の論理演算子の優先順位について学習します。複数の論理演算子が使われた時の評価順序を理解します。

## 学習目標
- 論理演算子の優先順位を理解する
- 評価順序のルールを理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// 論理演算子の優先順位
let isActive: boolean = true;
let hasPermission: boolean = false;
let isCompleted: boolean = true;

// 優先順位の例
let result1 = !isActive && hasPermission;    // (!isActive) && hasPermission
let result2 = isActive || hasPermission && isCompleted; // isActive || (hasPermission && isCompleted)

// 実用的な例
let userLoggedIn: boolean = true;
let formValid: boolean = false;
let hasData: boolean = true;

// 優先順位を考慮した条件
let canSubmit = userLoggedIn && formValid || hasData; // (userLoggedIn && formValid) || hasData
```

## 重要なポイント
1. **優先順位**: ! > && > ||の順序
2. **括弧**: 優先順位を制御するために括弧を使用
3. **実用性**: 複雑な条件式の理解に重要

## 次のステップ
次回は、論理演算子の組み合わせについて学習します。
