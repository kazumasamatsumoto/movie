# #090 「デバッグ(2) - 実行時エラー」

## 概要
TypeScript v5.9のデバッグ(2)について学習します。プログラム実行時に発生するエラーとその対処方法を理解します。

## 学習目標
- 実行時エラーの種類を理解する
- エラーの原因を理解する
- 安全な処理方法を理解する

## 画面表示用コード

```typescript
// デバッグ(2) - 実行時エラー

// null参照エラーの回避
let name: string | null = null;
if (name !== null) {
  console.log(name.toUpperCase()); // 安全
}

// 未定義プロパティの回避
let user: { name?: string } = {};
if (user.name) {
  console.log(user.name.toUpperCase()); // 安全
}

// 型変換エラーの回避
let input: unknown = "Hello";
if (typeof input === "string") {
  console.log(input.toUpperCase()); // 安全
}
```

## 重要なポイント
1. **null参照エラー**: null値へのアクセス
2. **未定義プロパティ**: 存在しないプロパティへのアクセス
3. **型ガード**: 安全な処理のために必要

## 次のステップ
次回は、パフォーマンス最適化(1)について学習します。