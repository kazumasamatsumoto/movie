# #204 「falseの代入」

## 概要
TypeScript v5.9のfalseの代入について学習します。boolean型の変数にfalse値を代入する方法を理解します。

## 学習目標
- false値の代入方法を理解する
- 偽値の使用場面を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// falseの代入
let isActive: boolean = false;
let isCompleted: boolean = false;
let hasPermission: boolean = false;

// 実用的な例
let userLoggedIn: boolean = false;
let formValid: boolean = false;
let dataLoaded: boolean = false;

// 条件分岐での使用
if (!isActive) {
  console.log("非アクティブです");
}
```

## 重要なポイント
1. **偽値**: falseは偽を表す値
2. **フラグ**: 無効状態を表す
3. **否定**: !演算子で否定

## 次のステップ
次回は、型推論でboolean型について学習します。
