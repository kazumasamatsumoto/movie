# #021 「テンプレートリテラルとは - バッククォート`」

## 概要
TypeScript v5.9のテンプレートリテラルについて学習します。バッククォート`で囲まれた文字列で、変数を埋め込める強力な機能です。

## 学習目標
- テンプレートリテラルの基本概念を理解する
- バッククォートの使用方法を理解する
- 従来の文字列結合との違いを理解する

## 画面表示用コード

```typescript
// テンプレートリテラルの基本
let name: string = "Alice";
let age: number = 30;

// バッククォートで囲む
let message: string = `Hello, ${name}!`;
let info: string = `${name} is ${age} years old`;

// 従来の文字列結合との比較
let oldWay: string = "Hello, " + name + "!";
let newWay: string = `Hello, ${name}!`;

// 実用的な例
let userName: string = "ずんだもん";
let greeting: string = `こんにちは、${userName}さん！`;
```

## 重要なポイント
1. **バッククォート**: `で囲まれた文字列リテラル
2. **変数埋め込み**: ${}で変数を文字列に埋め込み
3. **可読性**: 従来の文字列結合より読みやすい

## 次のステップ
次回は、テンプレートリテラルの基本構文について学習します。