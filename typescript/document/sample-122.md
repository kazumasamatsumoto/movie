# #122 「Infinityの型」

## 概要
TypeScript v5.9のInfinityの型について学習します。Infinityもnumber型として扱われることを理解し、型の一貫性を学びます。

## 学習目標
- Infinityの型を理解する
- typeof演算子での確認方法を理解する
- 型の一貫性を理解する

## 画面表示用コード

```typescript
// Infinityの型
let infinity: number = Infinity;
let normalNumber: number = 100;

// 型は同じ
console.log(typeof infinity);    // "number"
console.log(typeof normalNumber); // "number"

// 実用的な例
let maxValue: number = Infinity;
let userAge: number = 25;

// 型チェック
console.log(typeof maxValue); // "number"
console.log(typeof userAge);  // "number"
```

## 重要なポイント
1. **型の統一**: Infinityもnumber型として扱われる
2. **typeof確認**: typeof演算子で"number"と表示
3. **一貫性**: すべての数値が同じ型として扱われる

## 次のステップ
次回は、Infinityの生成について学習します。