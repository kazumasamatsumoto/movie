# #150 「単項プラス - +x」

## 概要
TypeScript v5.9の単項プラスについて学習します。数値を正の値に変換する+演算子の基本的な使用方法を理解します。

## 学習目標
- 単項プラス演算子の基本を理解する
- 数値の正規化方法を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// 単項プラス
let negative: number = -5;
let positive: number = +negative; // -5 (符号は変わらない)

// 型変換での使用
let stringNumber: string = "123";
let number: number = +stringNumber; // 123

// 実用的な例
let userInput: string = "42";
let numericValue: number = +userInput; // 42

let absoluteValue: number = +Math.abs(-10); // 10
```

## 重要なポイント
1. **正規化**: 数値を正の値に変換
2. **型変換**: 文字列を数値に変換
3. **実用性**: 数値の正規化や型変換に活用

## 次のステップ
次回は、単項マイナスについて学習します。

