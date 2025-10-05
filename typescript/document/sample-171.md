# #171 「変換失敗時 - NaN」

## 概要
TypeScript v5.9の変換失敗時について学習します。数値変換に失敗した時にNaNが返される仕組みを理解します。

## 学習目標
- 変換失敗時の動作を理解する
- NaNの特徴を理解する
- エラーハンドリングの重要性を理解する

## 画面表示用コード

```typescript
// 変換失敗時 - NaN
let invalidStr: string = "abc";
let emptyStr: string = "";

// 変換失敗
let result1: number = Number(invalidStr);  // NaN
let result2: number = parseInt(invalidStr); // NaN
let result3: number = parseFloat(emptyStr); // NaN

// 実用的な例
let userInput: string = "無効な値";
let userAge: number = Number(userInput);

if (Number.isNaN(userAge)) {
  console.log("無効な数値です");
} else {
  console.log("有効な数値です");
}
```

## 重要なポイント
1. **変換失敗**: 無効な値はNaNになる
2. **NaNチェック**: Number.isNaN()でチェック
3. **エラーハンドリング**: 適切な処理が必要

## 次のステップ
次回は、エラーハンドリングについて学習します。
