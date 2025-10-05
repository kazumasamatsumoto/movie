# #113 「2進数の型」

## 概要
TypeScript v5.9の2進数の型について学習します。2進数リテラルもnumber型として扱われることを理解します。

## 学習目標
- 2進数リテラルの型を理解する
- number型との関係を理解する
- 型の一貫性を理解する

## 画面表示用コード

```typescript
// 2進数の型
let binary: number = 0b1010;  // number型
let decimal: number = 10;     // number型

// 型は同じ
console.log(typeof binary);   // "number"
console.log(typeof decimal);  // "number"

// 値も同じ
console.log(binary === decimal); // true

// 実用的な例
let flag: number = 0b0001;
let value: number = 1;
console.log(flag === value); // true
```

## 重要なポイント
1. **型の統一**: 2進数リテラルもnumber型
2. **値の等価性**: 同じ数値は等価
3. **型の一貫性**: すべての数値リテラルはnumber型

## 次のステップ
次回は、8進数リテラルについて学習します。