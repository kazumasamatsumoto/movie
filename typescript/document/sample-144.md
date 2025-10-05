# #144 「剰余演算子」

## 概要
TypeScript v5.9の剰余演算子について学習します。数値の余りを求める%演算子の基本的な使用方法を理解します。

## 学習目標
- 剰余演算子の基本を理解する
- 数値の余り計算方法を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// 剰余演算子
let a: number = 17;
let b: number = 5;
let remainder: number = a % b; // 2

// 実用的な例
let number: number = 42;
let isEven: boolean = number % 2 === 0; // true

let seconds: number = 125;
let minutes: number = Math.floor(seconds / 60);
let remainingSeconds: number = seconds % 60; // 5
```

## 重要なポイント
1. **余り計算**: 2つの数値の余りを計算
2. **結果**: 数値同士の剰余演算は数値になる
3. **実用性**: 偶数奇数判定や周期計算に活用

## 次のステップ
次回は、剰余の型推論について学習します。

