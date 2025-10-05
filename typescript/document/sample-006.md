# #006 「constでstring型 - const name = "Charlie"」

## 概要
TypeScript v5.9のconstを使用したstring型の定数宣言について学習します。再代入不可の定数として文字列を扱う方法を理解します。

## 学習目標
- constを使った定数宣言の基本を理解する
- constとletの違いを理解する
- 定数として使うべき文字列の例を理解する

## 画面表示用コード

```typescript
// constでの定数宣言
const API_URL = "https://api.example.com";
const APP_NAME = "MyApp";
const VERSION = "1.0.0";

// 再代入はエラー
// API_URL = "https://other.com"; // エラー: Cannot assign to 'API_URL'

// 型推論でstring型
console.log(API_URL.toUpperCase()); // "HTTPS://API.EXAMPLE.COM"
```

## 重要なポイント
1. **再代入不可**: constで宣言した変数は再代入できない
2. **型推論**: 初期値から型が推論される
3. **定数の意図**: 変更されない値であることを明示

## 次のステップ
次回は、string型とリテラル型の違いについて学習します。