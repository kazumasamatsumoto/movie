# #030 「複数行のテンプレートリテラル」

## 概要
TypeScript v5.9の複数行テンプレートリテラルについて学習します。改行を含む複数行の文字列を簡単に記述できる機能を理解します。

## 学習目標
- 複数行テンプレートリテラルの基本を理解する
- 改行の扱い方を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// 複数行テンプレートリテラル
let userName: string = "Alice";
let userEmail: string = "alice@example.com";

// 複数行の文字列
let multiLineMessage: string = `
Hello, ${userName}!

Thank you for registering.
Your email: ${userEmail}

Best regards,
Support Team
`;

// 実用的な例
let htmlTemplate: string = `
<div class="user-card">
  <h2>${userName}</h2>
  <p>Email: ${userEmail}</p>
  <button>Edit Profile</button>
</div>
`;
```

## 重要なポイント
1. **改行の保持**: テンプレート内の改行がそのまま保持
2. **インデント**: インデントも保持される
3. **可読性**: 複数行の文字列が読みやすく記述可能

## 次のステップ
次回は、複数行文字列の実例について学習します。