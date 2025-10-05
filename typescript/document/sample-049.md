# #049 「なぜstringを使うべきか」

## 概要
TypeScript v5.9のstring型使用理由について学習します。型安全性、パフォーマンス、一貫性の観点からstring型を使用すべき理由を理解します。

## 学習目標
- string型を使用すべき理由を理解する
- 型安全性の利点を理解する
- パフォーマンスの利点を理解する

## 画面表示用コード

```typescript
// string型を使うべき理由

// 1. 型安全性
let userName: string = "Alice";
// userName = 123; // エラー: Type 'number' is not assignable to type 'string'

// 2. パフォーマンス
let message: string = "Hello, World!"; // 軽量なプリミティブ型

// 3. 一貫性
let userData = {
  name: "Bob",
  email: "bob@example.com"
};
let userInfo: string = `${userData.name} (${userData.email})`;

// 4. 予測可能な動作
let str1: string = "Hello";
let str2: string = "Hello";
console.log(str1 === str2); // 常にtrue
```

## 重要なポイント
1. **型安全性**: コンパイル時の型チェック
2. **パフォーマンス**: 軽量なプリミティブ型
3. **一貫性**: 予測可能な動作

## 次のステップ
次回は、String型使用禁止ルールについて学習します。