# #022 「基本構文 - `Hello, ${name}`」

## 概要
TypeScript v5.9のテンプレートリテラル基本構文について学習します。`文字列${変数}文字列`の形式で記述する方法を理解します。

## 学習目標
- テンプレートリテラルの基本構文を理解する
- 変数埋め込みの記述方法を理解する
- 様々な型の変数埋め込みを理解する

## 画面表示用コード

```typescript
// 基本構文の例
let name: string = "Alice";
let age: number = 30;
let isActive: boolean = true;

// 変数の埋め込み
let greeting: string = `Hello, ${name}!`;
let ageInfo: string = `Age: ${age}`;
let status: string = `Status: ${isActive ? "Active" : "Inactive"}`;

// 実用的な例
let userName: string = "Bob";
let userRole: string = "admin";
let welcomeMessage: string = `Welcome, ${userName}! Your role is ${userRole}.`;
```

## 重要なポイント
1. **基本構文**: `文字列${変数}文字列`の形式
2. **型の自動変換**: 埋め込まれる値は自動的に文字列に変換
3. **式の埋め込み**: 三項演算子などの式も使用可能

## 次のステップ
次回は、変数の埋め込みについて学習します。