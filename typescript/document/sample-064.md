# #064 「includes()の型」

## 概要
TypeScript v5.9のincludes()の型について学習します。includes()が常にboolean型を返すことを理解します。

## 学習目標
- includes()の戻り値の型を理解する
- 型推論の動作を理解する
- 型安全性の重要性を理解する

## 画面表示用コード

```typescript
// includes()の型
let message: string = "Hello, World!";
let result: boolean = message.includes("World"); // boolean型

// 型推論でもboolean型
let inferred = "TypeScript".includes("Script"); // boolean型と推論

// 真偽値の例
let hasHello: boolean = message.includes("Hello"); // true
let hasTypeScript: boolean = message.includes("TypeScript"); // false

// 実用的な例
let userInput: string = "alice@example.com";
let isValidEmail: boolean = userInput.includes("@") && userInput.includes(".");

// 型チェック
console.log(typeof isValidEmail); // "boolean"
```

## 重要なポイント
1. **戻り値の型**: 常にboolean型
2. **型推論**: 自動的にboolean型と推論
3. **型安全性**: TypeScriptが型を保証

## 次のステップ
次回は、startsWith()について学習します。