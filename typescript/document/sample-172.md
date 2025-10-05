# #172 「エラーハンドリング」

## 概要
TypeScript v5.9のエラーハンドリングについて学習します。数値変換のエラーを適切に処理する方法を理解します。

## 学習目標
- エラーハンドリングの重要性を理解する
- try-catch文の使用方法を理解する
- 安全な数値変換方法を理解する

## 画面表示用コード

```typescript
// エラーハンドリング
function safeNumberConversion(input: string): number | null {
  try {
    let result: number = Number(input);
    if (Number.isNaN(result)) {
      return null;
    }
    return result;
  } catch (error) {
    console.error("変換エラー:", error);
    return null;
  }
}

// 実用的な例
let userInput: string = "abc";
let userAge: number | null = safeNumberConversion(userInput);

if (userAge === null) {
  console.log("数値変換に失敗しました");
} else {
  console.log(`年齢: ${userAge}`);
}
```

## 重要なポイント
1. **エラーハンドリング**: 変換エラーを適切に処理
2. **try-catch**: エラーをキャッチして処理
3. **安全性**: 安全な数値変換を実現

## 次のステップ
次回は、数値バリデーションについて学習します。
