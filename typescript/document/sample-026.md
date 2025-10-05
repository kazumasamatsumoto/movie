# #026 「オブジェクトプロパティ - ${user.name}」

## 概要
TypeScript v5.9のオブジェクトプロパティ埋め込みについて学習します。${}内でオブジェクトのプロパティにアクセスして埋め込む機能を理解します。

## 学習目標
- オブジェクトプロパティ埋め込みの基本を理解する
- ドット記法でのアクセス方法を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// オブジェクトプロパティ埋め込みの例
let user = {
  name: "Alice",
  age: 30,
  email: "alice@example.com",
  isActive: true
};

// プロパティの埋め込み
let userInfo: string = `Name: ${user.name}`;
let userAge: string = `Age: ${user.age}`;
let userEmail: string = `Email: ${user.email}`;
let userStatus: string = `Status: ${user.isActive ? "Active" : "Inactive"}`;

// 実用的な例
let product = {
  name: "TypeScript学習本",
  price: 2980,
  category: "技術書"
};

let productInfo: string = `${product.name} (${product.category}) - ¥${product.price}`;
```

## 重要なポイント
1. **ドット記法**: ${object.property}でプロパティにアクセス
2. **型の自動変換**: プロパティの値が文字列に変換
3. **ネスト**: オブジェクトの任意のプロパティにアクセス可能

## 次のステップ
次回は、配列要素の埋め込みについて学習します。