# #025 「関数呼び出しの埋め込み - ${getName()}」

## 概要
TypeScript v5.9の関数呼び出し埋め込みについて学習します。${}内で関数を呼び出して戻り値を埋め込む機能を理解します。

## 学習目標
- 関数呼び出し埋め込みの基本を理解する
- 戻り値のある関数の使用方法を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// 関数呼び出し埋め込みの例
function getName(): string {
  return "Alice";
}

function getAge(): number {
  return 30;
}

function isAdult(age: number): boolean {
  return age >= 18;
}

// 関数呼び出しの埋め込み
let greeting: string = `Hello, ${getName()}!`;
let ageInfo: string = `Age: ${getAge()}`;
let adultStatus: string = `Adult: ${isAdult(getAge())}`;

// 実用的な例
function formatPrice(price: number): string {
  return `¥${price.toLocaleString()}`;
}

let productPrice: string = `Price: ${formatPrice(2980)}`;
```

## 重要なポイント
1. **関数実行**: ${}内で関数を呼び出して結果を埋め込み
2. **戻り値**: 関数の戻り値が文字列に変換される
3. **チェーン**: 関数の戻り値を別の関数に渡すことも可能

## 次のステップ
次回は、オブジェクトプロパティの埋め込みについて学習します。