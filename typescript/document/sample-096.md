# #096 「ベストプラクティス(3)」

## 概要
TypeScript v5.9のベストプラクティス(3)について学習します。string型の高度な使用パターンを理解します。

## 学習目標
- 高度な使用パターンを理解する
- 型ガードの使用方法を理解する
- ユニオン型の活用を理解する

## 画面表示用コード

```typescript
// ベストプラクティス(3)

// 1. 型ガード
function isString(value: unknown): value is string {
  return typeof value === "string";
}

// 2. ユニオン型
let status: "loading" | "success" | "error" = "loading";

// 3. オプショナル型
let userName: string | undefined = undefined;
let userEmail: string | null = null;

// 実用的な例
if (isString(userName)) {
  console.log(userName.toUpperCase());
}
```

## 重要なポイント
1. **型ガード**: 実行時の型チェック
2. **ユニオン型**: 複数の型の組み合わせ
3. **オプショナル型**: 未定義の可能性を表現

## 次のステップ
次回は、実践パターン(1)について学習します。