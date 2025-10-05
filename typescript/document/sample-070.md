# #070 「split(separator)」

## 概要
TypeScript v5.9のsplit()について学習します。指定した区切り文字で文字列を配列に分割するメソッドを理解します。

## 学習目標
- split()の基本使用方法を理解する
- 区切り文字の指定方法を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// split()の使用例
let message: string = "Hello,World,TypeScript";
let csv: string = "Alice,30,Tokyo";
let words: string = "Hello World TypeScript";

// 文字列の分割
let parts: string[] = message.split(","); // ["Hello", "World", "TypeScript"]
let userData: string[] = csv.split(","); // ["Alice", "30", "Tokyo"]
let wordArray: string[] = words.split(" "); // ["Hello", "World", "TypeScript"]

// 実用的な例
let email: string = "alice@example.com";
let emailParts: string[] = email.split("@"); // ["alice", "example.com"]
```

## 重要なポイント
1. **文字列分割**: 区切り文字で文字列を分割
2. **戻り値**: string[]型の配列
3. **実用性**: CSVデータやURLの解析に活用

## 次のステップ
次回は、文字列配列について学習します。