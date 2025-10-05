# #198 「間違い(3) - 文字列との混同」

## 概要
TypeScript v5.9の文字列との混同について学習します。数値と文字列を混同して使用する間違いを理解します。

## 学習目標
- 文字列との混同の間違いを理解する
- 型の不一致問題を理解する
- 適切な型変換方法を理解する

## 画面表示用コード

```typescript
// 間違い(3) - 文字列との混同
let userInput: string = "25";
let userAge: number = 25;

// ❌ 間違い
// let total: number = userInput + userAge; // "2525"

// ✅ 正しい方法
let total: number = Number(userInput) + userAge; // 50

// 実用的な例
let priceStr: string = "1500";
let price: number = 1500;

// 型安全な処理
let totalPrice: number = Number(priceStr) + price;
console.log(totalPrice); // 3000
```

## 重要なポイント
1. **間違い**: 数値と文字列を混同
2. **問題**: 型の不一致や予期しない動作
3. **解決**: 明示的な型変換を使用

## 次のステップ
次回は、ベストプラクティスについて学習します。
