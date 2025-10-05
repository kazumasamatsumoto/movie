# #028 「複数の変数埋め込み - `${first} ${last}`」

## 概要
TypeScript v5.9の複数変数埋め込みについて学習します。一つのテンプレートリテラル内で複数の変数を埋め込む機能を理解します。

## 学習目標
- 複数変数埋め込みの基本を理解する
- 複雑な情報の組み合わせ方法を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// 複数変数埋め込みの例
let firstName: string = "Alice";
let lastName: string = "Smith";
let age: number = 30;
let city: string = "Tokyo";

// 複数の変数埋め込み
let fullInfo: string = `${firstName} ${lastName}, ${age} years old, from ${city}`;
let greeting: string = `Hello, ${firstName} ${lastName}! You are ${age} years old.`;

// 実用的な例
let productName: string = "TypeScript学習本";
let price: number = 2980;
let discount: number = 0.1;
let finalPrice: string = `${productName}: ¥${price} (${discount * 100}% off) = ¥${price * (1 - discount)}`;
```

## 重要なポイント
1. **複数埋め込み**: 一つのテンプレート内で複数変数を使用
2. **情報の組み合わせ**: 関連する情報を一つの文字列に統合
3. **計算の組み込み**: 式と変数を組み合わせて使用

## 次のステップ
次回は、テンプレートリテラルの型について学習します。