# #008 「string型の変数宣言 - varは使わない理由」

## 概要
TypeScript v5.9のstring型変数宣言について学習します。var、let、constの違いとモダンな宣言方法を理解します。

## 学習目標
- var、let、constの基本的な違いを理解する
- スコープの概念を理解する
- モダンな宣言方法の重要性を理解する

## 画面表示用コード

```typescript
// var（非推奨）
// var oldStyle: string = "古いスタイル";

// let（推奨）- 再代入可能
let modernStyle: string = "モダンスタイル";
modernStyle = "更新された値"; // OK

// const（推奨）- 再代入不可
const constantValue: string = "定数値";
// constantValue = "新しい値"; // エラー

// 実用的な例
let userName: string = "初期値";
const API_ENDPOINT: string = "https://api.example.com";
```

## 重要なポイント
1. **var**: 関数スコープ、巻き上げが発生（非推奨）
2. **let**: ブロックスコープ、再代入可能（推奨）
3. **const**: ブロックスコープ、再代入不可（推奨）

## 次のステップ
次回は、string型とundefinedについて学習します。

