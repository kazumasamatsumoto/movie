# #173 「数値バリデーション」

## 概要
TypeScript v5.9の数値バリデーションについて学習します。数値が有効かどうかを検証する方法を理解します。

## 学習目標
- 数値バリデーションの重要性を理解する
- バリデーション関数の作成方法を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// 数値バリデーション
function validateNumber(value: number): boolean {
  return Number.isFinite(value) && !Number.isNaN(value);
}

function validateInteger(value: number): boolean {
  return Number.isInteger(value) && Number.isFinite(value);
}

// 実用的な例
let userAge: number = 25;
let productPrice: number = 1500;

if (validateNumber(userAge)) {
  console.log("有効な年齢です");
}

if (validateInteger(productPrice)) {
  console.log("有効な整数価格です");
}
```

## 重要なポイント
1. **バリデーション**: 数値の有効性を検証
2. **Number.isFinite**: 有限数かどうかをチェック
3. **Number.isInteger**: 整数かどうかをチェック

## 次のステップ
次回は、型安全な変換について学習します。
