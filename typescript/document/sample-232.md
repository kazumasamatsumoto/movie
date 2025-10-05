# #232 「ORの短絡評価」

## 概要
TypeScript v5.9のORの短絡評価について学習します。||演算子で左側がtruthyの場合、右側を評価しない機能を理解します。

## 学習目標
- ORの短絡評価の仕組みを理解する
- パフォーマンスの向上を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// ORの短絡評価
let isActive: boolean = true;
let hasPermission: boolean = false;

// 短絡評価の例
let result1 = isActive || hasPermission; // true（右側は評価されない）
let result2 = isActive || console.log("実行されない"); // true

// 実用的な例
let userLoggedIn: boolean = true;
let defaultUser: string = "Guest";

// 短絡評価を活用
let displayUser = userLoggedIn || defaultUser; // true（defaultUserは評価されない）
```

## 重要なポイント
1. **短絡評価**: 左側がtruthyの場合、右側を評価しない
2. **パフォーマンス**: 不要な処理を避けてパフォーマンス向上
3. **実用性**: デフォルト値設定とパフォーマンス向上に活用

## 次のステップ
次回は、ORとデフォルト値について学習します。
