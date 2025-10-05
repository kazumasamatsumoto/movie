# #126 「NaNの型」

## 概要
TypeScript v5.9のNaNの型について学習します。NaNもnumber型として扱われることを理解し、型の一貫性を学びます。

## 学習目標
- NaNの型を理解する
- typeof演算子での確認方法を理解する
- 型の一貫性を理解する

## 画面表示用コード

```typescript
// NaNの型
let nan: number = NaN;
let normalNumber: number = 100;

// 型は同じ
console.log(typeof nan);        // "number"
console.log(typeof normalNumber); // "number"

// 実用的な例
let invalidResult: number = NaN;
let validResult: number = 42;

// 型チェック
console.log(typeof invalidResult); // "number"
console.log(typeof validResult);   // "number"
```

## 重要なポイント
1. **型の統一**: NaNもnumber型として扱われる
2. **typeof確認**: typeof演算子で"number"と表示
3. **一貫性**: すべての数値が同じ型として扱われる

## 次のステップ
次回は、NaNの生成について学習します。