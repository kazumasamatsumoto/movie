# #206 「constでboolean型」

## 概要
TypeScript v5.9のconstでboolean型について学習します。constキーワードでboolean型の定数を宣言する方法を理解します。

## 学習目標
- constでのboolean型宣言を理解する
- 定数の特徴を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// constでboolean型
const isActive = true;        // boolean型と推論、変更不可
const isCompleted = false;    // boolean型と推論、変更不可
const hasPermission = true;   // boolean型と推論、変更不可

// 実用的な例
const userLoggedIn = true;    // boolean型と推論、変更不可
const formValid = false;      // boolean型と推論、変更不可
const dataLoaded = true;      // boolean型と推論、変更不可

// 変更不可
// isActive = false; // エラー: Cannot assign to 'isActive' because it is a constant
```

## 重要なポイント
1. **定数**: 値の変更ができない
2. **型推論**: 自動的にboolean型と推論
3. **安全性**: 意図しない変更を防ぐ

## 次のステップ
次回は、if文での使用について学習します。
