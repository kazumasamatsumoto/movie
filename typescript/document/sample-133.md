# #133 「Number.isSafeInteger()」

## 概要
TypeScript v5.9のNumber.isSafeInteger()について学習します。値が安全な整数かどうかを判定する関数の使用方法を理解します。

## 学習目標
- Number.isSafeInteger()の基本を理解する
- 安全な整数の概念を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// Number.isSafeInteger()
let safeInteger: number = 42;
let unsafeInteger: number = Number.MAX_SAFE_INTEGER + 1;

// 安全整数判定
let isSafe1: boolean = Number.isSafeInteger(safeInteger);   // true
let isSafe2: boolean = Number.isSafeInteger(unsafeInteger); // false

// 実用的な例
let userId: number = 12345;
if (Number.isSafeInteger(userId)) {
  console.log("安全な整数IDです");
} else {
  console.log("精度を失う可能性があります");
}
```

## 重要なポイント
1. **安全整数**: 精度を失わずに表現できる整数
2. **範囲**: Number.MAX_SAFE_INTEGERまでの範囲
3. **実用性**: 大きな数値の処理に重要

## 次のステップ
次回は、特殊な数値のベストプラクティスについて学習します。