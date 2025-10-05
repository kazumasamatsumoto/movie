# #182 「toPrecision()メソッド」

## 概要
TypeScript v5.9のtoPrecision()メソッドについて学習します。数値を指定した有効桁数で文字列に変換するメソッドの使用方法を理解します。

## 学習目標
- toPrecision()メソッドの基本を理解する
- 有効桁数の指定方法を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// toPrecision()メソッド
let num: number = 3.14159;

let precision1: string = num.toPrecision(3); // "3.14"
let precision2: string = num.toPrecision(5); // "3.1416"
let precision3: string = num.toPrecision(2); // "3.1"

// 実用的な例
let largeNumber: number = 123456.789;
let display1: string = largeNumber.toPrecision(4); // "1.235e+5"
let display2: string = largeNumber.toPrecision(8); // "123456.79"
```

## 重要なポイント
1. **有効桁数**: 全体の有効桁数を指定
2. **科学記法**: 大きな数値は科学記法で表示
3. **実用性**: 数値の精度制御に活用

## 次のステップ
次回は、イプシロン比較について学習します。
