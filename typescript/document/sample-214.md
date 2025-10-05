# #214 「boolean型の用途」

## 概要
TypeScript v5.9のboolean型の用途について学習します。boolean型が使用される様々な場面を理解します。

## 学習目標
- boolean型の用途を理解する
- 様々な使用場面を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// boolean型の用途

// 1. 条件分岐
let isActive: boolean = true;
if (isActive) {
  console.log("アクティブです");
}

// 2. フラグ管理
let hasPermission: boolean = true;
let canEdit: boolean = false;

// 3. 状態管理
let userLoggedIn: boolean = true;
let formValid: boolean = false;

// 4. バリデーション
let isEmailValid: boolean = true;
let isPasswordValid: boolean = false;
```

## 重要なポイント
1. **条件分岐**: if文やwhile文で使用
2. **フラグ管理**: アプリケーションの状態を管理
3. **状態管理**: ユーザーの状態を管理
4. **バリデーション**: 入力値の検証

## 次のステップ
次回は、基本まとめについて学習します。
