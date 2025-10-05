# #063 「includes(searchString)」

## 概要
TypeScript v5.9のincludes()について学習します。指定した文字列が含まれているかを判定するメソッドを理解します。

## 学習目標
- includes()の基本使用方法を理解する
- indexOf()との違いを理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// includes()の使用例
let message: string = "Hello, World!";
let text: string = "TypeScript is great";

// 包含チェック
let hasWorld: boolean = message.includes("World"); // true
let hasHello: boolean = message.includes("Hello"); // true
let hasTypeScript: boolean = text.includes("Script"); // true

// 実用的な例
let userEmail: string = "alice@example.com";
let hasAtSymbol: boolean = userEmail.includes("@"); // true
let hasDomain: boolean = userEmail.includes(".com"); // true

let productName: string = "TypeScript Handbook";
let isBook: boolean = productName.includes("Book"); // false
```

## 重要なポイント
1. **包含チェック**: 文字列が含まれているかを判定
2. **戻り値**: boolean型
3. **直感性**: indexOf()より直感的

## 次のステップ
次回は、includes()の型について学習します。