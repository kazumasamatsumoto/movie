# #035 「パフォーマンス考慮」

## 概要
TypeScript v5.9のテンプレートリテラルパフォーマンスについて学習します。テンプレートリテラルの実行速度やメモリ使用量を考慮した使用方法を理解します。

## 学習目標
- パフォーマンスの基本概念を理解する
- 効率的な使用方法を理解する
- 実用的な最適化例を理解する

## 画面表示用コード

```typescript
// パフォーマンス考慮の例
let users: string[] = ["Alice", "Bob", "Charlie"];

// 非効率：ループ内でテンプレートリテラル
// for (let user of users) {
//   console.log(`Hello, ${user}!`); // 毎回新しい文字列を作成
// }

// 効率的：事前に準備
let greetings: string[] = users.map(user => `Hello, ${user}!`);
greetings.forEach(greeting => console.log(greeting));

// 実用的な例
let productNames: string[] = ["本", "ペン", "ノート"];
let productList: string = productNames.map(name => `- ${name}`).join('\n');
```

## 重要なポイント
1. **文字列作成**: テンプレートリテラルは新しい文字列を作成
2. **ループ内**: ループ内での使用は注意が必要
3. **事前準備**: 可能な限り事前に準備する

## 次のステップ
次回は、デバッグのコツについて学習します。