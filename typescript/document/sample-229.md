# #229 「ANDと型の関係」

## 概要
TypeScript v5.9のANDと型の関係について学習します。&&演算子での型の関係と推論の仕組みを理解します。

## 学習目標
- ANDと型の関係を理解する
- 型推論のルールを理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// ANDと型の関係
let isActive: boolean = true;
let hasPermission: boolean = false;
let userName: string = "John";
let userAge: number = 25;

// 型の関係
let result1: boolean = isActive && hasPermission; // boolean && boolean = boolean
let result2: string = isActive && userName;       // boolean && string = string
let result3: number = isActive && userAge;        // boolean && number = number

// 実用的な例
let userLoggedIn: boolean = true;
let userData: string = "user123";
let displayData: string = userLoggedIn && userData; // string型
```

## 重要なポイント
1. **型の関係**: 左側の型と右側の型の組み合わせで結果の型が決まる
2. **boolean && boolean**: 結果はboolean型
3. **boolean && その他**: 結果は右側の型

## 次のステップ
次回は、論理和ORについて学習します。
