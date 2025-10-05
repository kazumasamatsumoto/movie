# #088 「間違い(3) - undefinedとの混同」

## 概要
TypeScript v5.9の間違い(3)について学習します。string型とundefined型を混同してしまう間違いとその問題点を理解します。

## 学習目標
- undefinedとの混同の問題点を理解する
- 型の違いを理解する
- 正しい使用方法を理解する

## 画面表示用コード

```typescript
// 間違い(3) - undefinedとの混同

// ❌ 間違い：型の混同
// let name: string = undefined; // エラー

// ✅ 正しい：undefined許可型の使用
let name: string | undefined = undefined;
let message: string | undefined = "Hello";

// 実用的な例
let userName: string | undefined = undefined;
let userEmail: string | undefined = "alice@example.com";

// undefinedチェック
if (userName !== undefined) {
  console.log(userName.toUpperCase());
}
```

## 重要なポイント
1. **型の混同**: string型とundefined型は異なる
2. **ユニオン型**: string | undefinedでundefined許可型を定義
3. **undefinedチェック**: 安全な処理のために必要

## 次のステップ
次回は、デバッグ(1)について学習します。