# #067 「substring(start, end)」

## 概要
TypeScript v5.9のsubstring()について学習します。指定した範囲の文字列を抽出するメソッドを理解します。

## 学習目標
- substring()の基本使用方法を理解する
- 開始と終了位置の指定方法を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// substring()の使用例
let message: string = "Hello, World!";
let text: string = "TypeScript is great";

// 部分文字列の抽出
let hello: string = message.substring(0, 5); // "Hello"
let world: string = message.substring(7, 12); // "World"
let script: string = text.substring(4, 10); // "Script"

// 実用的な例
let userEmail: string = "alice@example.com";
let username: string = userEmail.substring(0, 5); // "alice"
let domain: string = userEmail.substring(6); // "example.com"

let filePath: string = "/home/user/file.txt";
let fileName: string = filePath.substring(filePath.lastIndexOf("/") + 1); // "file.txt"
```

## 重要なポイント
1. **範囲指定**: 開始位置と終了位置を指定
2. **部分抽出**: 指定範囲の文字列を取得
3. **実用性**: 文字列の解析に活用

## 次のステップ
次回は、substring()の型について学習します。