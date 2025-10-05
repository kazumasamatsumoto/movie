# #016 「改行のエスケープ - \n」

## 概要
TypeScript v5.9の改行エスケープについて学習します。改行文字を表現する方法と複数行テキストの処理を理解します。

## 学習目標
- 改行エスケープの基本を理解する
- 複数行テキストの記述方法を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// 改行のエスケープ
let multiLineMessage: string = "Line 1\nLine 2\nLine 3";
let errorMessage: string = "エラーが発生しました\n詳細: ファイルが見つかりません";
let logMessage: string = "INFO: 処理開始\nDEBUG: データ読み込み中\nINFO: 処理完了";

// 実用的な例
let userInstructions: string = "手順:\n1. ファイルを選択\n2. アップロードボタンをクリック\n3. 完了を確認";
let systemMessage: string = "システムメンテナンス中\n復旧予定: 2024年1月1日 10:00";

// コンソール出力での確認
console.log(multiLineMessage);
```

## 重要なポイント
1. **改行文字**: \nで改行を表現
2. **複数行テキスト**: 一つの文字列で複数行を記述
3. **実用性**: エラーメッセージや表示テキストに活用

## 次のステップ
次回は、タブのエスケープについて学習します。