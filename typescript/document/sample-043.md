# #043 「String型の宣言 - 避けるべき」

## 概要
TypeScript v5.9のString型宣言について学習します。String型はオブジェクト型で、使用を避けるべき理由を理解します。

## 学習目標
- String型の宣言方法を理解する
- String型を避けるべき理由を理解する
- 型安全性の重要性を理解する

## 画面表示用コード

```typescript
// String型（避けるべき）
// let nameObj: String = new String("Alice"); // 非推奨
// let messageObj: String = new String("Hello"); // 非推奨

// 正しい方法：string型を使用
let name: string = "Alice";
let message: string = "Hello";

// 型の違い
console.log(typeof name);        // "string"
// console.log(typeof nameObj);  // "object"

// 実用的な例
let userName: string = "Bob";
let userRole: string = "admin";
let userInfo: string = `${userName} (${userRole})`;
```

## 重要なポイント
1. **String型**: オブジェクト型（非推奨）
2. **問題点**: パフォーマンスと型の不一致
3. **推奨**: string型の使用

## 次のステップ
次回は、Stringコンストラクタについて学習します。