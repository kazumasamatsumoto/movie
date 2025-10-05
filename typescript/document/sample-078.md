# #078 「配列のmap」

## 概要
TypeScript v5.9の配列mapについて学習します。配列の各要素を変換して新しい配列を作るメソッドを理解します。

## 学習目標
- map()メソッドの基本を理解する
- 配列変換の方法を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// 配列のmap
let names: string[] = ["alice", "bob", "charlie"];

// 大文字に変換
let upperNames: string[] = names.map(name => name.toUpperCase());
// ["ALICE", "BOB", "CHARLIE"]

// 実用的な例
let userEmails: string[] = ["alice@example.com", "bob@example.com"];
let usernames: string[] = userEmails.map(email => email.split("@")[0]);
// ["alice", "bob"]

let productNames: string[] = ["本", "ペン", "ノート"];
let displayNames: string[] = productNames.map(name => `商品: ${name}`);
```

## 重要なポイント
1. **配列変換**: 各要素を変換して新しい配列を作成
2. **関数型**: 関数を引数として受け取る
3. **実用性**: データの変換や表示用の配列作成に活用

## 次のステップ
次回は、配列のfilterについて学習します。