# #037 「よくある間違い(1)」

## 概要
TypeScript v5.9のテンプレートリテラルよくある間違いについて学習します。テンプレートリテラルでよく発生するエラーや問題を理解します。

## 学習目標
- よくある間違いの種類を理解する
- エラーの原因を理解する
- 正しい記述方法を理解する

## 画面表示用コード

```typescript
// よくある間違いの例

// 1. クォートの混在（間違い）
// let message = "Hello, ${name}!"; // ダブルクォートでは埋め込みされない

// 正しい方法
let name: string = "Alice";
let message: string = `Hello, ${name}!`; // バッククォートを使用

// 2. 未定義変数（間違い）
// let errorMessage = `Hello, ${undefinedVariable}!`; // エラー

// 正しい方法
let userName: string = "Bob";
let correctMessage: string = `Hello, ${userName}!`;

// 3. 型の不一致
let age: number = 30;
let ageMessage: string = `Age: ${age}`; // 数値も文字列に変換される
```

## 重要なポイント
1. **クォートの混在**: ダブルクォートでは埋め込みされない
2. **未定義変数**: 存在しない変数はエラー
3. **型の自動変換**: 数値や真偽値は文字列に変換

## 次のステップ
次回は、よくある間違い(2)について学習します。