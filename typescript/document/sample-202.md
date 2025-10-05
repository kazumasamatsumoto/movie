# #202 「boolean型の宣言」

## 概要
TypeScript v5.9のboolean型宣言について学習します。boolean型の基本的な宣言方法と使用方法を理解します。

## 学習目標
- boolean型の宣言方法を理解する
- 型注釈の使用方法を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// boolean型の宣言
let isActive: boolean;
let isCompleted: boolean;
let hasPermission: boolean;

// 後で値を代入
isActive = true;
isCompleted = false;
hasPermission = true;

// 実用的な例
let userLoggedIn: boolean = true;
let formValid: boolean = false;
let dataLoaded: boolean = true;
```

## 重要なポイント
1. **型注釈**: : booleanで型を指定
2. **初期化**: 宣言時に値を代入可能
3. **実用性**: 様々な状態管理に活用

## 次のステップ
次回は、trueの代入について学習します。
