# #032 「テンプレートリテラルのインデント」

## 概要
TypeScript v5.9のテンプレートリテラルインデントについて学習します。テンプレートリテラル内のインデントの扱い方を理解します。

## 学習目標
- インデントの保持について理解する
- trim()メソッドの使用方法を理解する
- 適切なインデント管理を理解する

## 画面表示用コード

```typescript
// インデントの例
let userName: string = "Alice";

// インデントが保持される
let message: string = `
    Hello, ${userName}!
    Welcome to our service.
    Have a great day!
`;

// trim()で先頭の改行を削除
let trimmedMessage: string = `
    Hello, ${userName}!
    Welcome to our service.
`.trim();

// 実用的な例
let htmlTemplate: string = `
<div class="container">
    <h1>${userName}</h1>
    <p>Welcome!</p>
</div>
`.trim();
```

## 重要なポイント
1. **インデント保持**: テンプレート内のインデントがそのまま保持
2. **trim()メソッド**: 先頭と末尾の空白を削除
3. **コードの可読性**: 適切なインデント管理が重要

## 次のステップ
次回は、バッククォートのエスケープについて学習します。