# #165 「Number型使用禁止」

## 概要
TypeScript v5.9のNumber型使用禁止について学習します。Number型の使用を避けるべき理由とルールを理解します。

## 学習目標
- Number型使用禁止の理由を理解する
- 開発ルールの重要性を理解する
- 適切な代替方法を理解する

## 画面表示用コード

```typescript
// Number型使用禁止ルール

// ❌ 禁止：Number型の使用
// let age: Number = new Number(25);
// let price: Number = new Number(1500);

// ✅ 推奨：number型の使用
let age: number = 25;
let price: number = 1500;

// ✅ 推奨：型推論の活用
let userAge = 25; // number型と推論
let productPrice = 1500; // number型と推論

// 実用的な例
let componentProps = {
  age: 25,
  price: 1500
};
let userAge: number = componentProps.age;
```

## 重要なポイント
1. **禁止ルール**: Number型の使用は避けるべき
2. **推奨**: number型の使用
3. **型推論**: 型注釈を省略して型推論を活用

## 次のステップ
次回は、Number()関数について学習します。
