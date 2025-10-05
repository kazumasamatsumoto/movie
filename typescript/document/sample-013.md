# #013 「ダブルとシングルの使い分け」

## 概要
TypeScript v5.9のダブルクォートとシングルクォートの使い分けについて学習します。一貫性のあるコードスタイルの重要性を理解します。

## 学習目標
- ダブルクォートとシングルクォートの使い分けを理解する
- 一貫性のあるコードスタイルの重要性を理解する
- 実用的な使い分け例を理解する

## 画面表示用コード

```typescript
// プロジェクト内での統一例
// シングルクォート統一スタイル
let message: string = 'Hello, World!';
let name: string = 'Alice';

// HTML属性内ではダブルクォート
let htmlTemplate: string = '<div class="container">Hello</div>';

// 実用的な例
let componentTemplate: string = '<h1>{{title}}</h1>';
let cssClass: string = 'btn btn-primary';
let apiEndpoint: string = '/api/users';

// 一貫性の重要性
let userMessage: string = 'ユーザー登録完了';
let systemMessage: string = 'システムエラー';
```

## 重要なポイント
1. **統一性**: プロジェクト内で一貫したスタイルを使用
2. **HTML属性**: HTML属性内ではダブルクォートを使用
3. **可読性**: 一貫性によりコードの可読性が向上

## 次のステップ
次回は、エスケープシーケンスについて学習します。