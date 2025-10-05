# #093 「セキュリティ - XSS対策」

## 概要
TypeScript v5.9のセキュリティXSS対策について学習します。クロスサイトスクリプティング攻撃を防ぐ対策を理解します。

## 学習目標
- XSS攻撃の基本を理解する
- 入力値の検証方法を理解する
- 出力時のエスケープを理解する

## 画面表示用コード

```typescript
// セキュリティ - XSS対策

// 入力値の検証
function sanitizeInput(input: string): string {
  return input.replace(/<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi, '');
}

// 安全な文字列処理
let userInput: string = "<script>alert('XSS')</script>";
let safeInput: string = sanitizeInput(userInput);

// 実用的な例
let userName: string = "Alice";
let userMessage: string = "Hello, World!";
let displayText: string = `${userName}: ${userMessage}`;
```

## 重要なポイント
1. **入力検証**: 悪意のあるスクリプトを除去
2. **サニタイズ**: 安全な文字列に変換
3. **セキュリティ**: アプリケーションの安全性確保

## 次のステップ
次回は、ベストプラクティス(1)について学習します。