# #071 「string[]型とは」

## 概要
TypeScript v5.9のstring[]型について学習します。文字列の配列を扱う型として、複数の文字列をまとめて管理する方法を理解します。

## 学習目標
- string[]型の基本概念を理解する
- 配列型の使用方法を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// string[]型の例
let names: string[] = ["Alice", "Bob", "Charlie"];
let emails: string[] = ["alice@example.com", "bob@example.com"];
let tags: string[] = ["TypeScript", "JavaScript", "Web開発"];

// 実用的な例
let userRoles: string[] = ["admin", "user", "guest"];
let productCategories: string[] = ["本", "ペン", "ノート"];
let apiEndpoints: string[] = ["/api/users", "/api/products"];
```

## 重要なポイント
1. **配列型**: 複数の文字列をまとめて管理
2. **型安全性**: 配列内の要素はすべてstring型
3. **実用性**: リスト表示やデータ管理に活用

## 次のステップ
次回は、string配列の宣言について学習します。