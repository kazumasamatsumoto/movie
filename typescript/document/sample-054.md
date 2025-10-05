# #054 「toLowerCase()の実例」

## 概要
TypeScript v5.9のtoLowerCase()実例について学習します。実際の開発でよく使われる使用例を理解します。

## 学習目標
- toLowerCase()の実用的な使用例を理解する
- データの正規化方法を理解する
- 比較処理での活用方法を理解する

## 画面表示用コード

```typescript
// toLowerCase()の実例

// 1. データの正規化
let userInput: string = "  ALICE  ";
let normalizedInput: string = userInput.trim().toLowerCase(); // "alice"

// 2. 比較処理
let storedName: string = "alice";
let inputName: string = "ALICE";
let isMatch: boolean = storedName === inputName.toLowerCase(); // true

// 3. 検索処理
let searchTerm: string = "TYPESCRIPT";
let content: string = "Learn TypeScript programming";
let isFound: boolean = content.toLowerCase().includes(searchTerm.toLowerCase());

// 実用的な例
let email: string = "USER@EXAMPLE.COM";
let normalizedEmail: string = email.toLowerCase(); // "user@example.com"
```

## 重要なポイント
1. **データ正規化**: 入力データの統一
2. **比較処理**: 大文字小文字を無視した比較
3. **検索処理**: 大文字小文字を無視した検索

## 次のステップ
次回は、charAt()について学習します。