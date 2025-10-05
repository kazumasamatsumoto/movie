# #062 「lastIndexOf()」

## 概要
TypeScript v5.9のlastIndexOf()について学習します。指定した文字列が最後に出現する位置のインデックスを取得するメソッドを理解します。

## 学習目標
- lastIndexOf()の基本使用方法を理解する
- indexOf()との違いを理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// lastIndexOf()の使用例
let message: string = "Hello, World! Hello, TypeScript!";
let text: string = "apple, banana, apple, orange";

// 最後の出現位置
let lastHello: number = message.lastIndexOf("Hello"); // 14
let lastApple: number = text.lastIndexOf("apple"); // 15

// 実用的な例
let filePath: string = "/home/user/documents/file.txt";
let lastSlash: number = filePath.lastIndexOf("/"); // 20
let fileName: string = filePath.substring(lastSlash + 1); // "file.txt"

let userEmail: string = "user.name@example.com";
let lastDot: number = userEmail.lastIndexOf("."); // 18
let extension: string = userEmail.substring(lastDot + 1); // "com"
```

## 重要なポイント
1. **後方検索**: 最後の出現位置を検索
2. **indexOf()との違い**: 最初vs最後の位置
3. **実用性**: ファイル名や拡張子の取得に活用

## 次のステップ
次回は、includes()について学習します。