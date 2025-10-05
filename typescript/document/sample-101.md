# #101 「number型とは - 数値を扱う型」

## 概要
TypeScript v5.9のnumber型について学習します。数値を扱う最も基本的なプリミティブ型として、整数、小数、負数などすべての数値を扱う重要な機能です。

## 学習目標
- number型の基本的な概念を理解する
- 数値データの扱い方の基礎を習得する
- 型安全性の恩恵を理解する

## 画面表示用コード

```typescript
// number型の基本
let age: number = 30;
let price: number = 2980.50;
let count: number = -5;

// 実用的な例
let userAge: number = 25;
let productPrice: number = 1500;
let discountRate: number = 0.1;
let finalPrice: number = productPrice * (1 - discountRate);
```

## 重要なポイント
1. **型安全性**: number型を指定することで、数値以外の値を代入しようとするとエラーになる
2. **数値処理**: 整数、小数、負数などすべての数値を扱える
3. **実用性**: 計算処理やデータ表示に活用

## 次のステップ
次回は、number型の宣言について学習します。