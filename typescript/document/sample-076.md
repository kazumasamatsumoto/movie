# #076 「配列の要素アクセス」

## 概要
TypeScript v5.9の配列要素アクセスについて学習します。インデックスを使って配列の要素にアクセスする方法を理解します。

## 学習目標
- インデックスアクセスの基本を理解する
- 配列の要素取得方法を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// 配列の要素アクセス
let names: string[] = ["Alice", "Bob", "Charlie"];

// インデックスでアクセス
let first: string = names[0]; // "Alice"
let second: string = names[1]; // "Bob"
let last: string = names[names.length - 1]; // "Charlie"

// 実用的な例
let userRoles: string[] = ["admin", "user", "guest"];
let adminRole: string = userRoles[0]; // "admin"
let userRole: string = userRoles[1]; // "user"
```

## 重要なポイント
1. **インデックス**: 0から始まる位置指定
2. **要素取得**: 指定位置の要素を取得
3. **範囲外アクセス**: 未定義を返す

## 次のステップ
次回は、配列のループについて学習します。