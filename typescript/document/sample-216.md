# #216 「trueリテラル型」

## 概要
TypeScript v5.9のtrueリテラル型について学習します。true値のみを許可する厳密な型の基本的な使用方法を理解します。

## 学習目標
- trueリテラル型の基本を理解する
- boolean型との違いを理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// trueリテラル型
let isActive: true = true;        // trueのみ許可
let isEnabled: true = true;       // trueのみ許可
let hasPermission: true = true;   // trueのみ許可

// 実用的な例
let userLoggedIn: true = true;    // trueのみ許可
let formValid: true = true;       // trueのみ許可
let dataLoaded: true = true;      // trueのみ許可

// 型の制限
// isActive = false; // エラー: Type 'false' is not assignable to type 'true'
```

## 重要なポイント
1. **厳密な型**: true値のみを許可
2. **型安全性**: より厳密な型制御
3. **実用性**: 定数フラグの管理に活用

## 次のステップ
次回は、trueリテラル型の宣言について学習します。
