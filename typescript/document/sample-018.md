# #018 「Unicode文字 - \u0041」

## 概要
TypeScript v5.9のUnicode文字について学習します。Unicodeエスケープシーケンスを使用した特殊文字の表現方法を理解します。

## 学習目標
- Unicodeエスケープシーケンスの基本を理解する
- 特殊文字や絵文字の表現方法を理解する
- 多言語対応での活用方法を理解する

## 画面表示用コード

```typescript
// Unicode文字の例
let unicodeA: string = "\u0041"; // A
let unicodeHeart: string = "\u2764"; // ❤
let unicodeStar: string = "\u2605"; // ★
let unicodeCheck: string = "\u2713"; // ✓

// 実用的な例
let successIcon: string = "\u2713 成功";
let errorIcon: string = "\u2717 エラー";
let warningIcon: string = "\u26A0 警告";
let infoIcon: string = "\u2139 情報";

// 多言語文字
let japanese: string = "\u65E5\u672C\u8A9E"; // 日本語
let chinese: string = "\u4E2D\u6587"; // 中文
```

## 重要なポイント
1. **Unicodeエスケープ**: \uXXXX形式でUnicode文字を表現
2. **特殊文字**: 絵文字や記号の表現
3. **多言語対応**: 国際化対応での活用

## 次のステップ
次回は、空文字列について学習します。