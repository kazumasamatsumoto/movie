# #200 「マスターチェック」

## 概要
TypeScript v5.9の数値のマスターチェックについて学習します。数値処理の理解度を確認するチェック項目を理解します。

## 学習目標
- 数値のマスターチェック項目を理解する
- 理解度の確認方法を理解する
- 実用的な応用を理解する

## 画面表示用コード

```typescript
// 数値のマスターチェック

// 1. 型の違い
let num: number = 30; // プリミティブ型
// let numObj: Number = new Number(30); // オブジェクト型（非推奨）

// 2. 精度問題
let sum: number = 0.1 + 0.2;
console.log(sum === 0.3); // false

// 3. 適切な比較
function isEqual(a: number, b: number): boolean {
  return Math.abs(a - b) < 1e-10;
}

// 4. バリデーション
function validateNumber(value: unknown): value is number {
  return typeof value === "number" && Number.isFinite(value);
}

// 5. 実用的な例
let userAge: number = 25;
let productPrice: number = 1500;
let total: number = userAge + productPrice;
```

## 重要なポイント
1. **型の違い**: number型とNumber型の使い分け
2. **精度問題**: IEEE 754の制限と回避方法
3. **適切な比較**: イプシロン比較の使用
4. **バリデーション**: 数値の有効性チェック
5. **実用性**: 実際の開発での活用

## 次のステップ
次回は、boolean型について学習します。
