# #066 「endsWith(suffix)」

## 概要
TypeScript v5.9のendsWith()について学習します。文字列が指定した文字列で終わるかを判定するメソッドを理解します。

## 学習目標
- endsWith()の基本使用方法を理解する
- 接尾辞チェックの動作を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// endsWith()の使用例
let fileName: string = "document.pdf";
let url: string = "https://example.com/page.html";
let message: string = "Hello, World!";

// 接尾辞チェック
let isPdf: boolean = fileName.endsWith(".pdf"); // true
let isHtml: boolean = url.endsWith(".html"); // true
let endsWithWorld: boolean = message.endsWith("World!"); // true

// 実用的な例
let userEmail: string = "alice@example.com";
let isComDomain: boolean = userEmail.endsWith(".com"); // true

let imageFile: string = "photo.jpg";
let isImage: boolean = imageFile.endsWith(".jpg") || imageFile.endsWith(".png");
```

## 重要なポイント
1. **接尾辞チェック**: 文字列の終了部分をチェック
2. **戻り値**: boolean型
3. **実用性**: ファイル拡張子やURLの判定に活用

## 次のステップ
次回は、substring()について学習します。