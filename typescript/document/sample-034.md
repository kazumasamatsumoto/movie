# #034 「ネストは避ける」

## 概要
TypeScript v5.9のテンプレートリテラルネストについて学習します。テンプレートリテラル内でテンプレートリテラルを使うことの問題点を理解します。

## 学習目標
- ネストの問題点を理解する
- シンプルな構造の重要性を理解する
- 代替案の使用方法を理解する

## 画面表示用コード

```typescript
// ネスト（非推奨）
let userName: string = "Alice";
let userRole: string = "admin";
// let nested: string = `User: \`${userName}\` with role \`${userRole}\``; // 複雑

// 推奨：シンプルな方法
let simple: string = `User: ${userName} with role ${userRole}`;

// 実用的な例
let productName: string = "TypeScript本";
let price: number = 2980;
let description: string = `${productName} - ¥${price}`; // シンプル

// 複雑な場合は分割
let part1: string = `Product: ${productName}`;
let part2: string = `Price: ¥${price}`;
let combined: string = `${part1} - ${part2}`;
```

## 重要なポイント
1. **可読性**: ネストは可読性を悪化させる
2. **エスケープ**: 複雑なエスケープが必要
3. **シンプル設計**: 分割やシンプルな構造を推奨

## 次のステップ
次回は、パフォーマンス考慮について学習します。