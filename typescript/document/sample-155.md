# #155 「数値演算まとめ」

## 概要
TypeScript v5.9の数値演算まとめについて学習します。数値演算子の要点を整理し、数値計算の理解を深めます。

## 学習目標
- 数値演算子の要点を整理する
- 主要な演算子の使い分けを理解する
- 実用的な応用を理解する

## 画面表示用コード

```typescript
// 数値演算まとめ

// 1. 四則演算
let a: number = 10;
let b: number = 3;
let sum: number = a + b;      // 13
let diff: number = a - b;     // 7
let prod: number = a * b;     // 30
let quot: number = a / b;     // 3.33...
let rem: number = a % b;      // 1

// 2. べき乗
let power: number = a ** 2;   // 100

// 3. インクリメント/デクリメント
let count: number = 5;
count++; // 6
count--; // 5

// 4. 複合代入
let value: number = 10;
value += 5; // 15
```

## 重要なポイント
1. **四則演算**: +、-、*、/、%の基本演算
2. **べき乗**: **演算子でのべき乗計算
3. **インクリメント/デクリメント**: ++、--演算子
4. **複合代入**: +=、-=、*=、/=、%=演算子

## 次のステップ
次回は、boolean型について学習します。
