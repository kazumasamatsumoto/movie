# #170 「明示的な型変換」

## 概要
TypeScript v5.9の明示的な型変換について学習します。開発者が意図的に型を変換する方法を理解します。

## 学習目標
- 明示的な型変換の方法を理解する
- 型変換関数の使用方法を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// 明示的な型変換
let str: string = "123";
let bool: boolean = true;

// 明示的な変換
let num1: number = Number(str);      // 123
let num2: number = parseInt(str);    // 123
let num3: number = Number(bool);     // 1

// 実用的な例
let userInput: string = "25";
let userAge: number = Number(userInput); // 明示的に変換

let isActive: boolean = true;
let activeValue: number = Number(isActive); // 明示的に変換
```

## 重要なポイント
1. **明示的**: 開発者が意図的に型を変換
2. **安全性**: 予測可能な結果
3. **推奨**: 暗黙的変換より明示的変換を推奨

## 次のステップ
次回は、変換失敗時について学習します。
