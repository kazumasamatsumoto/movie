# #057 「charAt()範囲外アクセス」

## 概要
TypeScript v5.9のcharAt()範囲外アクセスについて学習します。文字列の長さを超えるインデックスにアクセスした場合の動作を理解します。

## 学習目標
- 範囲外アクセスの動作を理解する
- 安全な文字列処理を理解する
- エラーハンドリングを理解する

## 画面表示用コード

```typescript
// charAt()範囲外アクセス
let name: string = "Alice"; // 長さ5

// 範囲内アクセス
let validChar: string = name.charAt(0); // "A"
let validChar2: string = name.charAt(4); // "e"

// 範囲外アクセス
let invalidChar: string = name.charAt(5); // ""（空文字列）
let invalidChar2: string = name.charAt(-1); // ""（空文字列）
let invalidChar3: string = name.charAt(10); // ""（空文字列）

// 実用的な例
let userInput: string = "Hello";
let safeChar: string = userInput.charAt(userInput.length); // ""（安全）
```

## 重要なポイント
1. **範囲外アクセス**: エラーではなく空文字列を返す
2. **安全性**: 例外が発生しない
3. **実用性**: 安全な文字列処理が可能

## 次のステップ
次回は、charCodeAt()について学習します。