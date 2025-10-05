# #089 「デバッグ(1) - 型エラーの読み方」

## 概要
TypeScript v5.9のデバッグ(1)について学習します。TypeScriptの型エラーメッセージを理解する方法を理解します。

## 学習目標
- 型エラーメッセージの読み方を理解する
- よくある型エラーの種類を理解する
- エラーの解決方法を理解する

## 画面表示用コード

```typescript
// デバッグ(1) - 型エラーの読み方

// 型の不一致エラー
let name: string = "Alice";
// name = 123; // エラー: Type 'number' is not assignable to type 'string'

// 未定義変数エラー
// let message: string;
// console.log(message); // エラー: Variable 'message' is used before being assigned

// 正しい方法
let userName: string = "Bob";
let userMessage: string = "Hello, " + userName;
console.log(userMessage);
```

## 重要なポイント
1. **型エラー**: 型の不一致によるエラー
2. **未定義エラー**: 初期化前の変数使用
3. **解決方法**: 適切な型指定と初期化

## 次のステップ
次回は、デバッグ(2)について学習します。