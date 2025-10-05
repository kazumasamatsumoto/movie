# #074 「string配列の初期化」

## 概要
TypeScript v5.9のstring配列初期化について学習します。宣言と同時に値を設定する効率的な方法を理解します。

## 学習目標
- 配列初期化の基本を理解する
- 初期値の設定方法を理解する
- 型推論との関係を理解する

## 画面表示用コード

```typescript
// string配列の初期化
let names: string[] = ["Alice", "Bob", "Charlie"];
let emails: string[] = ["alice@example.com", "bob@example.com"];
let emptyArray: string[] = [];

// 実用的な例
let userRoles: string[] = ["admin", "user", "guest"];
let productCategories: string[] = ["本", "ペン", "ノート"];
let errorMessages: string[] = ["エラー1", "エラー2"];

// 型推論でも配列型
let inferred = ["TypeScript", "JavaScript"]; // string[]型と推論
```

## 重要なポイント
1. **初期化**: 宣言と同時に値を設定
2. **空配列**: 初期値として空配列を使用
3. **型推論**: 配列リテラルから型を自動推論

## 次のステップ
次回は、配列への要素追加について学習します。