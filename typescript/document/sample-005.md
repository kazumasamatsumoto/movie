# #005 「型推論でstring型 - let name = "Bob"」

## 概要
TypeScript v5.9の型推論機能を使用して、より簡潔にstring型を扱う方法を学習します。明示的な型注釈なしで型安全性を保つ方法を理解します。

## 学習目標
- 型推論の基本概念を理解する
- 型推論と明示的型注釈の違いを理解する
- 型推論の利点と注意点を理解する

## 画面表示用コード

```typescript
// 型推論の例
let name = "Bob";        // string型と推論
let message = 'Hello';   // string型と推論
let template = `World`;  // string型と推論

// 型安全性は保たれる
// name = 123; // エラー: Type 'number' is not assignable to type 'string'

// 明示的型注釈との比較
let explicit: string = "Bob";  // 明示的
let inferred = "Bob";          // 推論
```

## 重要なポイント
1. **自動型判定**: 代入された値から型を自動推論
2. **コードの簡潔性**: 型注釈を書く手間が省ける
3. **型安全性**: 推論された型に対して型チェックが行われる

## 次のステップ
次回は、constを使った定数としてのstring型について学習します。