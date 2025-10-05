# #207 「if文での使用」

## 概要
TypeScript v5.9のif文でのboolean型使用について学習します。if文の条件式でboolean型の変数を使用する方法を理解します。

## 学習目標
- if文でのboolean型使用を理解する
- 条件分岐の制御を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// if文での使用
let isActive: boolean = true;
let isCompleted: boolean = false;

// 基本的な使用
if (isActive) {
  console.log("アクティブです");
}

if (!isCompleted) {
  console.log("未完了です");
}

// 実用的な例
let userLoggedIn: boolean = true;
if (userLoggedIn) {
  console.log("ユーザーがログインしています");
}
```

## 重要なポイント
1. **条件分岐**: if文の条件式で使用
2. **否定**: !演算子で否定
3. **実用性**: アプリケーションの制御に活用

## 次のステップ
次回は、while文での使用について学習します。
