# #019 「空文字列 - ""と''」

## 概要
TypeScript v5.9の空文字列について学習します。文字が含まれていない文字列の概念と使用方法を理解します。

## 学習目標
- 空文字列の基本概念を理解する
- 初期値としての使用方法を理解する
- 条件判定での活用方法を理解する

## 画面表示用コード

```typescript
// 空文字列の例
let emptyString1: string = "";
let emptyString2: string = '';
let name: string = "";
let description: string = '';

// 実用的な例
let userInput: string = "";
let searchQuery: string = '';
let errorMessage: string = "";
let successMessage: string = '';

// 条件判定での使用
if (userInput === "") {
  console.log("入力が空です");
}

if (searchQuery.length === 0) {
  console.log("検索クエリが設定されていません");
}
```

## 重要なポイント
1. **空文字列**: 文字が含まれていない文字列
2. **初期値**: フォームや変数の初期化に使用
3. **条件判定**: 入力チェックや状態確認に活用

## 次のステップ
次回は、文字列リテラルの型推論について学習します。