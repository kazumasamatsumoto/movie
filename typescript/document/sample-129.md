# #129 「Number.isNaN()の違い」

## 概要
TypeScript v5.9のNumber.isNaN()の違いについて学習します。isNaN()とNumber.isNaN()の動作の違いを理解し、適切な使い分けを学びます。

## 学習目標
- Number.isNaN()の基本を理解する
- isNaN()との違いを理解する
- 適切な使い分けを理解する

## 画面表示用コード

```typescript
// Number.isNaN()の違い
let nan: number = NaN;
let stringValue: string = "abc";

// isNaN() - 型変換あり
let isNan1: boolean = isNaN(nan);        // true
let isNan2: boolean = isNaN(stringValue);  // true (型変換される)

// Number.isNaN() - 型変換なし
let isNan3: boolean = Number.isNaN(nan);        // true
let isNan4: boolean = Number.isNaN(stringValue);  // false (型変換されない)

// 実用的な例
let userInput: number = parseInt("abc");
if (Number.isNaN(userInput)) {
  console.log("数値ではありません");
}
```

## 重要なポイント
1. **型変換**: isNaN()は型変換を行う
2. **厳密性**: Number.isNaN()は型変換を行わない
3. **推奨**: Number.isNaN()の使用が推奨される

## 次のステップ
次回は、isFinite()関数について学習します。