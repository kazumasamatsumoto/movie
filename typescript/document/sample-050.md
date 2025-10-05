# #050 「String型使用禁止ルール」

## 概要
TypeScript v5.9のString型使用禁止ルールについて学習します。String型の使用を避けるべき理由とルールを理解します。

## 学習目標
- String型使用禁止ルールを理解する
- 推奨される使用方法を理解する
- チーム開発での一貫性を理解する

## 画面表示用コード

```typescript
// String型使用禁止ルール

// ❌ 禁止：String型の使用
// let name: String = new String("Alice");
// let message: String = new String("Hello");

// ✅ 推奨：string型の使用
let name: string = "Alice";
let message: string = "Hello";

// ✅ 推奨：型推論の活用
let userName = "Bob"; // string型と推論
let userEmail = "bob@example.com"; // string型と推論

// 実用的な例
let componentProps = {
  title: "ユーザー管理",
  description: "ユーザー情報の管理画面"
};
let pageTitle: string = componentProps.title;
```

## 重要なポイント
1. **禁止**: String型の使用
2. **推奨**: string型の使用
3. **一貫性**: チーム開発での統一

## 次のステップ
次回は、toUpperCase()について学習します。