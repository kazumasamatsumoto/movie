# #012 「シングルクォート文字列 - 'hello'」

## 概要
TypeScript v5.9のシングルクォート文字列について学習します。シングルクォートで囲まれた文字列リテラルの使用方法を理解します。

## 学習目標
- シングルクォート文字列の基本を理解する
- ダブルクォートとの違いを理解する
- 一貫性のあるコードスタイルの重要性を理解する

## 画面表示用コード

```typescript
// シングルクォート文字列
let message: string = 'Hello, World!';
let name: string = 'Alice';
let description: string = 'TypeScript学習中';

// 実用的な例
let apiUrl: string = 'https://api.example.com';
let errorMessage: string = 'エラーが発生しました';
let successMessage: string = '処理が完了しました';

// 文字列の結合
let greeting: string = 'こんにちは、' + name + 'さん！';
let fullMessage: string = message + ' ' + description;
```

## 重要なポイント
1. **シングルクォート**: 'で囲まれた文字列リテラル
2. **機能的な違い**: ダブルクォートと機能的には同じ
3. **一貫性**: プロジェクト内で統一することが重要

## 次のステップ
次回は、ダブルとシングルの使い分けについて学習します。