# #228 「ANDの短絡評価」

## 概要
TypeScript v5.9のANDの短絡評価について学習します。&&演算子で左側がfalseの場合、右側を評価しない機能を理解します。

## 学習目標
- ANDの短絡評価の仕組みを理解する
- パフォーマンスの向上を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// ANDの短絡評価
let isActive: boolean = false;
let hasPermission: boolean = true;

// 短絡評価の例
let result1 = isActive && hasPermission; // false（右側は評価されない）
let result2 = isActive && console.log("実行されない"); // false

// 実用的な例
let userLoggedIn: boolean = false;
let userData: string = "user123";

// 短絡評価を活用
let displayData = userLoggedIn && userData; // false（userDataは評価されない）
```

## 重要なポイント
1. **短絡評価**: 左側がfalseの場合、右側を評価しない
2. **パフォーマンス**: 不要な処理を避けてパフォーマンス向上
3. **実用性**: エラー回避とパフォーマンス向上に活用

## 次のステップ
次回は、ANDと型の関係について学習します。
