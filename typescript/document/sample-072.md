# #072 「string配列の宣言」

## 概要
TypeScript v5.9のstring配列宣言について学習します。型注釈を使用して配列型を指定する方法を理解します。

## 学習目標
- string配列の宣言方法を理解する
- 型注釈の使用方法を理解する
- 空配列の宣言を理解する

## 画面表示用コード

```typescript
// string配列の宣言
let names: string[] = [];
let emails: string[] = [];
let tags: string[] = [];

// 後で値を代入
names = ["Alice", "Bob", "Charlie"];
emails = ["alice@example.com", "bob@example.com"];

// 実用的な例
let userList: string[] = [];
let productNames: string[] = [];
let errorMessages: string[] = [];
```

## 重要なポイント
1. **型注釈**: `: string[]`で配列型を指定
2. **空配列**: 初期値として空配列を使用
3. **後代入**: 宣言後に値を代入可能

## 次のステップ
次回は、Array<string>記法について学習します。