# #023 「変数の埋め込み - ${variable}」

## 概要
TypeScript v5.9の変数埋め込みについて学習します。${変数名}の形式で変数を文字列に埋め込む方法を理解します。

## 学習目標
- 変数埋め込みの基本構文を理解する
- 様々な型の変数埋め込みを理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// 変数埋め込みの例
let firstName: string = "Alice";
let lastName: string = "Smith";
let age: number = 30;
let isVip: boolean = true;

// 文字列変数の埋め込み
let fullName: string = `${firstName} ${lastName}`;
let ageMessage: string = `Age: ${age}`;
let vipStatus: string = `VIP: ${isVip}`;

// 実用的な例
let productName: string = "TypeScript学習本";
let price: number = 2980;
let description: string = `${productName} - ¥${price}`;
```

## 重要なポイント
1. **構文**: ${変数名}で変数を埋め込み
2. **型の自動変換**: 数値や真偽値も文字列に変換
3. **複数変数**: 一つのテンプレート内で複数変数を使用可能

## 次のステップ
次回は、式の埋め込みについて学習します。