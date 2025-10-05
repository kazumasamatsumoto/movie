# #001 「string型とは - 文字列を扱う最も基本的な型」

## 概要
TypeScript v5.9のstring型について学習します。文字列データを扱うプリミティブ型として、型安全性を提供する重要な機能です。

## 学習目標
- string型の基本的な概念を理解する
- 型安全性の恩恵を理解する
- 文字列データの扱い方の基礎を習得する

## 画面表示用コード

```typescript
// string型の基本宣言
let name: string = "Alice";

// 型安全性の例
name = "Bob";     // OK
// name = 123;    // エラー: Type 'number' is not assignable to type 'string'

// 文字列メソッドの型チェック
console.log(name.toUpperCase()); // "BOB"
console.log(name.length);        // 3
```

## 重要なポイント
1. **型安全性**: string型を指定することで、文字列以外の値を代入しようとするとエラーになる
2. **IDEサポート**: 自動補完やリファクタリングが安全に実行される
3. **可読性**: コードの意図が明確になり、保守性が向上する

## 次のステップ
次回は、string型の宣言方法について詳しく学習します。