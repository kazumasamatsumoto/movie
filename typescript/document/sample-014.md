# #014 「エスケープシーケンス - \"と\'」

## 概要
TypeScript v5.9のエスケープシーケンスについて学習します。特殊文字を文字列内で表現する方法を理解します。

## 学習目標
- エスケープシーケンスの基本概念を理解する
- クォート文字のエスケープ方法を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// エスケープシーケンスの例
let message1: string = "He said \"Hello\" to me";
let message2: string = 'It\'s a beautiful day';
let message3: string = "Path: C:\\Users\\Documents";

// 実用的な例
let jsonString: string = "{\"name\": \"Alice\", \"age\": 30}";
let htmlContent: string = "<div class=\"container\">Content</div>";
let filePath: string = "C:\\Program Files\\MyApp\\config.json";

// 複数のエスケープ
let complexMessage: string = "Line 1\nLine 2\tTabbed content";
```

## 重要なポイント
1. **エスケープ**: バックスラッシュ（\）で特殊文字を表現
2. **クォート**: \"と\'でクォート文字をエスケープ
3. **実用性**: JSON、HTML、ファイルパスなどで活用

## 次のステップ
次回は、バックスラッシュのエスケープについて学習します。