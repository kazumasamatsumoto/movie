# #163 「==と===での比較」

## 概要
TypeScript v5.9の==と===での比較について学習します。Numberとnumberの比較における違いを理解します。

## 学習目標
- ==と===の違いを理解する
- Numberとnumberの比較結果を理解する
- 適切な比較方法を理解する

## 画面表示用コード

```typescript
// ==と===での比較

// number型同士の比較
let num1: number = 30;
let num2: number = 30;
console.log(num1 === num2); // true
console.log(num1 == num2);  // true

// Numberオブジェクトとの比較
// let numObj = new Number(30);
// console.log(num1 === numObj); // false（型が異なる）
// console.log(num1 == numObj);  // true（型変換される）

// 実用的な例
let userAge: number = 25;
let expectedAge: number = 25;
console.log(userAge === expectedAge); // true

// 型安全な比較
if (userAge === expectedAge) {
  console.log("年齢が一致します");
}
```

## 重要なポイント
1. **===比較**: 型も含めて厳密に比較
2. **==比較**: 型変換を行って比較
3. **推奨**: ===を使用して型安全性を保つ

## 次のステップ
次回は、なぜnumberを使うべきかについて学習します。
