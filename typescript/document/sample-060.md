# #060 「indexOf()の戻り値」

## 概要
TypeScript v5.9のindexOf()の戻り値について学習します。見つかった場合と見つからない場合の戻り値を理解します。

## 学習目標
- indexOf()の戻り値の型を理解する
- 見つかった場合の動作を理解する
- 見つからない場合の動作を理解する

## 画面表示用コード

```typescript
// indexOf()の戻り値
let message: string = "Hello, World!";

// 見つかった場合
let foundIndex: number = message.indexOf("World"); // 7
let foundIndex2: number = message.indexOf("Hello"); // 0

// 見つからない場合
let notFoundIndex: number = message.indexOf("TypeScript"); // -1

// 型チェック
console.log(typeof foundIndex); // "number"
console.log(typeof notFoundIndex); // "number"

// 実用的な例
let userInput: string = "alice@example.com";
let atIndex: number = userInput.indexOf("@");
if (atIndex !== -1) {
  console.log("メールアドレス形式です");
}
```

## 重要なポイント
1. **戻り値の型**: 常にnumber型
2. **見つかった場合**: インデックス（0以上）
3. **見つからない場合**: -1

## 次のステップ
次回は、indexOf()で存在チェックについて学習します。