# #169 「暗黙的な型変換」

## 概要
TypeScript v5.9の暗黙的な型変換について学習します。自動的に型が変換される機能の仕組みを理解します。

## 学習目標
- 暗黙的な型変換の仕組みを理解する
- 演算での型変換を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// 暗黙的な型変換
let num: number = 10;
let str: string = "5";

// 演算での暗黙的変換
let result1: string = num + str;  // "105" (文字列結合)
let result2: number = num - str;  // 5 (数値演算)

// 実用的な例
let userAge: number = 25;
let ageStr: string = "歳";
let displayText: string = userAge + ageStr; // "25歳"

let price: number = 1000;
let discount: string = "100";
let finalPrice: number = price - discount; // 900
```

## 重要なポイント
1. **自動変換**: 演算時に自動的に型が変換
2. **演算子依存**: 演算子によって変換結果が異なる
3. **注意**: 予期しない結果になる場合がある

## 次のステップ
次回は、明示的な型変換について学習します。
