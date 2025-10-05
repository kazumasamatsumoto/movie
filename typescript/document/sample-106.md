# #106 「constでnumber型」

## 概要
TypeScript v5.9のconstでnumber型について学習します。再代入不可の定数として数値を扱う方法を理解します。

## 学習目標
- constを使った定数宣言の基本を理解する
- constとletの違いを理解する
- 定数として使うべき数値の例を理解する

## 画面表示用コード

```typescript
// constでの定数宣言
const MAX_USERS = 1000;
const PI = 3.14159;
const TAX_RATE = 0.1;

// 再代入はエラー
// MAX_USERS = 2000; // エラー: Cannot assign to 'MAX_USERS' because it is a constant

// 実用的な例
const API_TIMEOUT = 5000;
const MAX_RETRY_COUNT = 3;
const DEFAULT_PAGE_SIZE = 20;
```

## 重要なポイント
1. **再代入不可**: constで宣言した変数は再代入できない
2. **型推論**: 初期値から型が推論される
3. **定数の意図**: 変更されない値であることを明示

## 次のステップ
次回は、number型とリテラル型の違いについて学習します。