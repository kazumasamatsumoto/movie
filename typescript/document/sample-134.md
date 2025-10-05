# #134 「特殊な数値のベストプラクティス」

## 概要
TypeScript v5.9の特殊な数値のベストプラクティスについて学習します。InfinityやNaNを適切に扱う方法を理解します。

## 学習目標
- 特殊な数値の適切な扱い方を理解する
- ベストプラクティスを理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// 特殊な数値のベストプラクティス

// 1. 適切な判定関数の使用
let value: number = parseFloat("abc");
if (Number.isNaN(value)) {
  console.log("無効な数値です");
}

// 2. 有限数チェック
let result: number = 1 / 0;
if (Number.isFinite(result)) {
  console.log("有効な数値です");
} else {
  console.log("無限大またはNaNです");
}

// 3. 安全整数チェック
let largeNumber: number = 9007199254740992;
if (Number.isSafeInteger(largeNumber)) {
  console.log("安全な整数です");
}
```

## 重要なポイント
1. **適切な判定**: Number.isNaN()などの厳密な関数を使用
2. **有限数チェック**: Number.isFinite()で有効性を確認
3. **安全整数**: 大きな数値は安全整数かチェック

## 次のステップ
次回は、特殊な数値まとめについて学習します。