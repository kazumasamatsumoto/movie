# #004 「string型の初期化 - let name: string = "Alice"」

## 概要
TypeScript v5.9のstring型の変数を宣言と同時に初期化する方法を学習します。一行で宣言、型指定、初期値を設定する効率的な方法を理解します。

## 学習目標
- 変数の初期化の基本構文を理解する
- 初期化の利点を理解する
- 適切な初期化方法を習得する

## 画面表示用コード

```typescript
// 初期化の基本
let name: string = "Alice";
let email: string = "alice@example.com";
let message: string = "Hello, TypeScript!";

// 空文字列の初期化
let empty: string = "";

// 即座に使用可能
console.log(name.toUpperCase()); // "ALICE"
console.log(message.length);     // 17
```

## 重要なポイント
1. **一行で完結**: 宣言、型指定、初期化を同時に実行
2. **未定義回避**: 初期化によりundefined状態を避けられる
3. **意図の明確化**: コードの意図が明確になる

## 次のステップ
次回は、型推論を使ったより簡潔な書き方について学習します。