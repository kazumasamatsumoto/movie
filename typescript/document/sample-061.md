# #061 「indexOf()で存在チェック」

## 概要
TypeScript v5.9のindexOf()存在チェックについて学習します。indexOf()の戻り値を使って文字列の存在を確認する方法を理解します。

## 学習目標
- indexOf()を使った存在チェックを理解する
- 戻り値による判定方法を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// indexOf()で存在チェック
let message: string = "Hello, World!";
let userEmail: string = "alice@example.com";

// 存在チェック
let hasWorld: boolean = message.indexOf("World") !== -1; // true
let hasTypeScript: boolean = message.indexOf("TypeScript") !== -1; // false

// 実用的な例
let hasAtSymbol: boolean = userEmail.indexOf("@") !== -1; // true
let hasDomain: boolean = userEmail.indexOf(".com") !== -1; // true

// 条件分岐での使用
if (userEmail.indexOf("@") !== -1) {
  console.log("有効なメールアドレス形式です");
} else {
  console.log("無効なメールアドレス形式です");
}
```

## 重要なポイント
1. **存在チェック**: 戻り値が-1でないかチェック
2. **真偽値**: boolean型で結果を判定
3. **実用性**: バリデーションに活用

## 次のステップ
次回は、lastIndexOf()について学習します。