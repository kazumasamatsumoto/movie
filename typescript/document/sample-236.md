# #236 「二重否定 - !!」

## 概要
TypeScript v5.9の二重否定について学習します。!!演算子で値をboolean型に変換する方法を理解します。

## 学習目標
- 二重否定の基本を理解する
- !!演算子の使用方法を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// 二重否定 - !!
let userName: string = "John";
let userAge: number = 25;
let userData: object = {};
let nullValue: null = null;

// 二重否定の使用
let hasName: boolean = !!userName;        // true
let hasAge: boolean = !!userAge;          // true
let hasData: boolean = !!userData;        // true
let hasValue: boolean = !!nullValue;      // false

// 実用的な例
let userInput: string = "test";
let hasInput: boolean = !!userInput;      // true
```

## 重要なポイント
1. **二重否定**: 値をboolean型に変換
2. **簡潔性**: Boolean()関数より簡潔
3. **実用性**: 型変換に活用

## 次のステップ
次回は、二重否定での型変換について学習します。
