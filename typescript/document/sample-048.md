# #048 「==と===での比較」

## 概要
TypeScript v5.9の==と===での比較について学習します。Stringとstringの比較における型変換の違いを理解します。

## 学習目標
- ==と===の基本的な違いを理解する
- Stringとstringの比較結果を理解する
- 型変換の影響を理解する

## 画面表示用コード

```typescript
// ==と===での比較

// string型同士の比較
let str1: string = "Hello";
let str2: string = "Hello";
console.log(str1 === str2); // true
console.log(str1 == str2);  // true

// Stringオブジェクトとの比較
// let strObj = new String("Hello");
// console.log(str1 === strObj); // false（型が異なる）
// console.log(str1 == strObj);  // true（型変換される）

// 実用的な例
let userName: string = "Alice";
let userInput: string = "Alice";
console.log(userName === userInput); // true

// 型安全な比較
if (userName === userInput) {
  console.log("ユーザー名が一致します");
}
```

## 重要なポイント
1. **===**: 型変換なしの厳密な比較
2. **==**: 型変換ありの緩い比較
3. **型安全性**: ===の使用を推奨

## 次のステップ
次回は、なぜstringを使うべきかについて学習します。