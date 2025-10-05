# #010 「string型のスコープ - ブロックスコープ」

## 概要
TypeScript v5.9のstring型スコープについて学習します。ブロックスコープの概念と変数の有効範囲を理解します。

## 学習目標
- ブロックスコープの基本概念を理解する
- letとconstのスコープを理解する
- 変数の名前衝突を防ぐ方法を理解する

## 画面表示用コード

```typescript
// ブロックスコープの例
{
  let blockScoped: string = "ブロック内";
  const blockConstant: string = "ブロック定数";
  // このブロック内でのみ有効
}

// console.log(blockScoped); // エラー: Cannot find name 'blockScoped'

// 実用的な例
function processData() {
  let localData: string = "ローカルデータ";
  
  if (true) {
    let conditionalData: string = "条件付きデータ";
    // このブロック内でのみ有効
  }
  
  return localData;
}
```

## 重要なポイント
1. **ブロックスコープ**: {}で囲まれた範囲内でのみ有効
2. **名前衝突回避**: 同じ名前の変数を異なるスコープで使用可能
3. **実用性**: 関数内や条件分岐での局所的な変数管理

## 次のステップ
次回は、ダブルクォート文字列について学習します。

