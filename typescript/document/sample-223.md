# #223 「型推論 - const使用時」

## 概要
TypeScript v5.9の型推論（const使用時）について学習します。constで宣言した時に自動的にリテラル型と推論される機能を理解します。

## 学習目標
- const使用時の型推論を理解する
- リテラル型の自動推論を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// 型推論 - const使用時

// constでの型推論
const isActive = true;        // trueリテラル型と推論
const isDisabled = false;     // falseリテラル型と推論
const hasPermission = true;   // trueリテラル型と推論

// 実用的な例
const userLoggedIn = true;    // trueリテラル型と推論
const formValid = false;      // falseリテラル型と推論
const dataLoaded = true;      // trueリテラル型と推論

// 型の確認
// isActive = false; // エラー: Cannot assign to 'isActive' because it is a constant
```

## 重要なポイント
1. **自動推論**: constで宣言時に自動的にリテラル型と推論
2. **型安全性**: 推論後も型チェックが有効
3. **実用性**: 定数の型安全性を自動的に保つ

## 次のステップ
次回は、ユースケースについて学習します。
