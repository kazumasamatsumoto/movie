# #131 「Number.isFinite()」

## 概要
TypeScript v5.9のNumber.isFinite()について学習します。より厳密な有限数判定を行う関数として、isFinite()との違いを理解します。

## 学習目標
- Number.isFinite()の基本を理解する
- isFinite()との違いを理解する
- 適切な使い分けを理解する

## 画面表示用コード

```typescript
// Number.isFinite()
let normalNumber: number = 100;
let stringNumber: string = "123";

// isFinite() - 型変換あり
let isFinite1: boolean = isFinite(normalNumber); // true
let isFinite2: boolean = isFinite(stringNumber); // true (型変換される)

// Number.isFinite() - 型変換なし
let isFinite3: boolean = Number.isFinite(normalNumber); // true
let isFinite4: boolean = Number.isFinite(stringNumber); // false (型変換されない)

// 実用的な例
let userInput: number = 42;
if (Number.isFinite(userInput)) {
  console.log("有効な数値です");
}
```

## 重要なポイント
1. **型変換**: isFinite()は型変換を行う
2. **厳密性**: Number.isFinite()は型変換を行わない
3. **推奨**: Number.isFinite()の使用が推奨される

## 次のステップ
次回は、Number.isInteger()について学習します。