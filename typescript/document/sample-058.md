# #058 「charCodeAt(index)」

## 概要
TypeScript v5.9のcharCodeAt()について学習します。指定したインデックスの文字のUnicodeコードポイントを取得するメソッドを理解します。

## 学習目標
- charCodeAt()の基本使用方法を理解する
- Unicodeコードポイントの概念を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// charCodeAt()の使用例
let name: string = "Alice";
let message: string = "Hello";

// Unicodeコードポイントの取得
let codeA: number = name.charCodeAt(0); // 65 (Aのコードポイント)
let codeL: number = name.charCodeAt(1); // 108 (lのコードポイント)
let codeH: number = message.charCodeAt(0); // 72 (Hのコードポイント)

// 実用的な例
let userInput: string = "ABC";
let codeA: number = userInput.charCodeAt(0); // 65
let codeB: number = userInput.charCodeAt(1); // 66
let codeC: number = userInput.charCodeAt(2); // 67

// 範囲外アクセス
let invalidCode: number = name.charCodeAt(10); // NaN
```

## 重要なポイント
1. **Unicodeコードポイント**: 文字の数値表現
2. **戻り値**: number型
3. **範囲外アクセス**: NaNを返す

## 次のステップ
次回は、indexOf()について学習します。