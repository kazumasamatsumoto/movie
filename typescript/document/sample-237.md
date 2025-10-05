# #237 「二重否定での型変換」

## 概要
TypeScript v5.9の二重否定での型変換について学習します。!!演算子で任意の値をboolean型に変換する機能を理解します。

## 学習目標
- 二重否定での型変換の仕組みを理解する
- truthy/falsy値の変換を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// 二重否定での型変換
let str: string = "hello";
let num: number = 42;
let obj: object = {};
let arr: any[] = [];
let nullVal: null = null;
let undefinedVal: undefined = undefined;

// 型変換の例
let bool1: boolean = !!str;           // true
let bool2: boolean = !!num;           // true
let bool3: boolean = !!obj;           // true
let bool4: boolean = !!arr;           // true
let bool5: boolean = !!nullVal;       // false
let bool6: boolean = !!undefinedVal;  // false

// 実用的な例
let userInput: string = "test";
let hasInput: boolean = !!userInput;  // true
```

## 重要なポイント
1. **型変換**: 任意の値をboolean型に変換
2. **truthy値**: trueに変換される値
3. **falsy値**: falseに変換される値

## 次のステップ
次回は、論理演算子の優先順位について学習します。
