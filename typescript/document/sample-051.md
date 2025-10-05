# #051 「toUpperCase() - 大文字化」

## 概要
TypeScript v5.9のtoUpperCase()について学習します。文字列を大文字に変換するメソッドの使用方法を理解します。

## 学習目標
- toUpperCase()の基本使用方法を理解する
- 大文字化の動作を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// toUpperCase()の使用例
let name: string = "alice";
let email: string = "alice@example.com";
let message: string = "hello, world!";

// 大文字化
let upperName: string = name.toUpperCase(); // "ALICE"
let upperEmail: string = email.toUpperCase(); // "ALICE@EXAMPLE.COM"
let upperMessage: string = message.toUpperCase(); // "HELLO, WORLD!"

// 実用的な例
let userName: string = "bob";
let userRole: string = "admin";
let displayName: string = userName.toUpperCase();
let roleDisplay: string = userRole.toUpperCase();
```

## 重要なポイント
1. **大文字化**: すべての文字を大文字に変換
2. **戻り値**: 新しい文字列を返す
3. **実用性**: データの正規化に活用

## 次のステップ
次回は、toUpperCase()の型について学習します。