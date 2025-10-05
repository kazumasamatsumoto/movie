# #203 「trueの代入」

## 概要
TypeScript v5.9のtrueの代入について学習します。boolean型の変数にtrue値を代入する方法を理解します。

## 学習目標
- true値の代入方法を理解する
- 真値の使用場面を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// trueの代入
let isActive: boolean = true;
let isCompleted: boolean = true;
let hasPermission: boolean = true;

// 実用的な例
let userLoggedIn: boolean = true;
let formValid: boolean = true;
let dataLoaded: boolean = true;

// 条件分岐での使用
if (isActive) {
  console.log("アクティブです");
}
```

## 重要なポイント
1. **真値**: trueは真を表す値
2. **フラグ**: 有効状態を表す
3. **条件分岐**: if文の条件で使用

## 次のステップ
次回は、falseの代入について学習します。
