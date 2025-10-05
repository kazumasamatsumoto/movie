# #056 「charAt()の型」

## 概要
TypeScript v5.9のcharAt()の型について学習します。charAt()が常にstring型を返すことを理解します。

## 学習目標
- charAt()の戻り値の型を理解する
- 範囲外アクセスの動作を理解する
- 型安全性の重要性を理解する

## 画面表示用コード

```typescript
// charAt()の型
let name: string = "Alice";
let result: string = name.charAt(0); // string型

// 型推論でもstring型
let inferred = "Hello".charAt(1); // string型と推論

// 範囲外アクセス
let emptyResult: string = name.charAt(10); // ""（空文字列）

// 実用的な例
let userInput: string = "TypeScript";
let firstChar: string = userInput.charAt(0); // "T"
let lastChar: string = userInput.charAt(userInput.length - 1); // "t"

// 型チェック
console.log(typeof firstChar); // "string"
```

## 重要なポイント
1. **戻り値の型**: 常にstring型
2. **範囲外アクセス**: 空文字列を返す
3. **型安全性**: TypeScriptが型を保証

## 次のステップ
次回は、charAt()範囲外アクセスについて学習します。