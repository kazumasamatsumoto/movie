# #154 「シフト演算子」

## 概要
TypeScript v5.9のシフト演算子について学習します。数値のビットを左右にシフトする演算子の基本的な使用方法を理解します。

## 学習目標
- シフト演算子の基本を理解する
- 各種シフト演算の使用方法を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// シフト演算子
let value: number = 8;  // 1000

let leftShift: number = value << 1;   // 16 (10000)
let rightShift: number = value >> 1;  // 4 (0100)
let unsignedRightShift: number = value >>> 1; // 4

// 実用的な例
let number: number = 4;
let doubled: number = number << 1;    // 8 (2倍)
let halved: number = number >> 1;     // 2 (1/2倍)
```

## 重要なポイント
1. **ビットシフト**: 数値のビットを左右にシフト
2. **高速計算**: 2倍や1/2倍の高速計算
3. **実用性**: 数値の高速計算に活用

## 次のステップ
次回は、数値演算まとめについて学習します。