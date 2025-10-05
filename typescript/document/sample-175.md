# #175 「数値変換まとめ」

## 概要
TypeScript v5.9の数値変換まとめについて学習します。数値変換の要点と重要な機能のまとめを理解します。

## 学習目標
- 数値変換の要点を整理する
- 主要な変換関数の使い分けを理解する
- 実用的な応用を理解する

## 画面表示用コード

```typescript
// 数値変換まとめ

// 1. 基本変換関数
let str: string = "123.45";
let num1: number = Number(str);      // 123.45
let num2: number = parseInt(str);    // 123
let num3: number = parseFloat(str);  // 123.45

// 2. バリデーション
let isValid: boolean = Number.isFinite(num1);
let isInteger: boolean = Number.isInteger(num2);

// 3. エラーハンドリング
let userInput: string = "abc";
let converted: number = Number(userInput);
if (Number.isNaN(converted)) {
  console.log("変換に失敗しました");
}
```

## 重要なポイント
1. **基本変換**: Number()、parseInt()、parseFloat()
2. **バリデーション**: Number.isFinite()、Number.isInteger()
3. **エラーハンドリング**: NaNチェックと適切な処理

## 次のステップ
次回は、IEEE 754について学習します。
