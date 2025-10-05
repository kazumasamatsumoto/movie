# #205 「型推論でboolean型」

## 概要
TypeScript v5.9の型推論でboolean型について学習します。型注釈を省略してTypeScriptが自動的にboolean型と推論する機能を理解します。

## 学習目標
- 型推論の仕組みを理解する
- boolean型の型推論を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// 型推論でboolean型
let isActive = true;        // boolean型と推論
let isCompleted = false;    // boolean型と推論
let hasPermission = true;   // boolean型と推論

// 実用的な例
let userLoggedIn = true;    // boolean型と推論
let formValid = false;      // boolean型と推論
let dataLoaded = true;      // boolean型と推論

// 型注釈なしでも型安全
// isActive = "true"; // エラー: Type 'string' is not assignable to type 'boolean'
```

## 重要なポイント
1. **型推論**: TypeScriptが自動的に型を推論
2. **簡潔性**: 型注釈を省略可能
3. **型安全性**: 推論後も型チェックが有効

## 次のステップ
次回は、constでboolean型について学習します。
