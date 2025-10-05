# #130 「isFinite()関数」

## 概要
TypeScript v5.9のisFinite()関数について学習します。値が有限数かどうかを判定する関数の使用方法を理解します。

## 学習目標
- isFinite()関数の基本を理解する
- 有限数判定の方法を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// isFinite()関数
let normalNumber: number = 100;
let infinity: number = Infinity;
let nan: number = NaN;

// 有限数判定
let isFinite1: boolean = isFinite(normalNumber); // true
let isFinite2: boolean = isFinite(infinity);     // false
let isFinite3: boolean = isFinite(nan);          // false

// 実用的な例
let userInput: number = parseFloat("123.45");
if (isFinite(userInput)) {
  console.log("有効な数値です");
} else {
  console.log("無効な数値です");
}
```

## 重要なポイント
1. **有限数判定**: 値が有限数かどうかを判定
2. **無限大除外**: Infinityと-Infinityはfalse
3. **NaN除外**: NaNもfalseになる

## 次のステップ
次回は、Number.isFinite()について学習します。