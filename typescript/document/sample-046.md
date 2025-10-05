# #046 「Stringからstringへ - valueOf()」

## 概要
TypeScript v5.9のStringからstringへの変換について学習します。Stringオブジェクトをプリミティブのstring型に変換する方法を理解します。

## 学習目標
- Stringからstringへの変換方法を理解する
- valueOf()メソッドの使用方法を理解する
- String()関数の使用方法を理解する

## 画面表示用コード

```typescript
// Stringからstringへの変換

// 1. valueOf()メソッド
// let strObj = new String("Hello");
// let str: string = strObj.valueOf(); // string型に変換

// 2. String()関数
// let strObj = new String("Hello");
// let str: string = String(strObj); // string型に変換

// 3. 文字列リテラル（推奨）
let str: string = "Hello"; // 最初からstring型

// 実用的な例
let userData = {
  name: "Alice",
  email: "alice@example.com"
};

let userName: string = String(userData.name);
let userEmail: string = String(userData.email);
```

## 重要なポイント
1. **valueOf()**: Stringオブジェクトをstring型に変換
2. **String()関数**: 型変換関数
3. **推奨**: 最初からstring型を使用

## 次のステップ
次回は、自動ボックス化について学習します。