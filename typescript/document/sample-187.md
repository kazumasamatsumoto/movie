# #187 「BigIntとnumberの違い」

## 概要
TypeScript v5.9のBigIntとnumberの違いについて学習します。BigIntとnumber型の特徴と使い分けを理解します。

## 学習目標
- BigIntとnumberの違いを理解する
- 精度の違いを理解する
- 適切な型選択を理解する

## 画面表示用コード

```typescript
// BigIntとnumberの違い
let numberValue: number = 1234567890123456789;
let bigIntValue: bigint = 1234567890123456789n;

// 精度の違い
console.log(numberValue); // 1234567890123456800 (精度が失われる)
console.log(bigIntValue); // 1234567890123456789n (精度が保たれる)

// 型の違い
console.log(typeof numberValue); // "number"
console.log(typeof bigIntValue); // "bigint"

// 実用的な例
let userId: bigint = 1234567890123456789n;
let userAge: number = 25;
```

## 重要なポイント
1. **精度**: BigIntは任意精度、numberは固定精度
2. **制限**: BigIntは整数のみ、numberは小数も扱える
3. **使い分け**: 用途に応じて適切な型を選択

## 次のステップ
次回は、BigIntの使用例について学習します。
