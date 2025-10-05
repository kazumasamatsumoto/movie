# #162 「自動ボックス化」

## 概要
TypeScript v5.9の自動ボックス化について学習します。プリミティブ型が自動的にオブジェクト型に変換される機能を理解します。

## 学習目標
- 自動ボックス化の仕組みを理解する
- メソッド呼び出し時の変換を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// 自動ボックス化の例
let num: number = 30;

// メソッド呼び出し時に自動ボックス化
let numStr: string = num.toString(); // 自動的にNumberオブジェクトに変換
let numFixed: string = num.toFixed(2); // 自動的にNumberオブジェクトに変換

// プロパティアクセス時も自動ボックス化
let numStr2: string = num.toString(); // 自動的にNumberオブジェクトに変換

// 実用的な例
let userAge: number = 25;
let ageStr: string = userAge.toString();
let ageFixed: string = userAge.toFixed(0);
```

## 重要なポイント
1. **自動変換**: メソッド呼び出し時に自動的にオブジェクト化
2. **透明性**: 開発者は意識する必要がない
3. **実用性**: メソッドの使用が可能

## 次のステップ
次回は、==と===での比較について学習します。
