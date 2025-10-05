# #086 「間違い(1) - Stringを使う」

## 概要
TypeScript v5.9の間違い(1)について学習します。String型を使用してしまう間違いとその問題点を理解します。

## 学習目標
- String型の問題点を理解する
- string型との違いを理解する
- 正しい使用方法を理解する

## 画面表示用コード

```typescript
// 間違い(1) - Stringを使う

// ❌ 間違い：String型の使用
// let name: String = new String("Alice");
// let message: String = new String("Hello");

// ✅ 正しい：string型の使用
let name: string = "Alice";
let message: string = "Hello";

// 実用的な例
let userName: string = "Bob";
let userEmail: string = "bob@example.com";
let userInfo: string = `${userName} (${userEmail})`;
```

## 重要なポイント
1. **String型**: オブジェクト型（非推奨）
2. **string型**: プリミティブ型（推奨）
3. **問題点**: パフォーマンスと型の不一致

## 次のステップ
次回は、間違い(2)について学習します。