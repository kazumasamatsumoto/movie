# #040 「テンプレートリテラルまとめ」

## 概要
TypeScript v5.9のテンプレートリテラルまとめについて学習します。テンプレートリテラルの要点と重要な機能を総括します。

## 学習目標
- テンプレートリテラルの要点を理解する
- 主要な機能を整理する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// テンプレートリテラルの要点まとめ
let name: string = "Alice";
let age: number = 30;

// 1. 基本的な変数埋め込み
let greeting: string = `Hello, ${name}!`;

// 2. 複数変数の埋め込み
let info: string = `${name} is ${age} years old`;

// 3. 式の埋め込み
let calculation: string = `Next year: ${age + 1}`;

// 4. 複数行文字列
let multiLine: string = `
Hello, ${name}!
Age: ${age}
Welcome!
`;

// 5. 実用的な例
let user = { name: "Bob", role: "admin" };
let userInfo: string = `User: ${user.name} (${user.role})`;
```

## 重要なポイント
1. **バッククォート**: `で囲まれた文字列リテラル
2. **変数埋め込み**: ${}で変数を文字列に埋め込み
3. **複数行**: 改行を含む文字列を簡単に記述
4. **型安全性**: 常にstring型として扱われる

## 次のステップ
次回は、文字列メソッドについて学習します。