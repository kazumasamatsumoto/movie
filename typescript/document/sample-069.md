# #069 「slice(start, end)」

## 概要
TypeScript v5.9のslice()について学習します。指定した範囲の文字列を抽出するメソッドを理解します。

## 学習目標
- slice()の基本使用方法を理解する
- substring()との違いを理解する
- 負のインデックスの使用方法を理解する

## 画面表示用コード

```typescript
// slice()の使用例
let message: string = "Hello, World!";
let text: string = "TypeScript";

// 部分文字列の抽出
let hello: string = message.slice(0, 5); // "Hello"
let world: string = message.slice(7, 12); // "World"
let script: string = text.slice(4); // "Script"

// 負のインデックス
let lastChar: string = message.slice(-1); // "!"
let lastWord: string = message.slice(-6, -1); // "World"
```

## 重要なポイント
1. **範囲指定**: 開始位置と終了位置を指定
2. **負のインデックス**: 末尾からの位置指定が可能
3. **substring()との違い**: 負のインデックスが使用可能

## 次のステップ
次回は、split()について学習します。