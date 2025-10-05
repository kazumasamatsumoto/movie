# #008 「string型の変数宣言 - varは使わない理由」

## 概要
TypeScript v5.9でstring型を宣言する際に、varを使わない理由について学習します。letとconstの利点と、varの問題点を理解します。

## 学習目標
- varの問題点を理解する
- letとconstの利点を理解する
- 適切な変数宣言方法を習得する

## 画面表示用コード

```typescript
// varの問題（避けるべき）
var name: string = "Alice";
if (true) {
  var name: string = "Bob"; // 同じスコープで再宣言
}

// letの改善（推奨）
let message: string = "Hello";
if (true) {
  let message: string = "World"; // ブロックスコープ
}
console.log(message); // "Hello"
```

## 重要なポイント
1. **varの問題**: 関数スコープ、ホイスティング、再宣言可能
2. **letの利点**: ブロックスコープ、再宣言不可、予測可能な動作
3. **推奨**: letまたはconstを使用

## 次のステップ
次回は、string型とundefinedの関係について学習します。