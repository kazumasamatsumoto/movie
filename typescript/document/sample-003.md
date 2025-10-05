# #003 「string型への代入 - name = "Hello"」

## 概要
TypeScript v5.9のstring型への代入について学習します。文字列リテラルを代入する方法と型チェック機能を理解します。

## 学習目標
- string型変数への代入方法を理解する
- TypeScriptの型チェック機能を理解する
- 代入可能な値と不可能な値を区別する

## 画面表示用コード

```typescript
// string型への代入
let message: string;

// 文字列の代入
message = "Hello";        // OK
message = "World";        // OK
message = "こんにちは";    // OK

// 型エラーの例
// message = 123;         // エラー: Type 'number' is not assignable to type 'string'
// message = true;        // エラー: Type 'boolean' is not assignable to type 'string'

// 再代入
message = "Hello";
message = "Goodbye";
```

## 重要なポイント
1. **型チェック**: TypeScriptが代入時に型をチェック
2. **再代入可能**: letで宣言した変数は再代入可能
3. **文字列リテラル**: 文字列のみ使用可能

## 次のステップ
次回は、string型の初期化について学習します。

