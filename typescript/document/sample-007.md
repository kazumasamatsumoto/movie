# #007 「string型とリテラル型の違い - "hello" vs string」

## 概要
TypeScript v5.9のstring型とリテラル型の違いについて学習します。汎用的な文字列型と特定の文字列型の使い分けを理解します。

## 学習目標
- string型とリテラル型の基本的な違いを理解する
- 適切な使い分け方法を理解する
- 型の精度の重要性を理解する

## 画面表示用コード

```typescript
// string型 - 任意の文字列
let message: string = "Hello";
message = "World"; // OK
message = "こんにちは"; // OK

// リテラル型 - 特定の文字列のみ
let status: "active" | "inactive" = "active";
// status = "pending"; // エラー: Type '"pending"' is not assignable to type '"active" | "inactive"'

// 実用的な例
let theme: "light" | "dark" = "light";
let language: "ja" | "en" = "ja";
let userRole: "admin" | "user" | "guest" = "user";
```

## 重要なポイント
1. **string型**: 任意の文字列を受け入れる汎用的な型
2. **リテラル型**: 特定の文字列のみを受け入れる精密な型
3. **使い分け**: 用途に応じて適切な型を選択

## 次のステップ
次回は、string型の変数宣言について学習します。

