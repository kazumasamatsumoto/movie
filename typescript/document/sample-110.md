# #110 「number型の最小値 - MIN_VALUE」

## 概要
TypeScript v5.9のnumber型の最小値について学習します。number型が扱える最小の正の値について理解します。

## 学習目標
- number型の最小値を理解する
- Number.MIN_VALUEの使用方法を理解する
- 小さな数値の処理に注意する

## 画面表示用コード

```typescript
// number型の最小値
let minValue: number = Number.MIN_VALUE;
let maxValue: number = Number.MAX_VALUE;

console.log(minValue); // 5e-324
console.log(maxValue); // 1.7976931348623157e+308

// 実用的な例
let tinyNumber: number = 1e-100;
let normalNumber: number = 1e-10;

// 最小値チェック
if (tinyNumber > Number.MIN_VALUE) {
  console.log("最小値より大きいです");
}
```

## 重要なポイント
1. **最小値**: Number.MIN_VALUEで確認可能
2. **範囲チェック**: 小さな数値の処理時に注意
3. **実用性**: 数値計算の精度確保

## 次のステップ
次回は、10進数リテラルについて学習します。