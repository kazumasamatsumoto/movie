# #109 「number型の範囲 - MAX_VALUE」

## 概要
TypeScript v5.9のnumber型の範囲について学習します。number型が扱える最大値について理解します。

## 学習目標
- number型の最大値を理解する
- Number.MAX_VALUEの使用方法を理解する
- 大きな数値の処理に注意する

## 画面表示用コード

```typescript
// number型の範囲
let maxValue: number = Number.MAX_VALUE;
let minValue: number = Number.MIN_VALUE;

console.log(maxValue); // 1.7976931348623157e+308
console.log(minValue); // 5e-324

// 実用的な例
let largeNumber: number = 1e10;
let smallNumber: number = 1e-10;

// 範囲チェック
if (largeNumber < Number.MAX_VALUE) {
  console.log("安全な範囲内です");
}
```

## 重要なポイント
1. **最大値**: Number.MAX_VALUEで確認可能
2. **範囲チェック**: 大きな数値の処理時に注意
3. **実用性**: 数値計算の安全性確保

## 次のステップ
次回は、number型の最小値について学習します。