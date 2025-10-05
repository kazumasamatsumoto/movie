# #042 「string型の宣言 - プリミティブ」

## 概要
TypeScript v5.9のstring型宣言について学習します。プリミティブ型としてのstring型の宣言方法と特徴を理解します。

## 学習目標
- string型の宣言方法を理解する
- プリミティブ型の概念を理解する
- 型推論との関係を理解する

## 画面表示用コード

```typescript
// string型の宣言（プリミティブ型）
let name: string = "Alice";
let email: string = "alice@example.com";
let description: string = "TypeScript学習中";

// 型推論でもstring型
let inferred = "Bob"; // string型と推論

// 実用的な例
let componentTitle: string = "ユーザー管理";
let apiEndpoint: string = "/api/users";
let errorMessage: string = "エラーが発生しました";

// プリミティブ型の特徴
console.log(typeof name); // "string"
```

## 重要なポイント
1. **型注釈**: `: string`で型を明示
2. **プリミティブ型**: 基本的なデータ型
3. **型推論**: 文字列リテラルから自動推論

## 次のステップ
次回は、String型の宣言について学習します。