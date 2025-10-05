# #020 「文字列リテラルの型推論」

## 概要
TypeScript v5.9の文字列リテラル型推論について学習します。文字列リテラルから自動的に型を推論する機能を理解します。

## 学習目標
- 文字列リテラル型推論の基本を理解する
- letとconstでの型推論の違いを理解する
- 型の精度の重要性を理解する

## 画面表示用コード

```typescript
// letでの型推論 - string型
let message = "Hello"; // string型と推論
let name = "Alice";    // string型と推論

// constでの型推論 - リテラル型
const API_URL = "https://api.example.com"; // "https://api.example.com"型と推論
const VERSION = "1.0.0"; // "1.0.0"型と推論

// 実用的な例
let userName = "ずんだもん"; // string型
const APP_NAME = "TypeScript学習アプリ"; // "TypeScript学習アプリ"型

// 型の違い
// message = "World"; // OK (string型)
// API_URL = "https://new-api.com"; // エラー (リテラル型)
```

## 重要なポイント
1. **let**: string型に推論（汎用的な文字列型）
2. **const**: リテラル型に推論（特定の文字列型）
3. **型の精度**: constの方がより精密な型推論

## 次のステップ
次回は、テンプレートリテラルについて学習します。