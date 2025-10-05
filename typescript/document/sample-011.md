# #011 「ダブルクォート文字列 - "hello"」

## 概要
TypeScript v5.9のダブルクォート文字列について学習します。ダブルクォートで囲まれた文字列リテラルの使用方法を理解します。

## 学習目標
- ダブルクォート文字列の基本を理解する
- 文字列リテラルの記述方法を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// ダブルクォート文字列
let message: string = "Hello, World!";
let name: string = "Alice";
let description: string = "TypeScript学習中";

// 実用的な例
let apiUrl: string = "https://api.example.com";
let errorMessage: string = "エラーが発生しました";
let successMessage: string = "処理が完了しました";

// 文字列の結合
let greeting: string = "こんにちは、" + name + "さん！";
let fullMessage: string = message + " " + description;
```

## 重要なポイント
1. **ダブルクォート**: "で囲まれた文字列リテラル
2. **一般的な使用**: 最も一般的な文字列記述方法
3. **実用性**: テンプレートやプロパティに活用

## 次のステップ
次回は、シングルクォート文字列について学習します。