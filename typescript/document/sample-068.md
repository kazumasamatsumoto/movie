# #068 「substring()の型」

## 概要
TypeScript v5.9のsubstring()の型について学習します。substring()が常にstring型を返すことを理解します。

## 学習目標
- substring()の戻り値の型を理解する
- 型推論の動作を理解する
- 型安全性の重要性を理解する

## 画面表示用コード

```typescript
// substring()の型
let message: string = "Hello, World!";
let result: string = message.substring(0, 5); // string型

// 型推論でもstring型
let inferred = "TypeScript".substring(0, 4); // string型と推論

// 戻り値の例
let hello: string = message.substring(0, 5); // "Hello"
let empty: string = message.substring(10, 5); // ""（空文字列）

// 実用的な例
let userInput: string = "alice@example.com";
let username: string = userInput.substring(0, 5); // "alice"

// 型チェック
console.log(typeof username); // "string"
```

## 重要なポイント
1. **戻り値の型**: 常にstring型
2. **型推論**: 自動的にstring型と推論
3. **型安全性**: TypeScriptが型を保証

## 次のステップ
次回は、slice()について学習します。