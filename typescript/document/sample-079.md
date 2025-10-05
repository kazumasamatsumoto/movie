# #079 「配列のfilter」

## 概要
TypeScript v5.9の配列filterについて学習します。条件に合う要素だけを抽出して新しい配列を作るメソッドを理解します。

## 学習目標
- filter()メソッドの基本を理解する
- 条件による要素抽出を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// 配列のfilter
let names: string[] = ["Alice", "Bob", "Charlie", "David"];

// 長さが4文字以上の名前を抽出
let longNames: string[] = names.filter(name => name.length >= 4);
// ["Alice", "Charlie", "David"]

// 実用的な例
let userRoles: string[] = ["admin", "user", "guest", "moderator"];
let adminRoles: string[] = userRoles.filter(role => role.includes("admin"));
// ["admin"]

let productTags: string[] = ["本", "ペン", "ノート", "技術書"];
let bookTags: string[] = productTags.filter(tag => tag.includes("本"));
// ["本", "技術書"]
```

## 重要なポイント
1. **条件抽出**: 条件に合う要素のみを抽出
2. **新しい配列**: 元の配列は変更されない
3. **実用性**: データの絞り込みや検索結果に活用

## 次のステップ
次回は、配列のjoinについて学習します。