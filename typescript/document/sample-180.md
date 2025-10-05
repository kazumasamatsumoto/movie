# #180 「回避方法(2) - ライブラリ」

## 概要
TypeScript v5.9のライブラリによる回避方法について学習します。decimal.jsやbig.jsなどのライブラリを使用する方法を理解します。

## 学習目標
- ライブラリによる回避方法を理解する
- decimal.jsの基本を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// ライブラリによる回避（decimal.jsの例）
// npm install decimal.js
// import { Decimal } from 'decimal.js';

// const a = new Decimal(0.1);
// const b = new Decimal(0.2);
// const sum = a.plus(b);

// console.log(sum.toString()); // "0.3"

// 実用的な例
// const price1 = new Decimal(100.50);
// const price2 = new Decimal(200.25);
// const total = price1.plus(price2);

// console.log(total.toString()); // "300.75"
```

## 重要なポイント
1. **ライブラリ**: decimal.js、big.jsなど
2. **正確性**: 正確な小数計算が可能
3. **実用性**: 金融計算などに活用

## 次のステップ
次回は、toFixed()メソッドについて学習します。
