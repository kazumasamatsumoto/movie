# #047 「自動ボックス化」

## 概要
TypeScript v5.9の自動ボックス化について学習します。プリミティブ型が自動的にオブジェクト型に変換される機能を理解します。

## 学習目標
- 自動ボックス化の概念を理解する
- 発生するタイミングを理解する
- 実用的な例を理解する

## 画面表示用コード

```typescript
// 自動ボックス化の例
let str: string = "Hello";

// メソッド呼び出し時に自動ボックス化
let upperStr: string = str.toUpperCase(); // 自動的にStringオブジェクトに変換
let lowerStr: string = str.toLowerCase(); // 自動的にStringオブジェクトに変換

// プロパティアクセス時も自動ボックス化
let length: number = str.length; // 自動的にStringオブジェクトに変換

// 実用的な例
let userName: string = "Alice";
let userNameUpper: string = userName.toUpperCase();
let userNameLength: number = userName.length;
let userNameFirst: string = userName.charAt(0);
```

## 重要なポイント
1. **自動変換**: メソッド呼び出し時に自動的にオブジェクト化
2. **透明性**: 開発者は意識する必要がない
3. **パフォーマンス**: 必要な時のみオブジェクト化

## 次のステップ
次回は、==と===での比較について学習します。