# #053 「toLowerCase() - 小文字化」

## 概要
TypeScript v5.9のtoLowerCase()について学習します。文字列を小文字に変換するメソッドの使用方法を理解します。

## 学習目標
- toLowerCase()の基本使用方法を理解する
- 小文字化の動作を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// toLowerCase()の使用例
let name: string = "ALICE";
let email: string = "ALICE@EXAMPLE.COM";
let message: string = "HELLO, WORLD!";

// 小文字化
let lowerName: string = name.toLowerCase(); // "alice"
let lowerEmail: string = email.toLowerCase(); // "alice@example.com"
let lowerMessage: string = message.toLowerCase(); // "hello, world!"

// 実用的な例
let userName: string = "BOB";
let userRole: string = "ADMIN";
let normalizedName: string = userName.toLowerCase();
let normalizedRole: string = userRole.toLowerCase();
```

## 重要なポイント
1. **小文字化**: すべての文字を小文字に変換
2. **戻り値**: 新しい文字列を返す
3. **実用性**: データの正規化に活用

## 次のステップ
次回は、toLowerCase()の実例について学習します。