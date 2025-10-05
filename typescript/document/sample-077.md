# #077 「配列のループ - for...of」

## 概要
TypeScript v5.9の配列ループについて学習します。for...of文を使って配列の要素を順番に処理する方法を理解します。

## 学習目標
- for...of文の基本を理解する
- 配列の要素処理を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// 配列のループ
let names: string[] = ["Alice", "Bob", "Charlie"];

// for...of文
for (let name of names) {
  console.log(name);
}

// 実用的な例
let userRoles: string[] = ["admin", "user", "guest"];
for (let role of userRoles) {
  console.log(`Role: ${role}`);
}

let productTags: string[] = ["本", "ペン", "ノート"];
for (let tag of productTags) {
  console.log(`Tag: ${tag}`);
}
```

## 重要なポイント
1. **for...of**: 配列の要素を順番に処理
2. **シンプル**: インデックスを意識せずに処理
3. **実用性**: リストの表示や処理に活用

## 次のステップ
次回は、配列のmapについて学習します。