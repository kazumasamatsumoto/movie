# #055 「charAt(index) - 文字取得」

## 概要
TypeScript v5.9のcharAt()について学習します。指定したインデックスの文字を取得するメソッドの使用方法を理解します。

## 学習目標
- charAt()の基本使用方法を理解する
- インデックスでの文字取得を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// charAt()の使用例
let name: string = "Alice";
let message: string = "Hello, World!";

// 文字の取得
let firstChar: string = name.charAt(0); // "A"
let secondChar: string = name.charAt(1); // "l"
let lastChar: string = name.charAt(name.length - 1); // "e"

// 実用的な例
let userName: string = "Bob";
let userInitial: string = userName.charAt(0); // "B"

let productCode: string = "ABC123";
let category: string = productCode.charAt(0); // "A"
let subCategory: string = productCode.charAt(1); // "B"
```

## 重要なポイント
1. **インデックス**: 0から始まる位置指定
2. **文字取得**: 指定位置の文字を取得
3. **実用性**: 文字列の解析に活用

## 次のステップ
次回は、charAt()の型について学習します。