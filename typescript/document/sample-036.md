# #036 「デバッグのコツ」

## 概要
TypeScript v5.9のテンプレートリテラルデバッグについて学習します。テンプレートリテラルの問題を効率的に見つける方法を理解します。

## 学習目標
- デバッグの基本手法を理解する
- 変数確認の重要性を理解する
- 段階的な構築方法を理解する

## 画面表示用コード

```typescript
// デバッグのコツ
let userName: string = "Alice";
let userAge: number = 30;

// 1. 変数の確認
console.log("userName:", userName);
console.log("userAge:", userAge);

// 2. 段階的な構築
let part1: string = `Name: ${userName}`;
let part2: string = `Age: ${userAge}`;
let fullMessage: string = `${part1}, ${part2}`;

// 3. コンソール出力で確認
console.log("Full message:", fullMessage);

// 実用的な例
let product = { name: "本", price: 1000 };
let productInfo: string = `${product.name}: ¥${product.price}`;
console.log("Product info:", productInfo);
```

## 重要なポイント
1. **変数確認**: 埋め込む変数の値を確認
2. **段階的構築**: 複雑なテンプレートは分割して構築
3. **コンソール出力**: 結果を確認してデバッグ

## 次のステップ
次回は、よくある間違い(1)について学習します。