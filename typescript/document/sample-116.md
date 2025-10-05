# #116 「科学的記数法 - 1e6」

## 概要
TypeScript v5.9の科学的記数法について学習します。大きな数や小さな数を効率的に記述する方法を理解します。

## 学習目標
- 科学的記数法の基本を理解する
- e記法の使用方法を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// 科学的記数法
let large: number = 1e6;      // 1,000,000
let small: number = 1e-6;     // 0.000001
let veryLarge: number = 1e9;  // 1,000,000,000

// 実用的な例
let million: number = 1e6;    // 100万
let billion: number = 1e9;    // 10億
let microsecond: number = 1e-6; // マイクロ秒
let nanosecond: number = 1e-9;  // ナノ秒
```

## 重要なポイント
1. **e記法**: 数値とe、指数を書く
2. **大きな数**: 1e6 = 1,000,000
3. **小さな数**: 1e-6 = 0.000001

## 次のステップ
次回は、アンダースコア区切りについて学習します。