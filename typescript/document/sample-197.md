# #197 「間違い(2) - NaNチェック」

## 概要
TypeScript v5.9のNaNチェックの間違いについて学習します。NaNを===で比較する間違いを理解します。

## 学習目標
- NaNチェックの間違いを理解する
- NaNの特殊な性質を理解する
- 適切なNaNチェック方法を理解する

## 画面表示用コード

```typescript
// 間違い(2) - NaNチェック
let invalidNumber: number = Number("abc");

// ❌ 間違い
console.log(invalidNumber === NaN); // false

// ✅ 正しい方法
console.log(Number.isNaN(invalidNumber)); // true

// 実用的な例
function validateNumber(value: unknown): boolean {
  if (typeof value === "number") {
    return !Number.isNaN(value);
  }
  return false;
}

let userInput: unknown = "abc";
let converted: number = Number(userInput);
console.log(validateNumber(converted)); // false
```

## 重要なポイント
1. **間違い**: NaNを===で比較
2. **問題**: NaNは自分自身とも等しくない
3. **解決**: Number.isNaN()を使用

## 次のステップ
次回は、間違い(3)について学習します。
