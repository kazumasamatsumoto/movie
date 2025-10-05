# #201 「boolean型とは」

## 概要
TypeScript v5.9のboolean型について学習します。真偽値を表す型の基本的な概念と使用方法を理解します。

## 学習目標
- boolean型の基本を理解する
- 真偽値の概念を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// boolean型とは
let isActive: boolean = true;
let isCompleted: boolean = false;
let hasPermission: boolean = true;

// 実用的な例
let userLoggedIn: boolean = true;
let formValid: boolean = false;
let dataLoaded: boolean = true;

// 条件分岐での使用
if (isActive) {
  console.log("アクティブです");
}
```

## 重要なポイント
1. **真偽値**: trueかfalseの2つの値のみ
2. **条件分岐**: if文やwhile文で使用
3. **状態管理**: アプリケーションの状態を管理

## 次のステップ
次回は、boolean型の宣言について学習します。
