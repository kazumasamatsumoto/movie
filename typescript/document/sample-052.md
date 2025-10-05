# #052 「toUpperCase()の型」

## 概要
TypeScript v5.9のtoUpperCase()の型について学習します。toUpperCase()が常にstring型を返すことを理解します。

## 学習目標
- toUpperCase()の戻り値の型を理解する
- 型推論の動作を理解する
- 型安全性の重要性を理解する

## 画面表示用コード

```typescript
// toUpperCase()の型
let name: string = "alice";
let result: string = name.toUpperCase(); // string型

// 型推論でもstring型
let inferred = "hello".toUpperCase(); // string型と推論

// 実用的な例
let userInput: string = "john doe";
let normalizedInput: string = userInput.toUpperCase(); // "JOHN DOE"

let productName: string = "typescript book";
let displayName: string = productName.toUpperCase(); // "TYPESCRIPT BOOK"

// 型チェック
console.log(typeof normalizedInput); // "string"
```

## 重要なポイント
1. **戻り値の型**: 常にstring型
2. **型推論**: 自動的にstring型と推論
3. **型安全性**: TypeScriptが型を保証

## 次のステップ
次回は、toLowerCase()について学習します。