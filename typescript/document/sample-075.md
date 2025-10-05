# #075 「配列への要素追加」

## 概要
TypeScript v5.9の配列要素追加について学習します。push()メソッドやインデックス指定で配列に要素を追加する方法を理解します。

## 学習目標
- 配列要素追加の基本を理解する
- push()メソッドの使用方法を理解する
- 先頭追加の方法を理解する

## 画面表示用コード

```typescript
// 配列への要素追加
let names: string[] = ["Alice", "Bob"];

// 末尾に追加
names.push("Charlie"); // ["Alice", "Bob", "Charlie"]

// 先頭に追加
names.unshift("David"); // ["David", "Alice", "Bob", "Charlie"]

// 実用的な例
let userList: string[] = ["admin"];
userList.push("user");
userList.push("guest");

let productTags: string[] = ["本"];
productTags.push("技術書");
productTags.push("TypeScript");
```

## 重要なポイント
1. **push()**: 末尾に要素を追加
2. **unshift()**: 先頭に要素を追加
3. **動的追加**: 実行時に要素を追加可能

## 次のステップ
次回は、配列の要素アクセスについて学習します。