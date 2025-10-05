# #212 「デフォルト値」

## 概要
TypeScript v5.9のboolean型のデフォルト値について学習します。boolean型の変数に初期値を設定する方法を理解します。

## 学習目標
- boolean型のデフォルト値設定を理解する
- 初期値の重要性を理解する
- 実用的な使用例を理解する

## 画面表示用コード

```typescript
// boolean型のデフォルト値
let isActive: boolean = true;        // デフォルト値: true
let isCompleted: boolean = false;    // デフォルト値: false
let hasPermission: boolean = true;   // デフォルト値: true

// 実用的な例
let userLoggedIn: boolean = false;   // デフォルト値: false
let formValid: boolean = false;      // デフォルト値: false
let dataLoaded: boolean = false;     // デフォルト値: false

// デフォルト値の活用
if (isActive) {
  console.log("アクティブです");
}
```

## 重要なポイント
1. **デフォルト値**: 宣言時に初期値を設定
2. **初期状態**: アプリケーションの初期状態を管理
3. **実用性**: 予測可能な動作を保つ

## 次のステップ
次回は、初期化のベストプラクティスについて学習します。
