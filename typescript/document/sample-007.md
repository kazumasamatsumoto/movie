# #007 「string型とリテラル型の違い - "hello" vs string」

## 概要
TypeScript v5.9のstring型とリテラル型の重要な違いについて学習します。より厳密な型チェックを提供するリテラル型の概念を理解します。

## 学習目標
- string型とリテラル型の違いを理解する
- リテラル型の使用場面を理解する
- 型の厳密性の違いを理解する

## 画面表示用コード

```typescript
// string型: 任意の文字列
let message: string = "hello";
message = "world"; // OK

// リテラル型: 特定の値のみ
let status: "loading" | "success" | "error" = "loading";
status = "success"; // OK
// status = "pending"; // エラー

// 実用的な例
function setTheme(theme: "light" | "dark") {
  console.log(`Theme: ${theme}`);
}
```

## 重要なポイント
1. **string型**: 任意の文字列を代入可能（柔軟性）
2. **リテラル型**: 特定の値のみ許可（厳密性）
3. **使い分け**: 用途に応じて適切な型を選択

## 次のステップ
次回は、varを使わない理由について学習します。