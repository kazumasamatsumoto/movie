# #065 「startsWith(prefix)」

## 概要
TypeScript v5.9のstartsWith()について学習します。文字列が指定した文字列で始まるかを判定するメソッドを理解します。

## 学習目標
- startsWith()の基本使用方法を理解する
- 接頭辞チェックの動作を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// startsWith()の使用例
let url: string = "https://example.com";
let filePath: string = "/home/user/documents/file.txt";
let message: string = "Hello, World!";

// 接頭辞チェック
let isHttps: boolean = url.startsWith("https://"); // true
let isAbsolute: boolean = filePath.startsWith("/"); // true
let startsWithHello: boolean = message.startsWith("Hello"); // true

// 実用的な例
let userInput: string = "admin@example.com";
let isAdmin: boolean = userInput.startsWith("admin"); // true

let apiEndpoint: string = "/api/users";
let isApiRoute: boolean = apiEndpoint.startsWith("/api"); // true
```

## 重要なポイント
1. **接頭辞チェック**: 文字列の開始部分をチェック
2. **戻り値**: boolean型
3. **実用性**: URLやファイルパスの判定に活用

## 次のステップ
次回は、endsWith()について学習します。