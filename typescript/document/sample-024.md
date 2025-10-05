# #024 「式の埋め込み - ${1 + 2}」

## 概要
TypeScript v5.9の式埋め込みについて学習します。${}内で計算式や演算を実行して結果を埋め込む機能を理解します。

## 学習目標
- 式埋め込みの基本概念を理解する
- 算術演算の埋め込みを理解する
- 比較演算の埋め込みを理解する

## 画面表示用コード

```typescript
// 式埋め込みの例
let a: number = 10;
let b: number = 5;

// 算術演算
let sum: string = `Sum: ${a + b}`;
let product: string = `Product: ${a * b}`;
let average: string = `Average: ${(a + b) / 2}`;

// 比較演算
let comparison: string = `a > b: ${a > b}`;
let equality: string = `a === b: ${a === b}`;

// 実用的な例
let price: number = 1000;
let tax: number = 0.1;
let total: string = `Total: ¥${price * (1 + tax)}`;
```

## 重要なポイント
1. **式の実行**: ${}内で式を評価して結果を埋め込み
2. **算術演算**: 四則演算や複雑な計算が可能
3. **比較演算**: 真偽値の結果も文字列に変換

## 次のステップ
次回は、関数呼び出しの埋め込みについて学習します。