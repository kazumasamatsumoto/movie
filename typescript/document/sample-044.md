# #044 「Stringコンストラクタ - new String()」

## 概要
TypeScript v5.9のStringコンストラクタについて学習します。new String()でStringオブジェクトを作成する方法と問題点を理解します。

## 学習目標
- Stringコンストラクタの使用方法を理解する
- オブジェクト型の問題点を理解する
- 比較や型チェックの問題を理解する

## 画面表示用コード

```typescript
// Stringコンストラクタ（避けるべき）
// let strObj = new String("Hello"); // 非推奨

// 正しい方法：文字列リテラル
let str: string = "Hello";

// 型の違い
console.log(typeof str);        // "string"
// console.log(typeof strObj);  // "object"

// 比較の問題
let str1: string = "Hello";
let str2: string = "Hello";
console.log(str1 === str2); // true

// let obj1 = new String("Hello");
// let obj2 = new String("Hello");
// console.log(obj1 === obj2); // false
```

## 重要なポイント
1. **Stringコンストラクタ**: new String()でオブジェクト作成
2. **型の問題**: オブジェクト型になる
3. **比較の問題**: 異なるオブジェクトとして扱われる

## 次のステップ
次回は、Stringオブジェクトの問題点について学習します。