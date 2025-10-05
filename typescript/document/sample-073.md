# #073 「Array<string>記法」

## 概要
TypeScript v5.9のArray<string>記法について学習します。配列型を表す別の書き方として、より明示的な記述方法を理解します。

## 学習目標
- Array<string>記法の基本を理解する
- string[]記法との違いを理解する
- 使い分けの方法を理解する

## 画面表示用コード

```typescript
// Array<string>記法
let names: Array<string> = ["Alice", "Bob", "Charlie"];
let emails: Array<string> = ["alice@example.com", "bob@example.com"];
let tags: Array<string> = ["TypeScript", "JavaScript"];

// string[]記法との比較
let names1: string[] = ["Alice", "Bob"];
let names2: Array<string> = ["Alice", "Bob"];

// 実用的な例
let userRoles: Array<string> = ["admin", "user"];
let productCategories: Array<string> = ["本", "ペン"];
```

## 重要なポイント
1. **Array<T>記法**: より明示的な配列型の記述
2. **機能的な違い**: string[]とArray<string>は同じ
3. **使い分け**: プロジェクトの規約に従う

## 次のステップ
次回は、string配列の初期化について学習します。