# #003 「string型への代入 - name = "Hello"」

## 概要
TypeScript v5.9のstring型の変数に文字列を代入する方法と、型チェック機能について学習します。

## 学習目標
- string型変数への代入方法を理解する
- TypeScriptの型チェック機能を理解する
- 代入可能な値と不可能な値を区別する

## 画面表示用コード

```typescript
// string型変数の宣言
let message: string;

// 文字列の代入
message = "Hello";
message = 'World';
message = `Template`;

// 型エラーの例
// message = 123;    // エラー
// message = true;   // エラー

// 再代入
message = "TypeScript v5.9";
```

## 重要なポイント
1. **型チェック**: TypeScriptが代入時に型をチェック
2. **再代入可能**: letで宣言した変数は再代入可能
3. **文字列リテラル**: ダブルクォート、シングルクォート、バッククォートすべて使用可能

## 次のステップ
次回は、宣言と代入を同時に行う初期化について学習します。