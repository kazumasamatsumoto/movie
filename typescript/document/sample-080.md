# #080 「配列のjoin」

## 概要
TypeScript v5.9の配列joinについて学習します。配列の要素を結合して一つの文字列にするメソッドを理解します。

## 学習目標
- join()メソッドの基本を理解する
- 区切り文字の指定方法を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// 配列のjoin
let names: string[] = ["Alice", "Bob", "Charlie"];

// カンマで結合
let joined: string = names.join(", "); // "Alice, Bob, Charlie"

// 実用的な例
let userRoles: string[] = ["admin", "user", "guest"];
let roleList: string = userRoles.join(" | "); // "admin | user | guest"

let productTags: string[] = ["本", "ペン", "ノート"];
let tagString: string = productTags.join(", "); // "本, ペン, ノート"

let errorMessages: string[] = ["エラー1", "エラー2"];
let errorText: string = errorMessages.join("\n"); // 改行で結合
```

## 重要なポイント
1. **文字列結合**: 配列の要素を一つの文字列に結合
2. **区切り文字**: 任意の文字列で区切りを指定
3. **実用性**: リストの表示やデータの出力に活用

## 次のステップ
次回は、Angularコンポーネントのstring型について学習します。