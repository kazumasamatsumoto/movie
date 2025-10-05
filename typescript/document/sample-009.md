# #009 「string型とundefined - 初期化前のアクセス」

## 概要
TypeScript v5.9のstring型とundefinedについて学習します。初期化前の変数アクセスと安全な初期化方法を理解します。

## 学習目標
- 初期化前の変数の状態を理解する
- undefinedの概念を理解する
- 安全な初期化方法を習得する

## 画面表示用コード

```typescript
// 初期化前のアクセス
let name: string;
// console.log(name); // undefined

// 安全な初期化
let userName: string = "初期値";
console.log(userName); // "初期値"

// undefinedチェック
let optionalName: string | undefined;
if (optionalName !== undefined) {
  console.log(optionalName.toUpperCase());
}

// 実用的な例
let componentTitle: string = "";
let apiResponse: string | undefined;
```

## 重要なポイント
1. **未初期化**: letで宣言した変数は初期化前はundefined
2. **安全な初期化**: 宣言と同時に初期値を設定
3. **undefinedチェック**: オプショナルな値の安全な処理

## 次のステップ
次回は、string型のスコープについて学習します。

