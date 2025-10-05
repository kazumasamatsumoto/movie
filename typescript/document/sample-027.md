# #027 「配列要素の埋め込み - ${arr[0]}」

## 概要
TypeScript v5.9の配列要素埋め込みについて学習します。${}内で配列の要素にアクセスして埋め込む機能を理解します。

## 学習目標
- 配列要素埋め込みの基本を理解する
- インデックスでのアクセス方法を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// 配列要素埋め込みの例
let fruits: string[] = ["apple", "banana", "orange"];
let numbers: number[] = [1, 2, 3, 4, 5];
let users: string[] = ["Alice", "Bob", "Charlie"];

// 配列要素の埋め込み
let firstFruit: string = `First fruit: ${fruits[0]}`;
let lastNumber: string = `Last number: ${numbers[numbers.length - 1]}`;
let secondUser: string = `Second user: ${users[1]}`;

// 実用的な例
let tags: string[] = ["TypeScript", "JavaScript", "Web開発"];
let firstTag: string = `Primary tag: ${tags[0]}`;
let allTags: string = `Tags: ${tags.join(", ")}`;
```

## 重要なポイント
1. **インデックスアクセス**: ${array[index]}で要素にアクセス
2. **動的インデックス**: 計算結果をインデックスとして使用可能
3. **配列メソッド**: join()などの配列メソッドも使用可能

## 次のステップ
次回は、複数の変数埋め込みについて学習します。