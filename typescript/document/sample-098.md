# #098 「実践パターン(2)」

## 概要
TypeScript v5.9の実践パターン(2)について学習します。高度なstring型の使用パターンを理解します。

## 学習目標
- 高度なパターンを理解する
- バリデーションの実装を理解する
- エラーハンドリングを理解する

## 画面表示用コード

```typescript
// 実践パターン(2)

// 1. バリデーション
function validateEmail(email: string): boolean {
  return email.includes("@") && email.includes(".");
}

// 2. エラーハンドリング
try {
  let userInput: string = "invalid input";
  if (!validateEmail(userInput)) {
    throw new Error("Invalid email format");
  }
} catch (error) {
  let errorMessage: string = `Error: ${error.message}`;
  console.log(errorMessage);
}

// 3. ログ出力
let logMessage: string = `User action: ${new Date().toISOString()}`;
console.log(logMessage);
```

## 重要なポイント
1. **バリデーション**: 入力値の検証
2. **エラーハンドリング**: 例外の適切な処理
3. **ログ出力**: デバッグ情報の記録

## 次のステップ
次回は、総まとめについて学習します。