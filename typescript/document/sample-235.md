# #235 「NOTの型推論」

## 概要
TypeScript v5.9のNOTの型推論について学習します。!演算子での型推論の仕組みを理解します。

## 学習目標
- NOTの型推論の仕組みを理解する
- 型推論のルールを理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// NOTの型推論
let isActive: boolean = true;
let hasPermission: boolean = false;
let userName: string = "John";
let userAge: number = 25;

// 型推論の例
let result1: boolean = !isActive;        // boolean型
let result2: boolean = !hasPermission;   // boolean型
let result3: boolean = !userName;        // boolean型
let result4: boolean = !userAge;         // boolean型

// 実用的な例
let userLoggedIn: boolean = true;
let formValid: boolean = false;
let userLoggedOut: boolean = !userLoggedIn; // boolean型
```

## 重要なポイント
1. **型推論**: !演算子は常にboolean型を返す
2. **一貫性**: 入力の型に関係なくboolean型
3. **実用性**: 型安全な条件の反転

## 次のステップ
次回は、二重否定について学習します。
