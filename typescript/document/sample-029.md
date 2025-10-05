# #029 「テンプレートリテラルの型 - string型」

## 概要
TypeScript v5.9のテンプレートリテラル型について学習します。テンプレートリテラルは常にstring型として扱われることを理解します。

## 学習目標
- テンプレートリテラルの型を理解する
- 型推論の動作を理解する
- 型安全性の重要性を理解する

## 画面表示用コード

```typescript
// テンプレートリテラルの型
let name: string = "Alice";
let age: number = 30;
let isActive: boolean = true;

// すべてstring型になる
let message1: string = `Name: ${name}`;        // string型
let message2: string = `Age: ${age}`;          // string型
let message3: string = `Active: ${isActive}`;  // string型

// 型推論でもstring型
let inferred = `Hello, ${name}!`; // string型と推論

// 実用的な例
let userId: number = 12345;
let userName: string = "Bob";
let userInfo: string = `User ${userId}: ${userName}`;
```

## 重要なポイント
1. **常にstring型**: テンプレートリテラルは必ずstring型
2. **型の自動変換**: 埋め込まれる値は文字列に変換
3. **型安全性**: TypeScriptが型を保証

## 次のステップ
次回は、複数行のテンプレートリテラルについて学習します。