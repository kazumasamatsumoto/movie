# #103 「number型への代入」

## 概要
TypeScript v5.9のnumber型への代入について学習します。数値リテラルを代入する方法と型チェック機能を理解します。

## 学習目標
- number型変数への代入方法を理解する
- TypeScriptの型チェック機能を理解する
- 代入可能な値と不可能な値を区別する

## 画面表示用コード

```typescript
// number型への代入
let value: number;

// 数値の代入
value = 100;        // OK
value = 3.14;       // OK
value = -50;        // OK
value = 1e6;        // OK

// 型エラーの例
// value = "100";   // エラー: Type 'string' is not assignable to type 'number'
// value = true;    // エラー: Type 'boolean' is not assignable to type 'number'
```

## 重要なポイント
1. **型チェック**: TypeScriptが代入時に型をチェック
2. **数値リテラル**: 数値のみ使用可能
3. **多様な数値**: 整数、小数、負数、科学的記数法などすべて使用可能

## 次のステップ
次回は、number型の初期化について学習します。