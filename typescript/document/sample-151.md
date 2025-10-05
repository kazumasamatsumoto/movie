# #151 「単項マイナス - -x」

## 概要
TypeScript v5.9の単項マイナスについて学習します。数値の符号を反転する-演算子の基本的な使用方法を理解します。

## 学習目標
- 単項マイナス演算子の基本を理解する
- 数値の符号反転方法を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// 単項マイナス
let positive: number = 5;
let negative: number = -positive; // -5

let negative2: number = -10;
let positive2: number = -negative2; // 10

// 実用的な例
let price: number = 1000;
let discount: number = -price; // -1000

let temperature: number = 25;
let negativeTemp: number = -temperature; // -25
```

## 重要なポイント
1. **符号反転**: 数値の符号を反転
2. **正負変換**: 正の数は負に、負の数は正に
3. **実用性**: 符号の反転や絶対値計算に活用

## 次のステップ
次回は、複合代入演算子について学習します。