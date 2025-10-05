# #231 「ORの型推論」

## 概要
TypeScript v5.9のORの型推論について学習します。||演算子での型推論の仕組みを理解します。

## 学習目標
- ORの型推論の仕組みを理解する
- 型推論のルールを理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// ORの型推論
let isActive: boolean = true;
let hasPermission: boolean = false;
let userName: string = "John";
let defaultName: string = "Guest";

// 型推論の例
let result1 = isActive || hasPermission; // boolean型
let result2 = userName || defaultName;   // string型
let result3 = hasPermission || userName; // string型

// 実用的な例
let userLoggedIn: boolean = true;
let userData: string = "user123";
let displayData = userLoggedIn || userData; // boolean型
```

## 重要なポイント
1. **型推論**: 左側の値によって結果の型が決まる
2. **左側がtruthy**: 結果は左側の型
3. **左側がfalsy**: 結果は右側の型

## 次のステップ
次回は、ORの短絡評価について学習します。
