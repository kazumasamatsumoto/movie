# #041 「Stringとstringの基本的な違い」

## 概要
TypeScript v5.9のStringとstringの違いについて学習します。stringはプリミティブ型、Stringはオブジェクト型で、使用すべき型と避けるべき型を理解します。

## 学習目標
- Stringとstringの基本的な違いを理解する
- プリミティブ型とオブジェクト型の違いを理解する
- 適切な型の選択方法を理解する

## 画面表示用コード

```typescript
// string型（推奨）- プリミティブ型
let name: string = "Alice";
let message: string = "Hello, World!";

// String型（非推奨）- オブジェクト型
// let nameObj: String = new String("Alice"); // 避けるべき

// 型の違い
console.log(typeof name);        // "string"
// console.log(typeof nameObj);  // "object"

// 実用的な例
let userName: string = "Bob";
let userEmail: string = "bob@example.com";
let userInfo: string = `${userName} (${userEmail})`;
```

## 重要なポイント
1. **string型**: プリミティブ型（推奨）
2. **String型**: オブジェクト型（非推奨）
3. **型の違い**: typeof演算子で確認可能

## 次のステップ
次回は、string型の宣言について学習します。