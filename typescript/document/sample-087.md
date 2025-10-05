# #087 「間違い(2) - nullとの混同」

## 概要
TypeScript v5.9の間違い(2)について学習します。string型とnull型を混同してしまう間違いとその問題点を理解します。

## 学習目標
- nullとの混同の問題点を理解する
- 型の違いを理解する
- 正しい使用方法を理解する

## 画面表示用コード

```typescript
// 間違い(2) - nullとの混同

// ❌ 間違い：型の混同
// let name: string = null; // エラー

// ✅ 正しい：null許可型の使用
let name: string | null = null;
let message: string | null = "Hello";

// 実用的な例
let userName: string | null = null;
let userEmail: string | null = "alice@example.com";

// nullチェック
if (userName !== null) {
  console.log(userName.toUpperCase());
}
```

## 重要なポイント
1. **型の混同**: string型とnull型は異なる
2. **ユニオン型**: string | nullでnull許可型を定義
3. **nullチェック**: 安全な処理のために必要

## 次のステップ
次回は、間違い(3)について学習します。