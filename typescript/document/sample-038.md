# #038 「よくある間違い(2)」

## 概要
TypeScript v5.9のテンプレートリテラルよくある間違い続きについて学習します。エスケープの問題、複雑な式、パフォーマンスの問題を理解します。

## 学習目標
- 追加の間違いパターンを理解する
- エスケープの問題を理解する
- パフォーマンスの問題を理解する

## 画面表示用コード

```typescript
// よくある間違いの例（続き）

// 4. 複雑すぎる式（間違い）
// let complex = `Result: ${someFunction() + anotherFunction() * 2}`; // 読みにくい

// 正しい方法
let result1: number = someFunction();
let result2: number = anotherFunction() * 2;
let simple: string = `Result: ${result1 + result2}`;

// 5. エスケープの問題
let codeExample: string = `Code: \`const name = "test"\``; // 正しいエスケープ

// 6. パフォーマンスの問題
let items: string[] = ["a", "b", "c"];
// 非効率: ループ内でテンプレートリテラル
// 効率: 事前に準備
let itemList: string = items.map(item => `- ${item}`).join('\n');
```

## 重要なポイント
1. **複雑な式**: 読みにくい式は分割する
2. **エスケープ**: 適切なエスケープが必要
3. **パフォーマンス**: ループ内での使用は注意

## 次のステップ
次回は、ベストプラクティスについて学習します。