# #009 「string型とundefined - 初期化前のアクセス」

## 概要
TypeScript v5.9のstring型の変数が初期化前の状態（undefined）について学習します。未初期化変数の扱い方と安全な初期化方法を理解します。

## 学習目標
- undefinedの概念を理解する
- 未初期化変数の問題を理解する
- 安全な初期化方法を習得する

## 画面表示用コード

```typescript
// 未初期化の変数
let name: string;
console.log(name); // undefined

// 安全なアクセス
if (name !== undefined) {
  console.log(name.toUpperCase());
} else {
  console.log("名前が設定されていません");
}

// 初期化で解決
let message: string = "Hello";
console.log(message); // "Hello"
```

## 重要なポイント
1. **未初期化状態**: 宣言のみでは値はundefined
2. **型と値の違い**: 型はstringだが値はundefined
3. **安全なアクセス**: undefinedチェックまたは初期化が必要

## 次のステップ
次回は、string型のスコープについて学習します。