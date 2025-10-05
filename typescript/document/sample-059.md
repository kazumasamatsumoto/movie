# #059 「indexOf(searchString)」

## 概要
TypeScript v5.9のindexOf()について学習します。指定した文字列が最初に出現する位置のインデックスを取得するメソッドを理解します。

## 学習目標
- indexOf()の基本使用方法を理解する
- 文字列検索の動作を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// indexOf()の使用例
let message: string = "Hello, World!";
let text: string = "TypeScript is great";

// 文字列の検索
let index1: number = message.indexOf("World"); // 7
let index2: number = message.indexOf("Hello"); // 0
let index3: number = text.indexOf("Script"); // 4

// 実用的な例
let userEmail: string = "alice@example.com";
let atIndex: number = userEmail.indexOf("@"); // 5
let domainStart: number = userEmail.indexOf("example"); // 6

let productName: string = "TypeScript Handbook";
let bookIndex: number = productName.indexOf("Book"); // -1（見つからない）
```

## 重要なポイント
1. **文字列検索**: 指定した文字列の位置を検索
2. **戻り値**: 見つかった場合はインデックス、見つからない場合は-1
3. **実用性**: 文字列の解析に活用

## 次のステップ
次回は、indexOf()の戻り値について学習します。