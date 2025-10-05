# #002 「string型の宣言 - let name: string」

## 概要
TypeScript v5.9でstring型の変数を宣言する基本的な方法を学習します。型注釈を使用して明示的に型を指定する方法を理解します。

## 学習目標
- string型の変数宣言の基本構文を理解する
- 型注釈の役割と重要性を理解する
- 宣言と代入の違いを理解する

## 画面表示用コード

```typescript
// 型注釈での宣言
let name: string;
let email: string;
let message: string;

// 後で値を代入
name = "Alice";
email = "alice@example.com";
message = "Hello, TypeScript!";

// 型チェックが効く
// name = 123; // エラー
```

## 重要なポイント
1. **型注釈**: `: string` で型を明示的に指定
2. **未初期化**: 宣言だけでは値はundefined
3. **型安全性**: 宣言時に型を指定することで、後で型チェックが行われる

## 次のステップ
次回は、string型への代入について詳しく学習します。