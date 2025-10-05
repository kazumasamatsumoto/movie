# #181 「toFixed()メソッド」

## 概要
TypeScript v5.9のtoFixed()メソッドについて学習します。数値を指定した桁数で文字列に変換するメソッドの使用方法を理解します。

## 学習目標
- toFixed()メソッドの基本を理解する
- 桁数指定の方法を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// toFixed()メソッド
let num: number = 3.14159;

let fixed1: string = num.toFixed(2); // "3.14"
let fixed2: string = num.toFixed(4); // "3.1416"
let fixed3: string = num.toFixed(0); // "3"

// 実用的な例
let price: number = 1500.99;
let displayPrice: string = price.toFixed(2); // "1500.99"

let userAge: number = 25.5;
let displayAge: string = userAge.toFixed(0); // "26"
```

## 重要なポイント
1. **桁数指定**: 小数点以下の桁数を指定
2. **文字列変換**: 数値を文字列に変換
3. **実用性**: 表示フォーマットに活用

## 次のステップ
次回は、toPrecision()メソッドについて学習します。
