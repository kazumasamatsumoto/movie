# #217 「trueリテラル型の宣言」

## 概要
TypeScript v5.9のtrueリテラル型の宣言について学習します。trueリテラル型の基本的な宣言方法を理解します。

## 学習目標
- trueリテラル型の宣言方法を理解する
- 型注釈の使用方法を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// trueリテラル型の宣言
let isActive: true;        // trueのみ許可
let isEnabled: true;       // trueのみ許可
let hasPermission: true;   // trueのみ許可

// 後で値を代入
isActive = true;           // OK
isEnabled = true;          // OK
hasPermission = true;      // OK

// 実用的な例
let userLoggedIn: true = true;    // 宣言時に初期化
let formValid: true = true;       // 宣言時に初期化
```

## 重要なポイント
1. **型注釈**: : trueで型を指定
2. **値の制限**: true値のみ代入可能
3. **実用性**: 定数の型安全性を保つ

## 次のステップ
次回は、trueリテラル型の使用例について学習します。
